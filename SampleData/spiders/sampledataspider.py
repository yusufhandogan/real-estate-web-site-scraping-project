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
                'https://www.rumah.com/agen-properti/di-yogyakarta/',
                'https://www.rumah.com/agen-properti/di-yogyakarta/2',
                'https://www.rumah.com/agen-properti/di-yogyakarta/3',
                'https://www.rumah.com/agen-properti/di-yogyakarta/4',
                'https://www.rumah.com/agen-properti/di-yogyakarta/5',
                'https://www.rumah.com/agen-properti/di-yogyakarta/6',
                'https://www.rumah.com/agen-properti/di-yogyakarta/7',
                'https://www.rumah.com/agen-properti/di-yogyakarta/8',
                'https://www.rumah.com/agen-properti/di-yogyakarta/9',
                'https://www.rumah.com/agen-properti/di-yogyakarta/10',
                'https://www.rumah.com/agen-properti/di-yogyakarta/11',
                'https://www.rumah.com/agen-properti/di-yogyakarta/12',
                'https://www.rumah.com/agen-properti/di-yogyakarta/13',
                'https://www.rumah.com/agen-properti/di-yogyakarta/14',
                'https://www.rumah.com/agen-properti/di-yogyakarta/15',
                'https://www.rumah.com/agen-properti/di-yogyakarta/16',
                'https://www.rumah.com/agen-properti/di-yogyakarta/17',
                'https://www.rumah.com/agen-properti/di-yogyakarta/18',
                'https://www.rumah.com/agen-properti/di-yogyakarta/19',
                'https://www.rumah.com/agen-properti/di-yogyakarta/20',
                'https://www.rumah.com/agen-properti/di-yogyakarta/21',

        ]

        for url in urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse)

    def parse(self, response):

        for href in response.xpath("//div[@class='agent-contact']/a[@class='nav-link agent-contact-button']"):
            yield {
                "href": href.xpath('@href').extract_first(0)
            }



        """items = names()
        name = response.xpath('//*[@id="wrapper-inner"]/div[8]/div/div/div/section/div[3]/div[1]/div[1]/div[3]/a/@href').extract_first()
        items['name'] = name

        yield items"""


"""                "https://www.rumah.com/agen-properti/bali",
                    "https://www.rumah.com/agen-properti/di-yogyakarta",
                    "https://www.rumah.com/agen-properti/nanggroe-aceh-darussalam",
                    "https://www.rumah.com/agen-properti/kep-bangka-belitung",
                    "https://www.rumah.com/agen-properti/bengkulu",
                    "https://www.rumah.com/agen-properti/banten",
                    "https://www.rumah.com/agen-properti/gorontalo",
                    "https://www.rumah.com/agen-properti/jambi",
                    "https://www.rumah.com/agen-properti/jawa-barat",
                    "https://www.rumah.com/agen-properti/jawa-timur",
                    "https://www.rumah.com/agen-properti/jawa-tengah",
                    "https://www.rumah.com/agen-properti/kalimantan-barat",
                    "https://www.rumah.com/agen-properti/kalimantan-timur",
                    "https://www.rumah.com/agen-properti/kep-riau",
                    "https://www.rumah.com/agen-properti/kalimantan-selatan",
                    "https://www.rumah.com/agen-properti/kalimantan-tengah",
                    "https://www.rumah.com/agen-properti/lampung",
                    "https://www.rumah.com/agen-properti/maluku",
                    "https://www.rumah.com/agen-properti/maluku-utara",
                    "https://www.rumah.com/agen-properti/nusa-tenggara-barat",
                    "https://www.rumah.com/agen-properti/nusa-tenggara-timur", 
                    "https://www.rumah.com/agen-properti/papua",
                    "https://www.rumah.com/agen-properti/papua-barat",
                    "https://www.rumah.com/agen-properti/riau",
                    "https://www.rumah.com/agen-properti/sulawesi-utara",
                    "https://www.rumah.com/agen-properti/sumatera-barat",
                    "https://www.rumah.com/agen-properti/sumatera-selatan",
                    "https://www.rumah.com/agen-properti/sulawesi-tengah",
                    "https://www.rumah.com/agen-properti/sumatera-utara"""
