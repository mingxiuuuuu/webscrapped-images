#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:56:30 2020

@author: mingxiupua
"""
import scrapy
from stagewalk.items import ImageItem


class StageSpider(scrapy.Spider):
    name = "stagewalkspider"
    page_number = 1
    start_urls = ["https://www.thestagewalk.com/category/clothing/dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
      
        next_page = 'https://www.thestagewalk.com/category/clothing/dresses?page=' + str(StageSpider.page_number)  
        if StageSpider.page_number <= 20:
           StageSpider.page_number += 1
           yield response.follow(next_page, callback = self.parse)

