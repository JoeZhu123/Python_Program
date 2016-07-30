#-*-coding:utf-8-*-
import urllib
import urllib2
import cookielib

'''
#声明一个CookieJar对象实例来保存cookie
cookie=cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener=urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response=opener.open('http://www.baidu.com')
for item in cookie:
	print 'Name='+item.name
	print 'Value='+item.value

#保存cookie到文件
#设置cookie的文件，同级目录下的cookie.txt
filename='cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie,之后写入文件
cookie=cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener=urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response=opener.open('http://www.baidu.com')
#保存cookie到文件
cookie.save(ignore_discard=True,ignore_expires=True)
'''

filename='cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie=cookielib.MozillaCookieJar(filename)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata=urllib.urlencode({
	'qq':'1668045443',
	'pwd':'tkfoszly1020'
	})
#登录QQ邮箱
QQ_EmailUrl='https://mail.qq.com/cgi-bin/loginpage'
#模拟登录，并把cookie保存到变量
result=opener.open(QQ_EmailUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True,ignore_expires=True)
#利用cookie请求访问QQ空间
QQ_ZoneUrl='http://qzone.qq.com/'
#
result=opener.open(QQ_ZoneUrl)
print result.read()

