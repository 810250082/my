import subprocess
import os

# pid = os.getpid()
# subp = subprocess.call(["nslookup" , "www.baidu.com"])
# # print "exit code:" , subp
#
# print subp

subp = subprocess.Popen(['nslookup'] , stdin=subprocess.PIPE , stdout=subprocess.PIPE , stderr=subprocess.PIPE)
output , error = subp.communicate(b"set q=mx\npython.org\nexit\n")
print(output.decode('utf-8'))
print('exit code:' , subp.returncode)