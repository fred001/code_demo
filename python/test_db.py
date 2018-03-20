#!/usr/bin/env python
#-*- coding: utf-8 -*- 
import sys,os
from sys import exit
from random import randint 
import time,random
import unittest

"""
  frd python lib 之 frd.db.mysql 库测试用例

  Usage:
    python test_db.py
"""

filename=os.path.abspath(__file__)
current_dir=os.path.dirname(filename)
parent_dir=os.path.dirname(current_dir)


sys.path.append(parent_dir)
import frd.db.mysql as db


class TestDb(unittest.TestCase):
  def setUp(self):
    db.connect("root","","test")
    
    sql="CREATE TABLE if not exists `user` (    \
        `id` int(10) NOT NULL AUTO_INCREMENT,    \
        `name` char(20) DEFAULT NULL,    \
        `password` char(20) DEFAULT NULL,    \
        PRIMARY KEY (`id`)    \
    ) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8 "

    db.execute(sql)

    #clear data
    db.execute('delete from user')

  def tearDown(self):
    #clear data
    db.execute('delete from user')


  #insert
  #update
  #delete
  #exists
  def test_table(self):
    user=db.Table("user","id")
    user_id=user.insert({"name":"frd","password":"111"})
    self.assertTrue(user_id > 0)

    user.update(user_id,{"name":"frd2"})
    data=user.get(user_id)
    self.assertTrue(data['name'] == "frd2")

    user.delete(user_id)
    data=user.get(user_id)
    self.assertFalse(data)

    ret=user.exists(user_id)
    self.assertFalse(ret)

    #clear data
    db.execute('delete from user')

  #insert where
  #update where
  #delete where
  #exists where
  def test_table_extra(self):
    user=db.Table("user","id")
    user_id=user.insert({"name":"frd","password":"111"})
    self.assertTrue(user_id > 0)

    where={"name":"frd"}
    data={"name":"frd2","password":"111"}
    ret=user.insertWhere(where,data)

    user_data=user.get(user_id)
    self.assertTrue(user_data['name'] == "frd2")

    where={"name":"frd2"}
    data={"name":"frd3","password":"111"}
    user.updateWhere(where,data)
    user_data=user.get(user_id)
    self.assertTrue(user_data['name'] == "frd3")

    where={"name":"frd2"}
    user.deleteWhere(where)
    ret=user.existsWhere(where)
    self.assertFalse(ret)

    #clear data
    db.execute('delete from user')

  def test_table_query(self):
    user=db.Table("user","id")
    user_id=user.insert({"name":"frd","password":"111"})
    self.assertTrue(user_id > 0)

    rows=user.getAll() 
    self.assertTrue(len(rows) == 1)

    row=user.getRow() 
    self.assertTrue(row['name'] == 'frd')

    field=user.getOne({},'name') 
    self.assertTrue(field == "frd")

    #clear data
    db.execute('delete from user')


  def test_db(self):
    user=db.Table("user","id")
    user_id=user.insert({"name":"frd","password":"111"})
    self.assertTrue(user_id > 0)

    rows=db.fetchAll("select * from user where name=%s",("frd",))
    self.assertTrue(len(rows) == 1)

    row=db.fetchRow("select * from user where name=%s",("frd",))
    self.assertTrue(row['name'] == 'frd')

    user_id=db.fetchOne("select * from user where name=%s",("frd",))
    self.assertTrue(user_id > 0)



if __name__ == "__main__":
  unittest.main()

