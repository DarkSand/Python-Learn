#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sqlalchemy import Column, Integer, String, DateTime, Numeric, create_engine, VARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    sex = Column(String(100))
    account = Column(String(100))
    password = Column(String(100))
    date = Column(DateTime())


DB_CONNECT_STRING = 'sqlite:///' + os.path.dirname(__file__) + '/user.db'
CONNECT_ARGS = {'check_same_thread': False}

engine = create_engine(DB_CONNECT_STRING, echo=False, connect_args=CONNECT_ARGS)

DB_Session = sessionmaker(bind=engine)
session = DB_Session()

Base.metadata.create_all(engine)

user = User(name='mao', sex='man', account='darkwings', password='123456', date=datetime.datetime.utcnow())

session.add(user)
session.commit()
session.close()

for s in session.query(User).filter(User.name == 'mao'):
    print s.date
