#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:51:01 2020

@author: mingxiupua
"""
import scrapy
from closetspider.items import ImageItem


class ClosetSpider(scrapy.Spider):
    name = "closetspider"
    page_number = 1
    start_urls = ["https://www.theclosetlover.com/category/clothing/dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
        next_page = 'https://www.theclosetlover.com/category/clothing/dresses?page=' + str(ClosetSpider.page_number) 
        if ClosetSpider.page_number <= 13:
            ClosetSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)