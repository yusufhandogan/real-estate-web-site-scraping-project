# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AgentdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    
    Agent = scrapy.Field()
    
    Agency = scrapy.Field()
    
    Phone = scrapy.Field()
    
    Whatsapp = scrapy.Field()
