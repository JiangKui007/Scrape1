# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/10 21:20'
import urllib2
import itertools
"""
遍历ID爬取网页数据
"""

def download(url, user_agent="wswp", num_retries = 2):
    print 'Downloading:', url
    headers = {'User-agent':user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500<=e.code<600:
            #  重试5XX Http 错误
                return download(url,user_agent, num_retries-1)
    return html


max_errors = 5
num_errors = 0
for page in itertools.count(2):
    url = 'http://example.webscraping.com/places/default/view/-%d' % page
    html1 = download(url)
    if html1 is None:
        num_errors += 1
        if num_errors ==max_errors:
            break
    else:
        num_errors = 0
