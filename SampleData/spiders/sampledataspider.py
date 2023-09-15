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
            'https://www.rumah.com/agen-properti/jawa-timur/2',
            'https://www.rumah.com/agen-properti/jawa-timur/3',
            'https://www.rumah.com/agen-properti/jawa-timur/4',
            'https://www.rumah.com/agen-properti/jawa-timur/5',
            'https://www.rumah.com/agen-properti/jawa-timur/6',
            'https://www.rumah.com/agen-properti/jawa-timur/7',
            'https://www.rumah.com/agen-properti/jawa-timur/8',
            'https://www.rumah.com/agen-properti/jawa-timur/9',
            'https://www.rumah.com/agen-properti/jawa-timur/10',
            'https://www.rumah.com/agen-properti/jawa-timur/11',
            'https://www.rumah.com/agen-properti/jawa-timur/12',
            'https://www.rumah.com/agen-properti/jawa-timur/13',
            'https://www.rumah.com/agen-properti/jawa-timur/14',
            'https://www.rumah.com/agen-properti/jawa-timur/15',
            'https://www.rumah.com/agen-properti/jawa-timur/16',
            'https://www.rumah.com/agen-properti/jawa-timur/17',
            'https://www.rumah.com/agen-properti/jawa-timur/18',
            'https://www.rumah.com/agen-properti/jawa-timur/19',
            'https://www.rumah.com/agen-properti/jawa-timur/20',
            'https://www.rumah.com/agen-properti/jawa-timur/21',
            'https://www.rumah.com/agen-properti/jawa-timur/22',
            'https://www.rumah.com/agen-properti/jawa-timur/23',
            'https://www.rumah.com/agen-properti/jawa-timur/24',
            'https://www.rumah.com/agen-properti/jawa-timur/25',
            'https://www.rumah.com/agen-properti/jawa-timur/26',
            'https://www.rumah.com/agen-properti/jawa-timur/27',

        ]

        for url in urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse)

    def parse(self, response):

        for href in response.xpath("//div[@class='agent-contact']/a[@class='nav-link agent-contact-button']"):
            yield {
                "href": href.xpath('@href').extract_first(0)
            }
