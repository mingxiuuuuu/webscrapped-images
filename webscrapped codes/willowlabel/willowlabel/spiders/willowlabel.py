#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:30:17 2020

@author: mingxiupua
"""

import scrapy
from willowlabel.items import ImageItem


class WillowSpider(scrapy.Spider):
    name = "willowspider"
    page_number = 1
    start_urls = ["https://www.thewillowlabel.com/category/dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
        next_page = 'https://www.thewillowlabel.com/category/dresses?page=' + str(WillowSpider.page_number)  
        if WillowSpider.page_number <= 10:
           WillowSpider.page_number += 1
           yield response.follow(next_page, callback = self.parse)

            
            