# -*- coding: utf-8 -*-  
import urllib.request
import re
import csv
import locale
f = open("sample.txt")
n = len(f.readlines())
f.close
dancicnt = 0

for dancicnt in range(0,n):
 def getHtml(url):
     page = urllib.request.urlopen(url)
     html = page.read()
     return html

 def save_as_csv(data, filename):
    with open(filename, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)
        
 f = open("sample.txt")
 danci = f.readlines()[dancicnt]
 print("正在查询："+danci, end = '')
 iPos = 0
	 
 wangzhi="http://dict.youdao.com/app/baidu/search?q="+danci

 html = getHtml(wangzhi)

 def getImg(html):
     global iPos
     csvdata = []
     html = html.decode('utf-8')
     reg = r'<li>(.*?)</li>'
     imgre = re.compile(reg)
     imglist = re.findall(imgre,html)
     if len(imglist) == 0:
        result = "未收录"
        csvdata.append([danci,"未收录"])
        save_as_csv(csvdata,'output.csv')
        return result
     for i in range(0,len(imglist)):
      yuansu = ''.join(imglist[i])
      chazhao = '. '
      nPos = yuansu.find(chazhao)
      if nPos >= 0:
       iPos = i
     result = ''
     csvdata.append([danci])
     for c in range(0,iPos+1):
      if c == 0:
       s=''
      else:
       s='\n'
      csvdata[0].append(''.join(imglist[c]))
      result = result + s + ''.join(imglist[c])
     save_as_csv(csvdata,'output.csv')
     return result

 print(getImg(html).encode('gb18030','ignore').decode(locale.getpreferredencoding(),'ignore'))
 f.close()