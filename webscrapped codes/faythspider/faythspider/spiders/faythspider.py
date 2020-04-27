#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:20:11 2020

@author: mingxiupua
"""
import scrapy
from faythspider.items import ImageItem


class FaythSpider(scrapy.Spider):
    name = "faythspider"
    page_number = 2
    start_urls = ["https://fayth.com/clothing/dresses/"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
        next_page = 'https://fayth.com/clothing/dresses/?p=' + str(FaythSpider.page_number) 
        if FaythSpider.page_number <= 12:
            FaythSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
