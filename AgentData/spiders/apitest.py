import scrapy
import json


class RumahSpider(scrapy.Spider):
    name = "rumah_spider"
    start_urls = [
        "https://www.rumah.com/api/consumer/recommendation?type=ldp&locale=id&listingId=21802278&maxItems=8&propertyType=Rumah&listingType=SALE&price=1900000000&floorArea=250&bedrooms=6"
    ]

    def parse(self, response):
        data = json.loads(response.text)

        for item in data["data"]:
            title = item["title"]
            address = item["address"]
            price = item["price"]

            yield {"title": title, "address": address, "price": price}
