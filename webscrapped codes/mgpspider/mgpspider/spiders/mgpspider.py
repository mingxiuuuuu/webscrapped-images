#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:05:39 2020

@author: mingxiupua
"""

import scrapy
from mgpspider.items import ImageItem


class MgpSpider(scrapy.Spider):
    name = "mgpspider"
    page_number = 1
    start_urls = ["https://mgplabel.com/10-dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
      
        next_page = 'https://mgplabel.com/10-dresses?p=' + str(MgpSpider.page_number)  
        if MgpSpider.page_number <= 53:
           MgpSpider.page_number += 1
           yield response.follow(next_page, callback = self.parse)
