# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class JobScrape(Item):
    
    job_title = Field()
    company = Field()
    location = Field()
    date = Field()
