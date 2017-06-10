# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/10 17:04'

import urllib2


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





