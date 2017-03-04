#!/bin/sh
# // URL Check with Curl
while read line ; do
     statuscode=$(curl -siL $line | awk '/^HTTP/{print $2}')
     echo -e "${line}\t${statuscode}"  >> URL_Check.txt
 done < list.txt
