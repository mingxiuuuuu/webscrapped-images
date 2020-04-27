#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:10:40 2020

@author: mingxiupua
"""

import scrapy
from hervelvet.items import ImageItem


class HervelvetSpider(scrapy.Spider):
    name = "hervelvetspider"
    page_number = 1
    start_urls = ["https://www.hervelvetvase.com.sg/category/apparels/dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
      
        next_page = 'https://www.hervelvetvase.com.sg/category/apparels/dresses?page=' + str(HervelvetSpider.page_number)  
        if HervelvetSpider.page_number <= 10:
           HervelvetSpider.page_number += 1
           yield response.follow(next_page, callback = self.parse)