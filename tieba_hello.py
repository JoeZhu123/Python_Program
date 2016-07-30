#._*_ coding:utf-8 _*_
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
 
#百度贴吧爬虫类
class BDTB:
 
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
 
    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None
    def getTitle(self):
    	page = self.getPage(1)
    	pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
    	result = re.search(pattern,page)
    	if result:
		print result.group(1)  #测试输出
		return result.group(1).strip()
    	else:
		return None
    def getContent(self,page):
    	pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
    	items = re.findall(pattern,page)
    	for item in items:
        	print item
 
baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.getPage(1)


