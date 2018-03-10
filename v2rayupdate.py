import sys
import os
os.chdir('/'.join(sys.argv[0].split('\\')[:-1]))
try:
    import requests
except:
    print('pip install requests')
    exit()
#from bs4 import BeautifulSoup
import subprocess
import re
import zipfile
import shutil
rar=r"C:\Program Files\WinRAR\WinRAR.exe"
rmtmp=True
p = subprocess.Popen(['v2ray','-version'], stdout=subprocess.PIPE)
output, err = p.communicate()

now_version=re.findall(r'(v[\d\.]*?)\s',output.decode('utf-8'))[0]
a = requests.get("https://api.github.com/repos/v2ray/v2ray-core/releases/latest")
new_version=a.json()["tag_name"]
if now_version==new_version:
    print('没有core新版本，洗洗睡')
    input()
    exit()
print ("downloading core with requests")
url = "https://github.com/v2ray/v2ray-core/releases/download/"+new_version+"/v2ray-windows-64.zip" 
r = requests.get(url) 
with open("v2ray-windows-64.zip", "wb") as code:
    code.write(r.content)

ok1=subprocess.call(["taskkill","/F","/IM","v2rayN.exe"])
ok2=subprocess.call(["taskkill","/F","/IM","wv2ray.exe"])
ok3=subprocess.call(["taskkill","/F","/IM","v2ray.exe"])
ok4=subprocess.call('"'+rar+'" e -o+ -xconfig.json v2ray-windows-64.zip')
if rmtmp:
    subprocess.call(["del","v2ray-windows-64.zip"])
if ok1==0:
    subprocess.call(["v2rayN.exe"])
print('finished,你可还满意')
input()

