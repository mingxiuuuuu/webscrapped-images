#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:43:58 2020

@author: mingxiupua
"""
import scrapy
from lovebravery.items import ImageItem


class LovebraverySpider(scrapy.Spider):
    name = "lovebravery"
    page_number = 1
    start_urls = ["https://www.loveandbravery.com/category/clothing/dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
      
        next_page = 'https://www.loveandbravery.com/category/clothing/dresses?page=' + str(LovebraverySpider.page_number)  
        if LovebraverySpider.page_number <= 26:
           LovebraverySpider.page_number += 1
           yield response.follow(next_page, callback = self.parse)
           
