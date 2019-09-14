# -*- coding: utf-8 -*-
import scrapy
from ITCast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = 'itcast'
    # 允许爬虫爬取的域名范围
    allowed_domains = ['itcast.cn']
    # 爬虫启动时， 发送的第一批url地址列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 获取所有老师的节点
        node_list = response.xpath('//div[@class="li_txt"]')
        item_list = []
        # 迭代节点列表， 获取每个老师信息
        for node in node_list:
            # 每个item表示一个老师信息
            item = ItcastItem()
            item['name'] = node.xpath('./h3/text()').extract_first()
            item['title'] = node.xpath('./h4/text()').extract_first()
            item['info'] = node.xpath('./p/text()').extract_first()
            yield item


    # 1. 如果需要保存数据到json, csv, xml文件格式， 可以先将所有item数据放入列表，再return这个列表
    # 执行爬虫的时候，可以通过 -o 输出到指定的文件里， scrapy会识别文件的后缀，并存储到指定文件格式
'''
    # parse()默认解析start_urls里发送的请求对应的响应
    def parse(self, response):
        node_list = response.xpath('//div[@class="li_txt"]')
        item_list = []
        for node in node_list:
            item = ItcastItem()
            item['name'] = node.xpath('./h3/text()').extract_first()
            item['title'] = node.xpath('./h4/text()').extract_first()
            item['info'] = node.xpath('./p/text()').extract_first()
            item_list.append(item)
        return item_list
'''