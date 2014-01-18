# Scrapy settings for job project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'job'

SPIDER_MODULES = ['job.spiders']
NEWSPIDER_MODULE = 'job.spiders'

DATABASE = {'drivername': 'postgres',
			'host': 'localhost',
			'port': '5432',
			'username': 'naufal',
			'password': 'worldwideweb',
			'database': 'jobscrape'


}

ITEM_PIPELINES = ['job.pipelines.JobScrapePipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'job (+http://www.yourdomain.com)'
