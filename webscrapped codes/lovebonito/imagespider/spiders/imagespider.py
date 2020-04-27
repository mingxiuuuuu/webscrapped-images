#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:44:25 2020

@author: mingxiupua
"""
import scrapy
from imagespider.items import ImageItem


class ImageSpider(scrapy.Spider):
    name = "imagespider"
    page_number = 2
    start_urls = ["https://www.lovebonito.com/sg/clothing/category/dresses"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            
        next_page = 'https://www.lovebonito.com/sg/clothing/category/dresses?p=' + str(ImageSpider.page_number)
        if ImageSpider.page_number <= 22:
            ImageSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
            