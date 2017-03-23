import requests
from bs4 import BeautifulSoup
import os
import time
import re
import random
import pymysql 

database=pymysql.connect(host='localhost', port=3306, user='root', passwd='ccnu',db='cnki', charset='utf8',
 cursorclass=pymysql.cursors.DictCursor)
user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
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
for j in range(61,199):
    UA = random.choice(user_agent_list) ##从self.user_agent_list中随机取出一个字符串（聪明的小哥儿一定发现了这是完整的User-Agent中：后面的一半段）
    headers = {'User-Agent': UA}
    start_url = "page"+str(j)+".html"
    # print(cookie["LID"])
    # exit
    # p = {
    #     "q":16,
    #     "c":51,
    #     "l":50,
    #     "dbprefix":"CJFQ",
    #     "__":time.strftime('%a %b %d %Y %H:%M:%S')+' GMT+0800 (CST)'
    #     }
    # start_html = requests.get(start_url)
    # print(start_html.url)
    # f = open("data.html","w")
    # f.write(start_html.text)
    # exit
    content = BeautifulSoup(open(start_url),"lxml").find("table",class_="GridTableContent").find_all("tr")
    p = 0
    for i in range(1,len(content)-1):
        UA = random.choice(user_agent_list) ##从self.user_agent_list中随机取出一个字符串
        headers = {'User-Agent': UA}
        auth = content[i].find_all("td")[1].find("a")
        a = auth['href']
        dbname = a[a.index("dbname"):a.index("&filename")]
        filename = a[a.index("&filename"):a.index("&urlid")]
        uid = ""
        try:
            cite = content[i].find_all("td")[5].find("span",class_="KnowledgeNetcont").find("a",class_="KnowledgeNetLink").get_text()
        except:
            cite = "000"
        try:
            download = content[i].find_all("td")[6].find("span",class_="downloadCount").find("a").get_text()
        except:
            download = "000"
        href = "http://kns.cnki.net/KCMS/detail/detail.aspx?"+dbname+filename+uid
        html = requests.get(href,headers=headers,cookies=cookie)
        html.encoding = 'utf-8'
        shtml = BeautifulSoup(html.text,"lxml")
        try:
            title = shtml.find("div",class_="wxTitle").find("h2",class_="title").get_text()#题名
            title = title.replace('"',r'\"')
        except:
            title = "000"
        try:
            pubtime = content[i].find_all("td")[4].find("a").get_text()#时间
        except:
            pubtime = "000"
        try:
            auths = content[i].find("td",class_="author_flag").get_text()
            auths = dr.sub("",auths)#作者
        except:
            auths = "000"
        try:
            organs = shtml.find("div",class_="orgn").find_all("span")
            organ = ""
            for a in organs:
                organ = organ+a.find("a").get_text()+";"
        except:
            organ = "000"
        try:
            abstract = shtml.find("span",id="ChDivSummary").get_text()#摘要
            abstract = abstract.replace('"',r'\"')
        except:
            abstract = "000"
        try:
            keyword = shtml.find("div",class_="wxBaseinfo").find_all("p")[2].get_text()
            keyword = dr.sub("",keyword)#关键词
        except:
            keyword = "000"
        try:
            project = shtml.find("div",class_="wxBaseinfo").find_all("p")[1].get_text()
            project = dr.sub("",project)#项目
        except:
            project = "000"
        try:
            journal = shtml.find("div",class_="sourinfo").find("p",class_="title").find("a").get_text()
        except:
            journal = "000"
        try:
            term = shtml.find("div",class_="sourinfo").find_all("p")[4].get_text()
        except:
            term = "000"
        # print(auths)
        cursor = database.cursor()
        sql = "insert into journal (title,pubtime,auths,organ,abstract,keyword,cite,download,project) VALUES ("'"%s"'","'"%s"'","'"%s"'","'"%s"'","'"%s"'","'"%s"'","'"%s"'","'"%s"'","'"%s"'")" % (title,pubtime,auths,organ,abstract,keyword,cite,download,project)
        try:
            i = cursor.execute(sql)
            database.commit()
            print("success"+"\n")
            p =p+1
            print(p)
        except :
            f = open("error.txt","a")
            f.write(str(j)+"\t"+title+"\t"+sql+"\n")
            # f.write(sql)
            # database.close()
    # 题名	时间	作者	机构	地区（第一作者位置）	
    # 摘要	关键词	被引频次	下载频次	项目




