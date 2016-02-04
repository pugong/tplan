# -*- coding: utf-8 -*-
import scrapy


class AmapSpider(scrapy.Spider):
    name = "amap"
    allowed_domains = ["ditu.amap.com"]
    start_urls = (
        'http://ditu.amap.com/',
    )

    def parse(self, response):
        pass
