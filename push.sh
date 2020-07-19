#!/bin/bash
if [ $# -eq 0 ];then
    pushmessage=`date +"%F__%T"`
else
    pushmessage="$*"
fi

echo ${pushmessage}

git pull origin master
git add -A
git commit -m "${pushmessage}"
git push origin master
