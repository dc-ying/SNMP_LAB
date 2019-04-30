# coding=utf-8
import re
import os,sys
import time
import platform




def snmpWalk(host, oid):
    result = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read()
    return result


#snmpwalk -v 2c -c public  127.0.0.1 .1.3.6.1.4.1.2021.5000
#处理回显结果system
def getSystem(host):
    system = snmpWalk(host, '.1.3.6.1.4.1.2021.5000.3.1.2.10.103.101.116.119.105.110.105.110.102.111')
    if system.find('Hex-STRING:') > 0: 
        system = "".join(system.split('Hex-STRING:')[1:])
        system = "".join(system.split('\n'))
        system = "".join(system.split(' '))
        system = system.decode("hex")
    
    else:
        system = "".join(system.split('STRING: \"')[1:])
        system = system[0:len(system)-2]
    return system

def main():
    ip=input("Server IP:")
    hosts = [str(ip)]
    """
    for host in hosts:
        print('=' * 10 + host + '=' * 10)
        print("测试信息")
        system = getSystem(host)
        print(system)
        my_file = '.tmp/file'
        print ("信息存储到文件: %s"%(my_file)).decode('utf-8').encode('gbk')
        if os.path.exists(my_file):
            os.remove(my_file)
        f = open(my_file, 'a+')
        f.write(str(system))
        f.close()
    """
    while(True):
        oid=input("Please enter an OID:")
        if(oid==''):
            break
        else:
            for host in hosts:
                print("...")
                print("host:%s",host)
                print("oid:%s",oid)
                print("...")
                return_str=snmpWalk(host,oid)
                print(return_str)
                print("...")

if __name__ == '__main__':
    main()