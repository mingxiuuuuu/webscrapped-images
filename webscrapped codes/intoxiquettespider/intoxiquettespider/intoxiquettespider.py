#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:40:06 2020

@author: mingxiupua
"""

import scrapy
from intoxiquettespider.items import ImageItem


class IntoxiquetteSpider(scrapy.Spider):
    name = "intoxiquettespider"
    page_number = 1
    start_urls = ["https://www.intoxiquette.com/category/dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
        next_page = 'https://www.intoxiquette.com/category/dresses?page=' + str(IntoxiquetteSpider.page_number) 
        if IntoxiquetteSpider.page_number <= 9:
            IntoxiquetteSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
