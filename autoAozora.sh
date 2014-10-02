#!/bin/sh

#export LANG=ja_JP.UTF-8
while :
do
	twitText=`/usr/bin/python /home/pi/bin/importCsv.py`
	if [ "$?" -eq 0 ]
	then
		break
	fi
done

echo ${twitText}
/usr/local/bin/tw ${twitText} --yes

