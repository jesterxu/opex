#/usr/bin/!
echo "Baglanti tur ve sayilari..........:"
netstat -ntu | grep :80 | awk '{print $6}' | cut -f1 -d ':' |sort| uniq -c | sort -n;
echo "Fazla baglanti acan ipler..........:"
netstat -ntu | grep :80 | awk '{print $5}' | cut -f1 -d ':' |sort| uniq -c | sort -n | awk '$1 > 10 {print $1,$2}'
echo -n "Sunucudaki toplam baglanti sayisi..........:"
echo `netstat -an|wc -l`
echo -n "Sistem Load Durumu..........:"
echo `uptime | awk -F "load average: " '{ print $2 }' | cut -d, -f1`