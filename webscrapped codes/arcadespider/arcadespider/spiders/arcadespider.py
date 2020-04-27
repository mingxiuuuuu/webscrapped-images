#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:50:10 2020

@author: mingxiupua
"""

import scrapy
from arcadespider.items import ImageItem


class ArcadeSpider(scrapy.Spider):
    name = "arcadespider"
    start_urls = ["https://www.aforarcade.com/category/women?clothing%5B27%5D=27&op=Apply"]
                  
    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield ImageItem(image_urls=[img_url])
            