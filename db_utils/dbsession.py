#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class DbSession(object):
    session = None
    engine = None
    model = None

    def __init__(self,SQLALCHEMY_DATABASE_URI,model):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        _session = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)
        self.session = _session()
        self.model = model

    def create_tables(self):
        """
        仅执行一次，用于初始化数据库，对于已经建立的表不会重建
        :return:
        """
        self.model.metadata.create_all(self.engine)

    def add_data(self, data):
        """
        添加数据到库
        :param data: 在 :class:`datamodel` 中已定义的数据对象，可以是tuple元组
        :return:
        """
        if isinstance(data, list):
            self.session.add_all(data)
        else:
            self.session.add(data)
        self.session.commit()

    def update_data(self, query_string):
        """
        更新数据库
        """
        s = text(query_string)
        self.session.execute(s)
        self.session.commit()

    def query_data(self, query_string):
        """
        通过SQL语句查询数据
        :param query_string:SQL执行语句
        :return:全部查询结果,多行时为tuple元组
        """
        s = text(query_string)
        return self.session.execute(s).fetchall()

    def get_session(self):
        """
        获取当前session，用于自定义执行SQL
        :return: 当前session
        """
        return self.session

    def close_session(self):
        """
        关闭当前session的全部连接,在不再使用session时关闭
        :return:
        """
        self.session.close()
