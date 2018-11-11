#-*-coding:utf-8-*-
import scrapy

class BookSpider(scrapy.Spider):
    # 爬虫的标识
    name = "books"

    start_urls = ["https://www.hao123.com"]

    def parse(self,response):
        for book in response.css("article.product_pod"):
            name = book.xpath("./h3/a@titile").extract_first()

            price = book.css('p.price_color::text').extract_first()

            yield {
                'name': name,
                'price': price,
            }

        next_url = response.scc("ul.pager li.next a::attr(href)").extract_first()

        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)