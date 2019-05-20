# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 信息
    message = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 简介
    introduction = scrapy.Field()
    # 详情页面
    detail = scrapy.Field()