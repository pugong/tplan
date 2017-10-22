# -*- coding = Field()# : utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CollectorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class districtItem(Item):
    districtId = Field()# : 2
    districtName = Field()# : "上海"
    districtPinYin = Field()# : "shanghai"
    cood = Coordinate()
    #lat = Field()# : 31.2304592132568
    #lng = Field()# : 121.473701477051



class sightinfo(Item): 
    cood = Coordinate()
    bCoord = Coordinate()# : {Lng = Field()# : 121.50541, Lat = Field()# : 31.188206}
    commentCount = Field()# : 386
    commentScore = Field()# : 4.4
    coverImage = Field()# : "http://dimg05.c-ctrip.com/images/fd/tg/g2/M02/8A/98/Cghzf1Ww1TmAShLPAAnLLDJ9xuE210_C_210_140.jpg"
    coverImageUrl100x100 = Field()# : "http://dimg05.c-ctrip.com/images/fd/tg/g2/M02/8A/98/Cghzf1Ww1TmAShLPAAnLLDJ9xuE210_C_100_100.jpg"
    currency = Field()# : ""
    distance = Field()# : 0
    districtId = Field()# : 2
    districtName = Field()# : "上海"
    gDCoord = Coordinate()# : {Lng = Field()# : 121.498832598399, Lat = Field()# : 31.1825749272138}
    hasMorePrice = Field()# : false
    hasPlay = Field()# : false
    hasSightHotel = Field()# : false
    hasTicketSale = Field()# : false
    inChina = Field()# : true
    #lat = Field()# : 31.184599
    level = Field()# : ""
    #lng = Field()# : 121.494385
    percent = Field()# : 0
    price = Field()# : 0
    priceType = Field()# : 3
    rank = Field()# : 10
    recommendDesc = Field()# : "原上海世博会中国国家馆，观赏镇馆之宝——多媒体版《清明上河图》。"
    recommendType = Field()# : 1
    rmbPrice = Field()# : 0
    sightEName = Field()# : ""
    sightId = Field()# : 18317
    sightName = Field()# : "中华艺术宫"
    template = Field()# : 1


Class Coordinate(item):
    lng = Field()# : 121.498832598399
    lat = Field()# : 31.1825749272138