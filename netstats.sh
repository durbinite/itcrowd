#!/bin/sh
# // Netstat of IP's to check for DDos
timestamp() {
  date 
}
Uniqu=$(netstat -nat | awk '{ print $5}' | cut -d: -f1 | sed -e '/^$/d' | uniq | wc -l)
Repeat_offenders=$(netstat -nat | grep ESTABLISHED | awk '{ print $5}' | cut -d: -f1 | sort -u)
     echo -e "$(timestamp) # of current connections ${Uniqu}\n${Repeat_offenders}"  >> DDos_Check.txt
