import pymysql
import pymysql.cursors
import config

def connect_to_database():
  options = {
    'host': config.env['host'],
    'user': config.env['user'],
    'passwd': config.env['password'],
    'db': config.env['db'],
    'cursorclass' : pymysql.cursors.DictCursor,
    'charset': 'utf8'
  }
  db = pymysql.connect(**options)
  db.autocommit(True)
  return db
