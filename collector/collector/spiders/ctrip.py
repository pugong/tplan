# -*- coding: utf-8 -*-
import scrapy


class CtripSpider(scrapy.Spider):
    name = "ctrip"
    allowed_domains = ["ctrip.com"]
    start_urls = (
        'http://www.ctrip.com/',
    )

    def parse(self, response):
        pass
