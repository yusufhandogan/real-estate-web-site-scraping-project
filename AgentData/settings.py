# Scrapy settings for SampleData project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "AgentData"

SPIDER_MODULES = ["AgentData.spiders"]
NEWSPIDER_MODULE = "AgentData.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "SampleData (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
# USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language": "en-gb",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "SampleData.middlewares.SampledataSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "SampleData.middlewares.SampledataDownloaderMiddleware": 543,
# }
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

# LOG_LEVEL = "ERROR"  # to only display errors

DOWNLOADER_MIDDLEWARES = {
    # "rotating_proxies.middlewares.RotatingProxyMiddleware": 610,
    # "rotating_proxies.middlewares.BanDetectionMiddleware": 620,
    # "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    # "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
    # "scrapy_fake_useragent.middleware.RandomUserAgentMiddleware": 400,
    # "scrapy_fake_useragent.middleware.RetryUserAgentMiddleware": 401,
}

# FAKEUSERAGENT_PROVIDERS = [
#     "scrapy_fake_useragent.providers.FakeUserAgentProvider",  # This is the first provider we'll try
#     "scrapy_fake_useragent.providers.FakerProvider",  # If FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
#     "scrapy_fake_useragent.providers.FixedUserAgentProvider",  # Fall back to USER_AGENT value
# ]

# USER_AGENT = (
#     "<your user agent string which you will fall back to if all other providers fail>"
# )

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

FEED_EXPORTERS = {
    "xlsx": "scrapy_xlsx.XlsxItemExporter",
}

# RETRY_HTTP_CODES = [403]

# RETRY_ENABLED = True
# RETRY_TIMES = 5


# ROTATING_PROXY_LIST_PATH = "/home/yusufhandogan/AgentData/AgentData/proxy.txt"

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "SampleData.pipelines.SampledataPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

RETRY_HTTP_CODES = [429]
