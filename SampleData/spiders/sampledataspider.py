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
            'https://www.rumah.com/agen-properti/banten',
            'https://www.rumah.com/agen-properti/banten/2',
            'https://www.rumah.com/agen-properti/banten/3',
            'https://www.rumah.com/agen-properti/banten/4',
            'https://www.rumah.com/agen-properti/banten/5',
            'https://www.rumah.com/agen-properti/banten/6',
            'https://www.rumah.com/agen-properti/banten/7',
            'https://www.rumah.com/agen-properti/banten/8',
            'https://www.rumah.com/agen-properti/banten/9',
            'https://www.rumah.com/agen-properti/banten/10',
            'https://www.rumah.com/agen-properti/banten/11',
            'https://www.rumah.com/agen-properti/banten/12',
            'https://www.rumah.com/agen-properti/banten/13',
            'https://www.rumah.com/agen-properti/banten/14',
            'https://www.rumah.com/agen-properti/banten/15',
            'https://www.rumah.com/agen-properti/banten/16',
            'https://www.rumah.com/agen-properti/banten/17',
            'https://www.rumah.com/agen-properti/banten/18',
            'https://www.rumah.com/agen-properti/banten/19',
            'https://www.rumah.com/agen-properti/banten/20',
            'https://www.rumah.com/agen-properti/banten/21',
            'https://www.rumah.com/agen-properti/banten/22',
            'https://www.rumah.com/agen-properti/banten/23',
            'https://www.rumah.com/agen-properti/banten/24',
            'https://www.rumah.com/agen-properti/banten/25',
            'https://www.rumah.com/agen-properti/banten/26',
            'https://www.rumah.com/agen-properti/banten/27',
            'https://www.rumah.com/agen-properti/banten/28',
            'https://www.rumah.com/agen-properti/banten/29',
            'https://www.rumah.com/agen-properti/banten/30',
            'https://www.rumah.com/agen-properti/banten/31',
            'https://www.rumah.com/agen-properti/banten/32',
            'https://www.rumah.com/agen-properti/banten/33',
            'https://www.rumah.com/agen-properti/banten/34',
            'https://www.rumah.com/agen-properti/banten/35',
            'https://www.rumah.com/agen-properti/banten/36',
            'https://www.rumah.com/agen-properti/banten/37',
            'https://www.rumah.com/agen-properti/banten/38',
            'https://www.rumah.com/agen-properti/banten/39',
            'https://www.rumah.com/agen-properti/banten/40',
            'https://www.rumah.com/agen-properti/banten/41',
            'https://www.rumah.com/agen-properti/banten/42',
            'https://www.rumah.com/agen-properti/banten/43',
            'https://www.rumah.com/agen-properti/banten/44',
            'https://www.rumah.com/agen-properti/banten/45',
            'https://www.rumah.com/agen-properti/banten/46',
            'https://www.rumah.com/agen-properti/banten/47',
            'https://www.rumah.com/agen-properti/banten/48',
            'https://www.rumah.com/agen-properti/banten/49',
            'https://www.rumah.com/agen-properti/banten/50',
            'https://www.rumah.com/agen-properti/banten/51',
            'https://www.rumah.com/agen-properti/banten/52',
            'https://www.rumah.com/agen-properti/banten/53',
            'https://www.rumah.com/agen-properti/banten/54',
            'https://www.rumah.com/agen-properti/banten/55',
            'https://www.rumah.com/agen-properti/banten/56',
            'https://www.rumah.com/agen-properti/banten/57',
            'https://www.rumah.com/agen-properti/banten/58',
            'https://www.rumah.com/agen-properti/banten/59',
            'https://www.rumah.com/agen-properti/banten/60',
            'https://www.rumah.com/agen-properti/banten/61',
            'https://www.rumah.com/agen-properti/banten/62',
            'https://www.rumah.com/agen-properti/banten/63',
            'https://www.rumah.com/agen-properti/banten/64',
            'https://www.rumah.com/agen-properti/banten/65',
            'https://www.rumah.com/agen-properti/banten/66',
            'https://www.rumah.com/agen-properti/banten/67',
            'https://www.rumah.com/agen-properti/banten/68',
            'https://www.rumah.com/agen-properti/banten/69',
            'https://www.rumah.com/agen-properti/banten/70',
            'https://www.rumah.com/agen-properti/banten/71',
            'https://www.rumah.com/agen-properti/banten/72',
            'https://www.rumah.com/agen-properti/banten/73',
            'https://www.rumah.com/agen-properti/banten/74',
            'https://www.rumah.com/agen-properti/banten/75',
            'https://www.rumah.com/agen-properti/banten/76',
        ]

        for url in urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse)

    def parse(self, response):

        for href in response.xpath("//div[@class='agent-contact']/a[@class='nav-link agent-contact-button']"):
            yield {
                "href": href.xpath('@href').extract_first(0)
            }
