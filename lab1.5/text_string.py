import glob
import os

set_of_ip = set()

for f_host in glob.glob("*.log"):
    print(f_host)
    with open(f_host) as f:
        for f_line in f:
            if f_line.find("10.31") != -1:
                print (f_line)
                set_of_ip.add(f_line.replace("10.31","_100.31"))

        for i in set_of_ip:
            print(i)