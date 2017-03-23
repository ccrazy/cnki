import requests
from bs4 import BeautifulSoup
import os
import time
import re
class cnki():
    def getcookie(self):
        DbCatalog = "中国学术期刊网络出版总库"
        db_value = "中国学术期刊网络出版总库"
        joursource = "( 核心期刊=Y or CSSCI期刊=Y)"
        txt_1_value1 = "非物质文化遗产"
        timex = time.strftime('%a %b %d %Y %H:%M:%S')+' GMT+0800'
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
        cookie = requests.get(url,params=parameter).cookies
        start_url = "http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_result_aspx&dbPrefix=CJFQ&dbCatalog=%E4%B8%AD%E5%9B%BD%E5%AD%A6%E6%9C%AF%E6%9C%9F%E5%88%8A%E7%BD%91%E7%BB%9C%E5%87%BA%E7%89%88%E6%80%BB%E5%BA%93&ConfigFile=CJFQ.xml&research=off&t=1489915873138&keyValue=%E9%9D%9E%E7%89%A9%E8%B4%A8%E6%96%87%E5%8C%96%E9%81%97%E4%BA%A7&S=1"
        self.getlist(start_url,cookie)

    def getlist(self,start_url=None,cookie=None):
        start_html = requests.get(start_url,cookies=cookie)
        content = BeautifulSoup(start_html.text,"lxml").find("table",class_="GridTableContent").find_all("tr")
        for i in range(1,len(content)):
            auth = content[i].find_all("td")[1].find("a")
            a = auth['href']
            cite = content[i].find("span",class_="KnowledgeNetcont").find("a").get_text()
            href = "http://kns.cnki.net"+a
            self.getdetail(href,cite,cookie)
        

    # 题名	时间	作者	机构	地区（第一作者位置）	
    # 摘要	关键词	被引频次	下载频次	项目
    def getdetail(self,href,cite,cookie):
        html = requests.get(href,cookies=cookie)
        shtml = BeautifulSoup(html.text,"lxml")
        title = shtml.find("div",class_="wxTitle").find("h2").get_text()#题名
        pubtime = shtml.find("div",class_="sourinfo").find_all("p")[2].find("a").get_text()#时间
        auths = shtml.find("div",class_="author").get_text()
        auths = dr.sub("",auths)#作者
        organ = shtml.find("div",class_="orgn").get_text()
        organ = dr.sub("",organ)#机构
        abstract = shtml.find("span",id="ChDivSummary").get_text()#摘要
        keyword = shtml.find("div",class_="wxBaseinfo").find_all("p")[2].get_text()
        keyword = dr.sub("",keyword)#关键词
        cite = cite#被引频次
        download = shtml.find("span",class_="a").find("b").get_text()#下载频次
        project = shtml.find("div",class_="wxBaseinfo").find_all("p")[1].get_text()
        project = dr.sub("",project)#项目
        journal = shtml.find("div",class_="sourinfo").find("p",class_="title").find("a").get_text()
        term = shtml.find("div",class_="sourinfo").find_all("p")[4].get_text()
        print(journal)

cnki = cnki()
cnki.getcookie()



