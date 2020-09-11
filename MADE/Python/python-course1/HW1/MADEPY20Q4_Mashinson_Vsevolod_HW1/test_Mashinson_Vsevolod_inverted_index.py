from textwrap import dedent
from argparse import Namespace,  ArgumentParser, ArgumentDefaultsHelpFormatter, FileType, ArgumentTypeError
import pytest
import sys
from io import TextIOWrapper, StringIO
import struct

from task_Mashinson_Vsevolod_inverted_index import \
    InvertedIndex, \
    build_inverted_index, \
    load_documents, \
    process_queries, \
    process_queries_by_lists, \
    callback_build, \
    callback_query, \
    DEFAULT_INVERTD_INDEX_STORE_PATH, \
    DEFAULT_DATASET_PATH, \
    setup_parser, \
    EncodedFileType, \
    StructStoragePolicy

DATASET_BIG_PATH = DEFAULT_DATASET_PATH

DATASET_TINY_STR = (
"""
123	some words A_word and nothing
2	some words B_word in this dataset
5	famous_phrases to be or not to be
37	all words such as A_word and B_word are here
"""
)

QUERIES_FILE_CONTENT = (
"""A_word
B_word
A_word B_word
A_word word_does_not_exist
"""
)

@pytest.fixture()
def queries_file_path(tmpdir):
    dataset_fio = tmpdir.join("queries.txt")
    dataset_fio.write(QUERIES_FILE_CONTENT)
    return dataset_fio


@pytest.fixture()
def tiny_dataset_fio(tmpdir):
    dataset_fio = tmpdir.join("dataset.txt")
    dataset_fio.write(DATASET_TINY_STR)
    return dataset_fio


def test_can_load_documents_v(tiny_dataset_fio):
    DATASET_TINY_ETALON = (
        {
            123: "some words A_word and nothing",
            2: "some words B_word in this dataset",
            5: "famous_phrases to be or not to be",
            37: "all words such as A_word and B_word are here",
        }
    )
    documents = load_documents(tiny_dataset_fio)
    assert DATASET_TINY_ETALON == documents, (
        "load_documents incorrectly loaded dataset"
    )

@pytest.mark.parametrize(
    "query, etalon_answer",
    [
        pytest.param([], [], id="empty_query"),
        pytest.param(["A_word"], [123, 37]),
        pytest.param(["B_word"], [2, 37], id="B_word"),
        pytest.param(["A_word", "B_word"], [37], id="both_words"),
        pytest.param(["word_does_not_exist"], [], id="word does not exist"),
    ]
)


def test_query_inverted_index_intersect_results(tiny_dataset_fio, query, etalon_answer):
    documents = load_documents(tiny_dataset_fio)
    tiny_inverted_index = build_inverted_index(documents)
    answer = tiny_inverted_index.query(query)
    assert sorted(answer) == sorted(etalon_answer), (
        f"Expected answer is {etalon_answer}, but you got {answer}"
    )


def test_split_by_index_and_text():
    text = "123	abs ddd	ttt"
    expected = (123, "abs ddd	ttt")
    actual = InvertedIndex.split_by_index_and_text(text)
    assert expected == actual


def test_get_words_can_split_line_correctly():
    text = "   one or another   word,  test "
    expected_words = ["one", "or", "another", "word,", "test"]
    words = InvertedIndex.get_words(text)
    assert expected_words == words, (
        "expected words and parsed words are not the same"
    )


def test_get_words_return_empty_list_for_empty_text():
    text = ""
    expected_words = []
    words = InvertedIndex.get_words(text)
    assert expected_words == words


def test_get_words_raise_exception_for_none():
    with pytest.raises(AttributeError):
        InvertedIndex.get_words(None)

@pytest.mark.skip
def test_can_load_wikipedia_sample(wikipedia_documents):
    assert len(wikipedia_documents) == 4100, (
        "you incorrectrly loaded Wikipedia sample"
    )

@pytest.fixture()
def wikipedia_documents():
    return load_documents(DATASET_BIG_PATH)

@pytest.mark.skip
def test_can_build_and_query_inverted_index(wikipedia_documents):
    wiki_inverted_index = build_inverted_index(wikipedia_documents)
    doc_ids = wiki_inverted_index.query(["wikipedia"])
    assert isinstance(doc_ids, list), "inverted index query should return list"


