#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:05:08 2020

@author: mingxiupua
"""

import scrapy
from editorsmarket.items import ImageItem


class EditorsSpider(scrapy.Spider):
    name = "editorsspider"
    page_number = 1
    start_urls = ["https://www.theeditorsmarket.com/category/woman/dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
        next_page = 'https://www.theeditorsmarket.com/category/woman/dresses?page=' + str(EditorsSpider.page_number)  
        if EditorsSpider.page_number <= 15:
           EditorsSpider.page_number += 1
           yield response.follow(next_page, callback = self.parse)    
