# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from models import Jobs, db_connect, create_jobs_table



class JobScrapePipeline(object):
	"""JobDb pipeline for storing scraped items in the database"""

	def __init__(self):
		"""
		Initializez database connection and sessionmaker
		Create jobs table.
		"""
		engine = db_connect()
		create_jobs_table(engine)
		self.Session = sessionmaker(bind=engine)


	def process_item(self, item, spider):
		"""Save deals in the database

		This method is called for every item pipeline component.


		"""
		session = self.Session()
		job = Jobs(**item)

		try:
			session.add(job)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()

		return item

