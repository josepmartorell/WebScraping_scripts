# -*- coding: utf-8 -*-

# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class SQLlitePipeline(object):

    def open_spider(self, spider):
        # todo -1/CONNECTION: create connection ('A new file called “imdb.db” will be created where our database will
        #  be stored').
        self.connection = sqlite3.connect("imdb.db")
        # todo -2/CURSOR: To execute SQLite statements in Python, you need a cursor object.
        #  You can create it using the cursor () method.
        self.cursor = self.connection.cursor()
        # todo -3/EXECUTE: Using the cursor object, execute method is executed with CREATE TABLE query as parameter
        try:
            self.cursor.execute('''
                CREATE TABLE best_movies(
                    title TEXT,
                    year TEXT,
                    duration TEXT,
                    genre TEXT,
                    rating TEXT,
                    movie_url TEXT
                )
            
            ''')
        # todo -4/COMMIT: The commit () method saves all the changes we make.
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        # todo -5/CLOSE: Finally the close () method closes the connection.
        self.connection.close()

    def process_item(self, item, spider):
        # todo -1/EXECUTE: Using the cursor object, execute method is executed with INSERT INTO query as parameter
        self.cursor.execute('''
            INSERT INTO best_movies (title,year,duration,genre,rating,movie_url) VALUES(?,?,?,?,?,?)

        ''', (
            item.get('title'),
            item.get('year'),
            item.get('duration'),
            item.get('genre'),
            item.get('rating'),
            item.get('movie_url')
        ))
        # todo -2/COMMIT: The commit () method saves all the changes we make.
        self.connection.commit()
        return item
