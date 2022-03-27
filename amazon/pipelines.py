# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector

class AmazonPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='booksdb'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS books """)
        self.curr.execute("""create table books (book_name text,book_author text, book_price text)""")
        #self.curr.execute("""insert into books values('a','b',1)""")

    def store_data(self,item):
        name = len(item['book_name'])

        author = len(item['book_author'])

        price=len(item['book_price'])

        size = min(name,author,price)
        for i in range(0,size):
            self.curr.execute("""insert into books values(%s,%s,%s)""",(item['book_name'][i],item['book_author'][i],
                                                                     item['book_price'][i]))
        self.conn.commit()

    def process_item(self, item, spider):

        self.store_data(item)

        return item
