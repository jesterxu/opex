#/usr/bin/!
# Cpanel icin ilk satir, plesk icin 2. satiri kullanabilirsiniz.
find  /usr/local/apache/domlogs/* -print | xargs grep -l "$1"
#find /var/log/httpd/* -print | xargs grep -l '$1'