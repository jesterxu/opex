#!/bin/sh
echo "root dizininde sqlyedek klasoru var mi."
if [ -d '/root/sqlyedek' ]; then
echo "root dizininde sqlyedek klasoru var."
else
echo "root dizininde sqlyedek klasoru yok ama simdi olusturuyorum."
      mkdir /root/sqlyedek
fi
echo
echo "sql yedek almaya basliyor"

ls /var/lib/mysql/ > /root/list
_USERS="$(gawk -F: '{ print $1 }' /root/list)"
for u in $_USERS
do

mysqldump -u root -p$1 ${u} > /root/sqlyedek/${u}.sql
echo "HAZIR > ${u}"
done

zaman=`date +"%d.%m.%Y-%T"`
tar cvzf /root/$zaman-yedek-mysql.tar.gz '/root/sqlyedek'

echo "TUM VERI TABANLARI YEDEKLENDI"
echo "DOSYA YOLU : /root/$zaman-yedek-mysql.tar.gz"