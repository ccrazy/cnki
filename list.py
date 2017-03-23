import requests
from bs4 import BeautifulSoup
import os
import time
import re
import random
user_agent_list = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; Sleipnir/2.9.8)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) RockMelt/0.9.64.361 Chrome/13.0.782.218 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/10.04 Chromium/15.0.874.106 Chrome/15.0.874.106 Safari/535.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.106 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618; Lunascape 4.7.3)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Lunascape 5.0 alpha2)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 5.0 alpha2)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; Tablet PC 2.0; Lunascape 5.0 alpha2)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAGW; .NET4.0C; Lunascape 6.5.8.24780)",
]
DbCatalog = "中国学术期刊网络出版总库"
db_value = "中国学术期刊网络出版总库"
joursource = "( 核心期刊=Y or CSSCI期刊=Y)"
txt_1_value1 = "非物质文化遗产"
timex = time.strftime('%a %b %d %Y %H:%M:%S')+' GMT+0800 (CST)'
parameter = {
    "action":"",
    "NaviCode":"*",
    "ua":"1.21",
    "PageName":"ASP.brief_result_aspx",
    "DbPrefix":"CJFQ",
    "DbCatalog":DbCatalog,
    "ConfigFile":"CJFQ.xml",
    "db_opt":"CJFQ",
    "db_value":db_value,
    "@joursource":joursource,
    "year_to":2016,
    "year_type":"echar",
    "txt_1_sel":"SU",
    "txt_1_value1":txt_1_value1,
    "txt_1_relation":"#CNKI_AND",
    "txt_1_special1":"=",
    "his":0,
    "__":timex
}
dr = re.compile(r'<[^>]+>',re.S)
url = "http://kns.cnki.net/kns/request/SearchHandler.ashx?"
# start_url = "http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_result_aspx&dbPrefix=CJFQ&dbCatalog=%E4%B8%AD%E5%9B%BD%E5%AD%A6%E6%9C%AF%E6%9C%9F%E5%88%8A%E7%BD%91%E7%BB%9C%E5%87%BA%E7%89%88%E6%80%BB%E5%BA%93&ConfigFile=CJFQ.xml&research=off&t=1489915873138&keyValue=%E9%9D%9E%E7%89%A9%E8%B4%A8%E6%96%87%E5%8C%96%E9%81%97%E4%BA%A7&S=1"
# cookies = dict(PHPSESSID='2lt1vi03b615qojvp6h09n6tu6')
UA = random.choice(user_agent_list) ##从self.user_agent_list中随机取出一个字符串
headers = {'User-Agent': UA}
cookie = requests.get(url,params=parameter,headers=headers).cookies
# print(cookie)
# exit
for j in range(111,199):
    UA = random.choice(user_agent_list) ##从self.user_agent_list中随机取出一个字符串（聪明的小哥儿一定发现了这是完整的User-Agent中：后面的一半段）
    headers = {'User-Agent': UA}
    start_url = "http://kns.cnki.net/kns/brief/brief.aspx?curpage="+str(j)+"&RecordsPerPage=50&QueryID=16&ID=&turnpage=1&tpagemode=L&dbPrefix=CJFQ&Fields=&DisplayMode=listmode&PageName=ASP.brief_result_aspx#J_ORDER&"
    start_html = requests.get(start_url,headers=headers,cookies=cookie)
    # print(start_html.url)
    f = open("page"+str(j)+".html","w")
    f.write(start_html.text)
    f.close 
    print("page"+str(j)+".html")
    # if int(j/10)==j/10:
    #     time.sleep(120)
    time.sleep(10)  




