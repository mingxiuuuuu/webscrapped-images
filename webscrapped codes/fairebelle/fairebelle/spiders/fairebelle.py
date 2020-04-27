#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:44:21 2020

@author: mingxiupua
"""

import scrapy
from fairebelle.items import ImageItem


class FairebelleSpider(scrapy.Spider):
    name = "fairebellespider"
    page_number = 1
    start_urls = ["https://www.fairebelle.com/category/apparels/dresses-"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
      
        next_page = 'https://www.fairebelle.com/category/apparels/dresses-?page=' + str(FairebelleSpider.page_number)  
        if FairebelleSpider.page_number <= 6:
           FairebelleSpider.page_number += 1
           yield response.follow(next_page, callback = self.parse)