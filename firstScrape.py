# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/10 20:57'

import re

from crawlingWeb import download


def crawl_sitemap(url):
    #download the sitemap file
    sitemap = download(url)
    #extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    #download each link
    for link in links:
        print link
        html = download(link)
        html.save('123.txt')