#!/usr/bin/env python3
"""
Inverted index module
"""
from collections import defaultdict
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType, ArgumentTypeError
from io import TextIOWrapper
import sys
import struct

class StructStoragePolicy:
    """StructStoragePolicy"""
    @classmethod
    def dump_list(cls, arr, fout):
        """dump_list"""
        fout.write(struct.pack('i', len(arr)))
        for element in arr:
            packed = struct.pack('h', element)
            fout.write(packed)

    @classmethod
    def decode_list(cls, fin):
        """decode_list"""
        packed = fin.read(4)
        count = struct.unpack('i', packed)[0]
        packed = fin.read(2 * count)
        format_str = f'{count}h'
        result = list(struct.unpack(format_str, packed))
        return result

    @classmethod
    def dump_string(cls, string, fout):
        """dump_string"""
        string = string.encode(encoding="utf-8")
        bytes_lenght = len(string)
        format_str = f'{bytes_lenght}s'
        length_packed = struct.pack('i', bytes_lenght)
        string_packed = struct.pack(format_str, string)
        fout.write(length_packed)
        fout.write(string_packed)

    @classmethod
    def decode_string(cls, fin):
        """decode_string"""
        count = struct.unpack('i', fin.read(4))[0]
        packed = fin.read(count)
        format_str = f'{count}s'
        result = struct.unpack(format_str, packed)[0].decode()
        return result

    @classmethod
    def dump_dic(cls, dic, fout):
        """dump_dic"""
        fout.write(struct.pack('i', len(dic)))
        for key, value in dic.items():
            cls.dump_string(key, fout)
            cls.dump_list(value, fout)

    @classmethod
    def decode_dic(cls, fin):
        """decode_dic"""
        count = struct.unpack('i', fin.read(4))[0]
        result = defaultdict(set)
        for _ in range(count):
            key = cls.decode_string(fin)
            value = cls.decode_list(fin)
            result[key] = set(value)
        return result


class EncodedFileType(FileType):
    """EncodedFileType"""
    def __call__(self, string):
        # the special argument "-" means sys.std{in,out}
        if string == '-':
            if 'r' in self._mode:
                stdin = TextIOWrapper(sys.stdin.buffer, encoding=self._encoding)
                return stdin

            if 'w' in self._mode:
                stdout = TextIOWrapper(sys.stdout.buffer, encoding=self._encoding)
                return stdout

            msg = 'argument "-" with mode %r' % self._mode
            raise ValueError(msg)

        # all other arguments are used as file names
        try:
            return open(string, self._mode, self._bufsize, self._encoding,
                        self._errors)
        except OSError as error:
            message = "can't open '%s': %s"
            raise ArgumentTypeError(message % (string, error)) from error


class InvertedIndex:
    """Inverted index model"""

    def __init__(self, storage):
        """initialize index from dictionary
        @param: storage: key-value storage
        """
        self._storage = storage
        self._storage_policy = StructStoragePolicy()


    @classmethod
    def from_documents(cls, documents_to_id_map):
        """-_-"""
        storage = defaultdict(set)
        for text_id, text in documents_to_id_map.items():
            text_words = InvertedIndex.get_words(text)

            for word in text_words:
                storage[word].add(text_id)

        return InvertedIndex(storage)


    def query(self, words: list) -> list:
        """-_-"""
        if len(words) == 0 or words[0] not in self._storage:
            return []

        assert isinstance(words, list), {
            "query should be provided with a list of words, but user provided "f"{repr(words)}"
        }
        result = set(self._storage[words[0]])
        for word in words:
            if word not in self._storage:
                return []

            result &= self._storage[word]

        return list(result)


    def dump(self, filepath: str):
        """-_-"""
        with open(filepath, "wb") as fout:
            self._storage_policy.dump_dic(self._storage, fout)


    def __eq__(self, rhs):
        return self._storage == rhs._storage


    def __ne__(self, other):
        return not self.__eq__(other)


    @classmethod
    def load(cls, filepath: str):
        """Deserialize index"""
        with open(filepath, "rb") as fin:
            index_dic = StructStoragePolicy().decode_dic(fin)
            return InvertedIndex(index_dic)

    @classmethod
    def get_words(cls, line):
        """Split line by spaces"""
        return line.split()


    @classmethod
    def split_by_index_and_text(cls, line):
        """split line by frist tab"""
        tab_index = line.find('\t')
        if tab_index == -1:
            return (-1, "")

        return (int(line[:tab_index]), line[tab_index + 1:])


