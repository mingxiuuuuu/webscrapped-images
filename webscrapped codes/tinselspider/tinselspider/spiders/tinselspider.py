#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:31:48 2020

@author: mingxiupua
"""
import scrapy
from tinselspider.items import ImageItem


class TinselSpider(scrapy.Spider):
    name = "tinselspider"
    page_number = 1
    start_urls = ["https://www.thetinselrack.com/category/apparel/dresses?items_per_page=100"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
        next_page = 'https://www.thetinselrack.com/category/apparel/dresses?page=' + str(TinselSpider.page_number) + '&items_per_page=100' 
        if TinselSpider.page_number <= 2:
            TinselSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
