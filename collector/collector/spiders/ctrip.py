# -*- coding: utf-8 -*-
import scrapy


class CtripSpider(scrapy.Spider):
    name = "ctrip"
    allowed_domains = ["ctrip.com"]
    start_urls = (
        #'http://www.ctrip.com/',
        'http://m.ctrip.com/restapi/soa2/10159/json/getsightinfolistforapp670?_fxpcqlniredt=09031170310176890207',
    )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.path('//result/ul/li')
        #sites = hxs.path('//ul/li')
        items = []
        for site in sites:
            item = sightinfo()
            item['title'] = site.path('a/text()').extract()
            item['link'] = site.path('a/@href').extract()
            item['desc'] = site.path('text()').extract()
            items.append(item)
        return items