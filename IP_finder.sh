## Add list of URL's to your mylist.txt and run this script. Results will be listed in IP_list.txt##
#!/bin/bash
while read -r domain
do
    dig +short $domain
done < mylist | sort -u | awk '{printf "%s ", $0} END {printf "\n"}' > IP_list.txt
