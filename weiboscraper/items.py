# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    
class UserInfoItem(scrapy.Item):
    # 用户信息
    nickname = Field()
    avatar = Field()
    location = Field()
    sex = Field()
    birth = Field()
    blog = Field()
    site = Field()
    intro = Field()
    
    email = Field()
    qq = Field()
    msn = Field()
    
    n_follows = Field()
    n_fans = Field()
    
    edu = Field()
    work = Field()
    tags = Field()
