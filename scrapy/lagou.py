from  urllib.request import urlopen
from bs4 import BeautifulSoup
import request
import datetime
import random
import re


# random.seed(datetime.datetime.now())
# companyUrl
def get_company_links(page_links):
    """得到要爬的网页中每一页的公司链接
    """
    a = []
    for l in page_links:
        html = urlopen(l)
        bsOjc = BeautifulSoup(html, 'html.parser')
        for link in bsOjc.findAll(class_="position_link"):
            a.append("http://" + link.attrs['href'][2:])
            # print (link.attrs['href'][2:])
    search_key_words(a)
    return a

    # yield link


def search_key_words(links):
    """解析并提取关键每个公司的招聘信息
    """
    response = []
    for i, l in enumerate(links):
        html = urlopen(l).read()
        bsOjc = BeautifulSoup(html, 'html.parser')
        company_name = bsOjc.find(id="job_detail").div.get_text()
        job_name = bsOjc.find(id="job_detail").h1['title']
        info = []
        for information in bsOjc.findAll(class_="c_feature"):
            info.append(information.get_text().replace('\n','').replace('  ',''))
        # info = filter(lambda x: x.g, list())
        print (info)
        # print(i, company_name, job_name)
        #'<ul class="c_feature">.*?<li><span>.*?</span>(.*?)</li>'
        resp = {
            'index': i,
            'company': company_name,
            'job_name': job_name,
            'info': info[0][3:]+info[1][-3:]
        }
        response.append(resp)
    print (response)


def _get_page_links():
    """得到要爬的网页"""
    for i in range(1, 14):
        link = 'http://www.lagou.com/zhaopin/Python/' + str(i) + '/'
        yield link


if __name__ == '__main__':
    get_company_links(_get_page_links())
