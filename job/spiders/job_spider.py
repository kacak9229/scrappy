#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website livingsocial.com and
save to a database (postgres).

Scrapy spider part - it actually performs scraping.
"""

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from job.items import JobScrape


class LivingSocialSpider(BaseSpider):
    """Spider for JobsDb website """

    name = "jobs"
    allowed_domains = ['http://my.jobsdb.com/']
    start_urls = ['http://my.jobsdb.com/MY/EN/Search/FindJobs?KeyOpt=COMPLEX&JSRV=1&RLRSF=1&JobCat=37&SearchFields=Positions,Companies&Key=fresh%20graduate&JSSRC=JSRSB']#fresh graduates

    deals_list_xpath = '//div[@id="JobListingSection"]'
    item_fields = {
        'job_title': '//h3[@class="job-title"]/a[@class="posLink"]/text()', 
        #'company': '',
        #'location': '',
        #'date': '',
    }
    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link

        """
        selector = HtmlXPathSelector(response)

        # iterate over deals
        for deal in selector.select(self.deals_list_xpath):
            loader = XPathItemLoader(JobScrape(), selector=deal)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()