@pytest.fixture()
def wikipedia_inverted_index(wikipedia_documents):
    return build_inverted_index(wikipedia_documents)

@pytest.fixture()
def small_wikipedia_inverted_index(tiny_dataset_fio):
    return build_inverted_index(load_documents(tiny_dataset_fio))


def test_inverted_index_equality():
    dic_lhs = {1: "abc bcd", 2: "bcd abc"}
    lhs_index = InvertedIndex.from_documents(dic_lhs)

    dic_rhs = {2: "bcd abc", 1: "abc  bcd"}
    rhs_index = InvertedIndex.from_documents(dic_lhs)

    dic_other = {2: "bcd abc", 1: "abc bcd", 3: "e a"}
    other_index = InvertedIndex.from_documents(dic_other)

    assert lhs_index == rhs_index 
    assert rhs_index == lhs_index
    assert lhs_index != other_index

def __check_index(path, index):
    index_fio = path.join("index.dump")
    expected_index = index
    expected_index.dump(index_fio)
    loaded_invertd_index = InvertedIndex.load(index_fio)
    assert expected_index == loaded_invertd_index, (
        "load should return the same inverted index"
    )


def test_can_dump_and_load_small_wikipedia_inverted_index(tmpdir, small_wikipedia_inverted_index):
    __check_index(tmpdir, small_wikipedia_inverted_index)

@pytest.mark.skip
def test_can_dump_and_load_big_wikipedia_inverted_index(tmpdir, wikipedia_inverted_index):
    __check_index(tmpdir, wikipedia_inverted_index)


def test_process_queries_can_process_all_queries_from_provided_file(small_wikipedia_inverted_index, queries_file_path, capsys):
    small_wikipedia_inverted_index.dump(DEFAULT_INVERTD_INDEX_STORE_PATH)
    with open(queries_file_path) as queries_file:
        process_queries(
            inverted_index_filepath=DEFAULT_INVERTD_INDEX_STORE_PATH,
            query_file=queries_file
        )
    captured = capsys.readouterr()
    assert captured.out == "123,37\n2,37\n37\n\n"
    assert captured.err == ""


def test_process_queries_can_process_all_queries_from_stdin(capsys):
    process_queries_by_lists(
        inverted_index_filepath=DEFAULT_INVERTD_INDEX_STORE_PATH,
        queries=[['A_word'], ['B_word'], ['A_word', 'B_word'], ['not_exists']]
    )
    captured = capsys.readouterr()
    assert captured.out == "123,37\n2,37\n37\n\n"
    assert captured.err == ""

def test_callback_query_from_file(queries_file_path, capsys):
    with open(queries_file_path) as queries_file:
        arguments = Namespace(
            inverted_index_filepath=DEFAULT_INVERTD_INDEX_STORE_PATH,
            query_file=queries_file,
            query=None
        )
        callback_query(arguments)
    captured = capsys.readouterr()
    assert captured.out == "123,37\n2,37\n37\n\n"
    assert captured.err == ""

def test_callback_query_from_stdin(capsys):
    arguments = Namespace(
        inverted_index_filepath=DEFAULT_INVERTD_INDEX_STORE_PATH,
        query_file=None,
        query=[['A_word'], ['B_word'], ['A_word', 'B_word'], ['not_exists']]
    )
    callback_query(arguments)
    captured = capsys.readouterr()
    assert captured.out == "123,37\n2,37\n37\n\n"
    assert captured.err == ""

def test_callback_build(tiny_dataset_fio, tmpdir):
    arguments = Namespace(
        dataset=tiny_dataset_fio,
        output=tmpdir.join("text.index"),
    )
    callback_build(arguments)


def test_StructStoragePolicy(tmpdir):
    dic = {
        'abc defα𓀂': {1, 7, 13, 2},
        "βα": {1, 1, 53, 29123}
    }
    expected = {}
    filepath = tmpdir.join("index.index")
    with open(filepath, "wb") as fout:
        StructStoragePolicy.dump_dic(dic, fout)

    with open(filepath, "rb") as fin:
        expected = StructStoragePolicy.decode_dic(fin)
    
    assert(expected == dic)

