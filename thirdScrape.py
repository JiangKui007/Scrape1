# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/10 21:45'
import re
import urlparse

from crawlingWeb import download

def get_links(html):
    """
    返回一个从html中关于链接的列表
    :param html:
    :return:
    """
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    print webpage_regex.findall(html)
    return webpage_regex.findall(html)


def link_crawler(seed_url,link_regex):
    """
    从相关正则表达式中下载网页
    :param seed_url:
    :param link_regex:
    :return:
    """
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                crawl_queue.append(link)

link_crawler('http://example.webscraping.com','/(index|view)')
