#!/bin/sh
# Bu scripti kimin yazdigini bilmiyorum ama yazan arkadasa tesekkur ederim.


# Saldiri varmi ?
SYNCOUNT=`netstat -n | grep SYN | wc -l`

if [ $SYNCOUNT -gt 20 ] ; then

echo "$SYNCOUNT SYN Bulundu! Banlama basliyor lutfen bekleyin."

# Sunucu iplerini beyaz liste alalim.
ip addr show|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|cut -d: -f9|cut -d/ -f1|while read ipler; do touch /tmp/$ipler.tk; done

# Bloklanicak Paket Sayisi
#Default deger BPAKET=40
BPAKET=40
# Incelenecek Paket Sayisi
# Default deger SPAKET=5000
SPAKET=5000
# Inceleyelim.
tcpdump -n -q -c $SPAKET 'tcp[tcpflags] & tcp-syn != 0 and dst port 80'| awk '{print $3}'|awk -F. -v n=. '{print $1 n $2 n $3 n $4}'|sort|uniq -c|sort -nr|awk '$1 > $PAKET'|awk '{print $2}'|while read ipler;
do if [ ! -f /tmp/$ipler.tk ]; then
touch /tmp/$ipler.tk && iptables -A INPUT -s $ipler -j DROP && echo $ipler blokladim;
fi
done

# Cikalim.
else
echo "$SYNCOUNT SYN Bulundu! Saldiri tespit edilmedi..."
fi
exit 0
