# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PorndistancePipeline(object):
    def process_item(self, item, spider):
    	print("This is the item " + item + " and this is its depth " + item['depth'])
        return item