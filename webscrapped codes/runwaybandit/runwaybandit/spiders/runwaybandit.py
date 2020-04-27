#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:51:14 2020

@author: mingxiupua
"""
import scrapy
from runwaybandit.items import ImageItem


class RunwaybanditSpider(scrapy.Spider):
    name = "runwaybanditspider"
    page_number = 1
    start_urls = ["https://www.runwaybandits.com/category/clothes/dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
      
        next_page = 'https://www.runwaybandits.com/category/clothes/dresses?page=' + str(RunwaybanditSpider.page_number)  
        if RunwaybanditSpider.page_number <= 30:
           RunwaybanditSpider.page_number += 1
           yield response.follow(next_page, callback = self.parse)
