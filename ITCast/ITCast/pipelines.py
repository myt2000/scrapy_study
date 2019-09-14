# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json



class ItcastPipeline(object):
    def open_spider(self, spider):
        self.file_name = open('itcast2.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item))
        content = '{},\n'.format(content)
        self.file_name.write(content)
        return item

    def close_spider(self, spider):
        self.file_name.close()