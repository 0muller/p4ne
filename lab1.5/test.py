import glob
import os


#s = f_host1.read()
#print (s)
set_of_ip = set()

for f_host in glob.glob("*.log"):
    print(f_host)
    with open(f_host) as f:
        for f_line in f:
            if f_line.find("ip address") == 1:
                print (f_line)
                set_of_ip.add(f_line.replace("ip address","ip_address"))
          #set_of_ip.add(f_line.replace("10","192").strip())

          #set_of_ip.add(f_line.replace("192", "122").strip())

        for i in set_of_ip:
            print(i)
