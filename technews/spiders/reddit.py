# -*- coding: utf-8 -*-
"""
@author: hasnayeen
"""

import scrapy
import time

class RedditSpider(scrapy.Spider):
    name = "reddit"
    allowed_domains = ["reddit.com"]
    start_urls = (
        'http://www.reddit.com/r/programming',
    )

    def parse(self, response):
        links = response.xpath('//p[@class="title"]/a/@href').extract()
        titles = response.xpath('//p[@class="title"]/a/text()').extract()
        filename = time.strftime("%d-%m-%Y") + ".txt"
        f = open(filename, 'a+')
        for x in range(0, links.__len__()):
            news_title = titles[x].encode('utf-8')
            news_link = links[x].encode('utf-8')
            o = open(filename, 'rb')
            line_list = o.readlines()
            if line_list.__len__() != 0:
                for line in line_list:
                    if line.split("\t")[0] == news_title:
                        new = False
                        break
                    else:
                        new = True
                
                if new != False:
                    f.write(news_title + "\t" + news_link + "\t" + "false" + "\n")
                    
            else:
                f.write(news_title + "\t" + news_link + "\t" + "false" + "\n")
            
            o.close()
            
        f.close()