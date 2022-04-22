import urllib.request
import urllib.parse
from lxml import etree


"""
爬取世界国家与地区一览表
"""

url = 'https://baike.baidu.com/item/%E5%9B%BD%E5%AE%B6%E5%92%8C%E5%9C%B0%E5%8C%BA/52039732?fromtitle=%E4%B8%96%E7%95%8C%E5%9B%BD%E5%AE%B6%E4%B8%8E%E5%9C%B0%E5%8C%BA%E4%B8%80%E8%A7%88%E8%A1%A8&fromid=850195#27'
# 请求头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
# 利用请求地址和请求头部构造请求对象
req = urllib.request.Request(url=url, headers=headers, method='GET')
# 发送请求，获得响应
response = urllib.request.urlopen(req)
# 读取响应，获得文本
text = response.read().decode('utf-8')
# 构造 _Element 对象
html = etree.HTML(text)


# tables = html.xpath('.//table/tbody/tr/td/a')
tables = html.xpath('.//table')
# guojia = [0,25]
# diqu = [26]
# haiwaisheng = [27]
# haiwaishudi = [28]
# zizhigongheguo = [29]
dic = {}
for table in tables[28:29]:

    trs = table.xpath('.//tr')
    for tr in trs:
        if tr.xpath('./td'):
            try:
                t = tr.xpath('./td')[0]
                # print(t.xpath('./div/a/text()'))
                key = t.xpath('./div/a/text()')[0]
                value = t.xpath('./div/a')[0].xpath('@href')[0]
                dic[key] =  'https://baike.baidu.com' + value
            except:
                t = tr.xpath('./td')[1]
                key = t.xpath('./div/a/text()')[0]
                value = t.xpath('./div/a')[0].xpath('@href')[0]
                dic[key] = 'https://baike.baidu.com' + value