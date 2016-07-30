import urllib
import urllib2

#POST
'''
values = {}
values['username'] = "1668045443@qq.com"
values['password'] = "tkfoszly1020"
'''
'''
values = {"username":"1668045443@qq.com","password":"tkfoszly1020"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
'''
#GET
values = {}
values['username'] = "joezhu"
values['password'] = "xxxxxxxxxxxxxx"#密码隐藏
data = urllib.urlencode(values)
url = "http://www.cc98.org"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)

print response.read()

