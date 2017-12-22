# -*- coding: utf-8 -*-  
import urllib.request
import re
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

 f = open("sample.txt")
 w = open("output.txt","a+")
 danci = f.readlines()[dancicnt]
 print("正在查询："+danci, end = '')
 w.write(danci)
 iPos = 0
	 
 wangzhi="http://dict.youdao.com/app/baidu/search?q="+danci

 html = getHtml(wangzhi)

 def getImg(html):
     global iPos
     html = html.decode('utf-8','ignore')
     reg = r'<li>(.*?)</li>'
     imgre = re.compile(reg)
     imglist = re.findall(imgre,html)
     if len(imglist) == 0:
        result = "未收录"
        return result
     for i in range(0,len(imglist)):
      yuansu = ''.join(imglist[i])
      chazhao = '. '
      nPos = yuansu.find(chazhao)
      if nPos >= 0:
       iPos = i
     result = ''
     for c in range(0,iPos+1):
      if c == 0:
       s=''
      else:
       s='\n'
      result = result + s + ''.join(imglist[c])
     return result
 print(getImg(html).encode('gb18030','ignore').decode(locale.getpreferredencoding(),'ignore'))
 w.write(getImg(html).encode('gb18030','ignore').decode(locale.getpreferredencoding(),'ignore') + '\n' + '\n')
 f.close()
 w.close()
