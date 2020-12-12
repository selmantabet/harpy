PATH=$PATH:/sbin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/home/chaos/joy/bin

ethr_addr_list="08:12:A5:57:92:56
                00:55:DA:54:6D:B7
                C8:2B:96:56:FA:5D
                6C:E8:C6:38:B3:F1
                D8:F1:5B:AF:CF:67
                1C:F2:9A:34:D9:6F
                2C:AA:8E:A4:97:B7
                F6:8C:78:20:78:63
                E0:98:06:CB:61:4D
                00:17:88:B3:4A:D0
                3C:52:82:2D:1C:5B
                10:7B:44:91:A3:00
                16:91:82:BB:03:90"

fileCo=1
while [ $fileCo -le 1 ]
do
    fileName="${fileCo}.pcap"
    echo Processing $fileName
    deviceCo=1
    for addr in $ethr_addr_list
    do
        joy output="json_files/${fileCo}_${deviceCo}.json"\
            bpf="ether host ${addr}"\
            bidir=1\
            dns=1\
            http=1\
            "pcap_files/${fileCo}.pcap"
        ((deviceCo++))
    done
    ((fileCo++))
done

echo Running HARPY on 5-minute interval
python3 harpy.py -t 5
echo Running HARPY on 15-minute interval
python3 harpy.py -t 15
echo Running HARPY on 30-minute interval
python3 harpy.py -t 30

echo Done
