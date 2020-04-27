#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:09:51 2020

@author: mingxiupua
"""

import scrapy
from fleurspider.items import ImageItem


class FleurSpider(scrapy.Spider):
    name = "fleurspider"
    page_number = 1
    start_urls = ["https://www.thefleurlabel.com/category/dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
        next_page = 'https://www.thefleurlabel.com/category/dresses?page=' + str(FleurSpider.page_number) 
        if FleurSpider.page_number <= 4:
            FleurSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)