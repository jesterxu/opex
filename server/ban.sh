#/usr/bin/!
iptables -A INPUT -s $1 -j DROP
echo "$1 numarali ipi banladim."