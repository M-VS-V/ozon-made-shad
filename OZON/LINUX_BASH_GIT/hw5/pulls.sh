#!/bin/bash

nick_name=$1
final_json='[]'
pages_number=2
for i in $(seq 1 $pages_number)
do
   test_json=`curl -X GET https://api.github.com/repos/datamove/linux-git2/pulls?page=$i\&per_page=100\&state=all`
   final_json=`echo $final_json $test_json | jq -s add`
done
final_json=`echo $final_json | jq ".[] | select(.user.login==\"$1\") | {number, created_at, merged_at, closed_at, asf: .user.\"login\"}"`
final_json=`echo $final_json | jq -n '[inputs]'` # преобразуем лист в массив
PULLS=`echo $final_json | jq 'length'`
EARLIEST=`echo $final_json | jq 'sort_by(.created_at) | .[0].number'`

echo PULLS $PULLS
echo EARLIEST $EARLIEST

MERGED=`echo $final_json | jq 'sort_by(.created_at) | .[0].merged_at'`
if [[ $MERGED =~ "null" ]]; then
    echo MERGED 0
else
    echo MERGED 1
fi
