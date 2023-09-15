import scrapy
from urllib.parse import urlencode
#from SampleData.items import names

API_KEY = '983e9cb8-ec3e-4d5f-9ae1-874837c26cbe'


def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class QuotesSpider(scrapy.Spider):

    name = "urls_city"

    def start_requests(self):

        urls = [
                'https://www.rumah.com/agen-properti/kalimantan-barat',
                'https://www.rumah.com/agen-properti/kalimantan-barat/2',
                'https://www.rumah.com/agen-properti/kalimantan-barat/3',
                'https://www.rumah.com/agen-properti/kalimantan-barat/4',

        ]

        for url in urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse)

    def parse(self, response):

        for href in response.xpath("//div[@class='agent-contact']/a[@class='nav-link agent-contact-button']"):
            yield {
                "href": href.xpath('@href').extract_first(0)
            }
