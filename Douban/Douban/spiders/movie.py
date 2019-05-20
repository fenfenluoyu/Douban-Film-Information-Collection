# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = (    # 元组
        url + str(offset),
    )

    def parse(self, response):
        movies = response.xpath('//*[@class = "grid_view"]/li')
        for each in movies:
            item = DoubanItem()
            item['title'] = each.xpath('.//span[@class = "title"][1]/text()').extract()[0]
            message = each.xpath('.//div[@class = "bd"]/p[1]/text()[2]').extract()[0].split(" ")
            item['message'] = "".join(message)

            item['score'] = each.xpath('.//span[@class = "rating_num"]/text()').extract()[0]
            introduction = each.xpath('.//span[@class = "inq"]/text()').extract()
            if len(introduction) != 0:
                item['introduction'] = introduction[0]
            detail_url = each.xpath('div[1]/div[1]/a/@href').extract()[0]
            yield scrapy.Request(detail_url, meta = {'item' : item}, callback = self.parse_detail)

        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url+str(self.offset), callback = self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        item['detail'] = response.xpath('//span[@property = "v:summary"]/text()').extract()[0]
        yield item
