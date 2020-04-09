import sqlalchemy
from sqlalchemy import create_engine, Column, Text, Integer, DateTime, Date, ForeignKey, Float, Boolean, MetaData, func, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date, datetime
import pandas as pd
import numpy as np

metadata = MetaData()

# create and connect sqlalchemy engine
engine = create_engine('sqlite:///realestate.db')
engine.connect()

# declare db as Base
Base = declarative_base()

### BUILDING TABLES ###

# Sellers Table
class Sellers(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(Text)
    lastname = Column(Text)
    email = Column(Text)
    phone = Column(Text)

    def __repr__(self):
        return "<Sellers(id={0}, firstname={1}, lastname={2}, email={3}, phone={4}>".format(self.id, self.firstname, self.lastname, self.email, self.phone)


# Real Estate Agents Table
class RealEstateAgents(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(Text)
    lastname = Column(Text)
    email = Column(Text)

    def __repr__(self):
        return "<RealEstateAgents(id={0}, firstname={1}, lastname={2}, email={3})>".format(self.id, self.firstname, self.lastname, self.email)


# Offices Table
class Offices(Base):
    __tablename__ = 'offices'
    id = Column(Integer, primary_key=True, index=True)
    region = Column(Text)

    def __repr__(self):
        return "<Offices(id={0}, region={1})>".format(self.id, self.region)


# Houses Table
class Houses(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True, index=True)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    zipcode = Column(Text)
    price = Column(Float)
    datelisted = Column(Date)
    sellerid = Column(Integer, ForeignKey('sellers.id'))
    agentid = Column(Integer, ForeignKey('agents.id'))
    officeid = Column(Integer, ForeignKey('offices.id'))
    sold = Column(Boolean)

    def __repr__(self):
        return "<Houses(id={0}, bedrooms={1}, bathrooms={2},\
            zipcode={3}, price={4}, datelisted={5},\
            sellerid={6}, agentid={7}, officeid={8}, sold={9})>".format(self.id, self.bedrooms, self.bathrooms,
                                                                        self.zipcode, self.price, self.datelisted, 
                                                                        self.sellerid, self.agentid, self.officeid,
                                                                        self.sold)


# Buyers Table
class Buyers(Base):
    __tablename__ = 'buyers'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(Text)
    lastname = Column(Text)
    email = Column(Text)

    def __repr__(self):
        return "<Buyers(id={0}, firstname={1}, lastname={2}, email={3})>".format(self.id, self.firstname, self.lastname, self.email)


# Sales Table
class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, index=True)
    selldate = Column(Date)
    finalprice = Column(Float)
    houseid = Column(Integer, ForeignKey('houses.id'))
    buyerid = Column(Integer, ForeignKey('buyers.id'))
    officeid = Column(Integer, ForeignKey('offices.id'))
    agentid = Column(Integer, ForeignKey('agents.id'))

    def __repr__(self):
        return "<Sales(id={0}, selldate={1}, finalprice={2}, \
            houseid={3}, buyerid={4}, officeid={5}, agentid={6})>".format(self.id, self.selldate, self.finalprice,
                                                             self.houseid, self.buyerid, self.officeid, self.agentid)


# Profit Table
class Profits(Base):
    __tablename__ = 'profits'
    id = Column(Integer, primary_key=True, index=True)
    saleid = Column(Integer, ForeignKey('sales.id'))
    commission = Column(Float)
    agentid = Column(Integer, ForeignKey('agents.id'))

    def __repr__(self):
        return '<Profits(id={0}, saleid={1}, commission={2}, agentid={3})>'.format(self.id, self.saleid,
                                                                             self.commission, self.agentid)

# Summary Table
class Summary(Base):
    __tablename__ = 'summary'
    id = Column(Integer, primary_key=True, index=True)
    sumofsales = Column(Float)
    totalcommission = Column(Float)

    def __repr__(self):
        return "<Summary(id={0}, sumofsales={1}, totalcommission={2})>".format(self.id, self.sumofsales,
                                                                             self.totalcommission)