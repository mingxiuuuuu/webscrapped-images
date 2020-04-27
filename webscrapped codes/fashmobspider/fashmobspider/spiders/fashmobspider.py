#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:27:37 2020

@author: mingxiupua
"""

import scrapy
from fashmobspider.items import ImageItem


class FashmobSpider(scrapy.Spider):
    name = "fashmobspider"
    page_number = 1
    start_urls = ["https://www.shopfashmob.com/products?terms[1-4][6]=6&op=Filter"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
        next_page = 'https://www.shopfashmob.com/products?page=' + str(FashmobSpider.page_number) + '&terms[1-4][6]=6&op=Filter'
        if FashmobSpider.page_number <= 22:
            FashmobSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)