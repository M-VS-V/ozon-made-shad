#!/bin/bash
touch /tmp/Fr0do.json
curl -s https://api.github.com/repos/datamove/linux-git2/pulls?state=all\&page=1\&per_page=100 | jq '.[]' > /tmp/Fr0do.json
curl -s https://api.github.com/repos/datamove/linux-git2/pulls?state=all\&page=2\&per_page=100 | jq '.[]' >> /tmp/Fr0do.json

touch /tmp/ans.json
cat /tmp/Fr0do.json | jq -n '[inputs]' | jq "map(select(.user.login == \"${1}\"))" > /tmp/ans.json

T1=`cat /tmp/ans.json | jq length`
echo "PULLS $T1"

T2=`cat /tmp/ans.json | jq "min_by(.created_at) | .number"`
echo "EARLIEST $T2"

T3=`cat /tmp/ans.json | jq "min_by(.created_at) | .merged_at != null"`
if [ "$T3" = "false" ]; then 
    echo "MERGED 0"
else
    echo "MERGED 1"
fi
