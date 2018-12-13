#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, text, ForeignKey, Float, Enum

BaseModel = declarative_base()


class DateMap(BaseModel):
    __tablename__ = 'date_map'
    pid = Column(Integer, primary_key=True)

    create_date = Column(Date(), nullable=False, unique=True)

    def __repr__(self):
        return "<ProjectMap(pid='%s', create_date='%s')>" % (self.pid,self.create_date)


class ProjectMeasures(BaseModel):
    __tablename__ = 'project_measures'

    mid = Column(Integer, primary_key=True)
    project_key = Column(String(64), nullable=False)

    bugs = Column(Integer, nullable=False)
    vulnerabilities = Column(Integer, nullable=False)
    code_smells = Column(Integer, nullable=False)

    create_date = Column(Integer, ForeignKey('date_map.pid'), nullable=False)

    def __repr__(self):
        return "<ProjectMetrics(mid='%s', project_key='%s', bugs='%s', vulnerabilities='%s', code_smells='%s', create_date='%s')>" % (
            self.mid,self.project_key, self.bugs, self.vulnerabilities, self.code_smells, self.create_date)


