# -*- coding: utf-8 -*-

# Scrapy settings for pornDistance project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pornDistance'

SPIDER_MODULES = ['pornDistance.spiders']
NEWSPIDER_MODULE = 'pornDistance.spiders'
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
SPIDER_MIDDLEWARES = {
	'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': 36
	'scrapy.contrib.downloadermiddleware.ajaxcrawl.AjaxCrawlMiddleware' : 28
}
CONCURRENT_REQUESTS = 120
COOKIES_ENABLED = False
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 15
AJAXCRAWL_ENABLED = True
REDIRECT_ENABLED = False
COOKIES_ENABLED = False

EXTENSIONS = {
	'scrapy.contrib.closespider.CloseSpider' : 35
}
CLOSESPIDER_PAGECOUNT = 50
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pornDistance (+http://www.yourdomain.com)'