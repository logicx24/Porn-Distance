from __future__ import absolute_import
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from pornDistance.items import FoundLink
import re

class pornSpider(CrawlSpider):
	name = 'porn_finder'
	
	def __init__(self, base_url, *args, **kwargs):
		self.base_url = base_url
		self.start_urls = []
		self.start_urls.append(self.base_url)
		self._compile_rules()
		self.rules = (
		Rule(LinkExtractor(allow=()), callback=self.parse_item, follow=True),
		)
		super(pornSpider, self).__init__(*args, **kwargs)

	def parse_item(self, response):
		# if self.base_url in response.url:
		# 	response.meta['depth'] -= 1
		link = FoundLink()
		link['link'] = response.url
		link['is_porn'] = self.is_porn(response)
		link['depth'] = response.meta['depth']
		return link

	def is_porn(self, response):
		porn_urls = ['youporn','redtube','xxvideos','xx','fuck','sex','pornhub','xxhamster','hamster','tube8','tube','porn','lube','cunt','booty','nude','sluts','xvideos','slut','anal','bitch','whore','fap']
		for keyword in porn_urls:
			if keyword in response.url.lower() and 'youtube' not in response.url.lower():
				print('Checking if porn')
				print(keyword)
				print(response.url)
				return True
		return False