def load_documents(filepath: str):
    """Make doc to id dictionary from text in filepath"""
    documents_to_id_map = {}
    with open(filepath) as document:
        data = document.read()
        for line in data.split("\n"):
            index, text = InvertedIndex.split_by_index_and_text(line)
            if index != -1:
                documents_to_id_map[index] = text

    return documents_to_id_map


def build_inverted_index(documents):
    """build_inverted_index"""
    return InvertedIndex.from_documents(documents)


def callback_build(arguments):
    """Handle `build` CLI command"""
    documents = load_documents(arguments.dataset)
    index = build_inverted_index(documents)
    index.dump(arguments.output)

def process_queries(inverted_index_filepath, query_file):
    """Handle `query` CLI command"""
    inverted_index = InvertedIndex.load(inverted_index_filepath)
    for query in query_file:
        query = query.strip().split()
        document_ids = inverted_index.query(query)
        print(",".join(map(str, document_ids)))

def process_queries_by_lists(inverted_index_filepath, queries):
    """Handle `query` CLI command"""
    inverted_index = InvertedIndex.load(inverted_index_filepath)
    for query in queries:
        document_ids = inverted_index.query(query)
        print(",".join(map(str, document_ids)))

def callback_query(arguments):
    """callback_query"""
    if arguments.query is not None:
        process_queries_by_lists(arguments.inverted_index_filepath, arguments.query)
    else:
        process_queries(arguments.inverted_index_filepath, arguments.query_file)


DEFAULT_DATASET_PATH = "wikipedia_sample.txt"
DEFAULT_INVERTD_INDEX_STORE_PATH = "inverted.index"

def setup_parser(parser):
    """Adjust parsers"""
    subparsers = parser.add_subparsers(help="choose command")

    build_parser = subparsers.add_parser(
        "build",
        help="build inverted index and save in binary format into hard drive",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    build_parser.add_argument(
        "-d", "--dataset",
        default=DEFAULT_DATASET_PATH,
        required=False,
        help="path to dataset to load",
    )
    build_parser.add_argument(
        "-o", "--output",
        default=DEFAULT_INVERTD_INDEX_STORE_PATH,
        required=False,
        help="path to store inverted index in a binary format",
    )
    build_parser.set_defaults(callback=callback_build)

    query_parser = subparsers.add_parser(
        "query",
        help="query inverted index",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    query_parser.add_argument(
        "-i", "--index", default=DEFAULT_INVERTD_INDEX_STORE_PATH,
        dest="inverted_index_filepath",
        help="path to read inverted index",
    )

    query_file_group = query_parser.add_mutually_exclusive_group(required=True)
    query_file_group.add_argument(
        "--query-file-utf8", dest = "query_file",
        type=EncodedFileType("r", encoding="utf-8"),
        default=sys.stdin,
        help="query to run against inverted index",
    )
    query_file_group.add_argument(
        "--query-file-cp1251", dest = "query_file",
        type=EncodedFileType("r", encoding="cp1251"),
        default=TextIOWrapper(sys.stdin.buffer, encoding="cp1251"),
        help="query to run against inverted index",
    )
    query_file_group.add_argument(
        "--query",
        nargs="+",
        action='append',
        metavar='WORD',
        help="query to run against inverted index",
    )
    query_parser.set_defaults(callback=callback_query)

def main():
    """Start point of program"""
    parser = ArgumentParser(
        prog="inverted-index",
        description="tool to build, dump, load and query inverted index",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    setup_parser(parser)
    arguments, _ = parser.parse_known_args()
    arguments.callback(arguments)


if __name__ == "__main__":
    main()
