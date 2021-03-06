# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_project_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_project_test'

# 爬虫默认存放路径
# 找爬虫的位置
SPIDER_MODULES = ['scrapy_project_test.spiders']
# 新建爬虫的位置
NEWSPIDER_MODULE = 'scrapy_project_test.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"

# Obey robots.txt rules 遵守robots协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 处理最大请求数，默认16， 硬件足够
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 请求延迟 1-3秒之间
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 某个域名或IP发多少个请求
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 是否使用cookie
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 远程连接，本地监听的端口
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 默认的请求报头
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# 爬虫中间件
# SPIDER_MIDDLEWARES = {
#    'scrapy_project_test.middlewares.ScrapyProjectTestSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 下载中间件
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_project_test.middlewares.ScrapyProjectTestDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM中间件, value表示优先级，值越小，优先级越高
# ITEM_PIPELINES = {
#    'scrapy_project_test.pipelines.ScrapyProjectTestPipeline': 300,
#    'scrapy_project_test.pipelines.ScrapyProjectTestMongodbPipeline': 300,
#    'scrapy_project_test.pipelines.ScrapyProjectTestJsonPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
