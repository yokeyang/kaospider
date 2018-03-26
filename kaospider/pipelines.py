# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

def dbInfo(db):
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'yang218906',
        charset = 'utf8mb4',
        use_unicode = False,
        db = db
    )
    return conn
class KaospiderPipeline(object):
    def process_item(self, item, spider):
        emoji = item['emoji']
        textEnglish = item['text_english']
        table = item['table']
        conn = dbInfo('emoji')
        cursor = conn.cursor()
        cursor.execute("SET NAMES utf8mb4")
        cursor.execute(
            "create table if not exists %s(id int NOT NULL AUTO_INCREMENT primary key,emoji char(100),text_english char(100),text_chinese char(100))ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;" 
            % (table))
        conn.commit()
        cursor.execute('insert into %s(emoji,text_english) values("%s","%s")'
                        % (table, emoji, textEnglish))
        cursor.close()
        conn.commit()
        print(u"插入数据成功")
        conn.close()

    def close_spider(self, spider):
        pass

class pipeline2(object):
    def process_item(self, item, spider):
        kaomoji = item['kaomoji']
        textJapanese = item['text_japanese']
        table = item['table']
        conn = dbInfo('kaomoji')
        cursor = conn.cursor()
        cursor.execute("SET NAMES utf8mb4")
        cursor.execute(
            "create table if not exists %s(id int NOT NULL AUTO_INCREMENT primary key,kaomoji char(100),text_japanese char(100),text_chinese char(100))ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;" % (table))
        conn.commit()
        cursor.execute('insert into %s(kaomoji,text_japanese) values("%s","%s")'
                        % (table, kaomoji, textJapanese))
        cursor.close()
        conn.commit()
        print(u"插入数据成功")
        conn.close()

    def close_spider(self, spider):
        pass
