# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 1.爬虫名为必须参数
    name = 'baidu'
    # 2. 允许爬虫爬取的域名范围
    allowed_domains = ['baidu.com']
    # 3. 爬虫启动爬取的第一批url地址, start_urls里的请求不做去重，且不受allowed_domains的限制
    start_urls = ['http://baidu.com/', 'http://www.qq.com', 'http://www.sina.com.cn']

    # 4. 默认解析从start_urls的请求返回的响应
    def parse(self, response):
        # response.xpath()
        print("-------"*20)
        print(len(response.body))
        # 构建请求，请求发送后，由callback指定的回调函数来解析响应
        yield scrapy.Request(url="https://www.qq.com", callback=self.parse)