# -*- encoding: utf-8 -*-
# begin

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, Unicode, Binary, LargeBinary, Time, DateTime, Date, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship, backref, deferred
from sqlalchemy.orm import sessionmaker

Base = declarative_base()



class SourceModule1 (Base):
    __tablename__ = "Source_module1"
    ts = Column('ts', Time, primary_key = True)
    nodename = Column('nodename', Unicode, primary_key = True)
    device = Column('device', Unicode, primary_key = True)
    module = Column('module', Unicode, primary_key = True)
    qmin = Column('Qmin', BigInteger)
    qmax = Column('Qmax', Integer)
    qavg = Column('Qavg', Integer)
    alarmtable_ts = Column('AlarmTable_ts', Time, ForeignKey('AlarmTable.ts'))
    alarmtable_nodename = Column('AlarmTable_nodename', Unicode, ForeignKey('AlarmTable.nodename'))
    alarmtable_module = Column('AlarmTable_module', Unicode, ForeignKey('AlarmTable.module'))
    alarmtable_device = Column('AlarmTable_device', Unicode, ForeignKey('AlarmTable.device'))
    predictiontable_ts = Column('PredictionTable_ts', Time, ForeignKey('PredictionTable.ts'))
    predictiontable_nodename = Column('PredictionTable_nodename', Unicode, ForeignKey('PredictionTable.nodename'))
    predictiontable_module = Column('PredictionTable_module', Unicode, ForeignKey('PredictionTable.module'))
    predictiontable_device = Column('PredictionTable_device', Unicode, ForeignKey('PredictionTable.prediction'))

# Saves the Alarms from NMS
class Alarmtable (Base):
    __tablename__ = "AlarmTable"
    ts = Column('ts', Time, primary_key = True)
    nodename = Column('nodename', Unicode, primary_key = True)
    module = Column('module', Unicode, primary_key = True)
    device = Column('device', Unicode, primary_key = True)
    alarmdesc = deferred(Column('alarmDesc', Text))
    severity = Column('severity', Unicode)

class Modelinfo (Base):
    __tablename__ = "modelInfo"
    ts = Column('ts', Time, primary_key = True)
    module = Column('module', Unicode, primary_key = True)
    # Unknown SQL type: 'bigint' 
    run_uuid = Column('run_uuid', String, primary_key = True)
    metrics = Column('metrics', Unicode)
    metric_value = Column('metric_value', BigInteger)
    predictiontable_ts = Column('PredictionTable_ts', Time, ForeignKey('PredictionTable.ts'))
    predictiontable_nodename = Column('PredictionTable_nodename', Unicode, ForeignKey('PredictionTable.nodename'))
    predictiontable_module = Column('PredictionTable_module', Unicode, ForeignKey('PredictionTable.module'))
    predictiontable_device = Column('PredictionTable_device', Unicode, ForeignKey('PredictionTable.device'))

# predictions for each device across nodes and modules
class Predictiontable (Base):
    __tablename__ = "PredictionTable"
    ts = Column('ts', Time, primary_key = True)
    nodename = Column('nodename', Unicode, primary_key = True)
    module = Column('module', Unicode, primary_key = True)
    device = Column('device', Unicode, primary_key = True)
    prediction = Column('prediction', BigInteger)
    score = Column('Score', BigInteger)

# source table for module 2
class SourceModule2 (Base):
    __tablename__ = "Source_module2"
    ts = Column('ts', Time, primary_key = True)
    nodename = Column('nodename', Unicode, primary_key = True)
    device = Column('device', Unicode, primary_key = True)
    module = Column('module', Unicode, primary_key = True)
    berfecmax = Column('berfecmax', BigInteger)
    berfecmin = Column('berfecmin', BigInteger)
    berfecavg = Column('berfecavg', BigInteger)
    alarmtable_ts = Column('AlarmTable_ts', Time, ForeignKey('AlarmTable.ts'))
    alarmtable_nodename = Column('AlarmTable_nodename', Unicode, ForeignKey('AlarmTable.nodename'))
    alarmtable_module = Column('AlarmTable_module', Unicode, ForeignKey('AlarmTable.module'))
    alarmtable_device = Column('AlarmTable_device', Unicode, ForeignKey('AlarmTable.device'))
    predictiontable_ts = Column('PredictionTable_ts', Time, ForeignKey('PredictionTable.ts'))
    predictiontable_nodename = Column('PredictionTable_nodename', Unicode, ForeignKey('PredictionTable.nodename'))
    predictiontable_module = Column('PredictionTable_module', Unicode, ForeignKey('PredictionTable.module'))
    predictiontable_device = Column('PredictionTable_device', Unicode, ForeignKey('PredictionTable.device'))

# source table for module 2
class SourceModule3 (Base):
    __tablename__ = "Source_module3"
    ts = Column('ts', Time, primary_key = True)
    nodename = Column('nodename', Unicode, primary_key = True)
    device = Column('device', Unicode, primary_key = True)
    module = Column('module', Unicode, primary_key = True)
    podmax = Column('podmax', BigInteger)
    podmin = Column('podmin', BigInteger)
    podavg = Column('podavg', BigInteger)
    alarmtable_ts = Column('AlarmTable_ts', Time, ForeignKey('AlarmTable.ts'))
    alarmtable_nodename = Column('AlarmTable_nodename', Unicode, ForeignKey('AlarmTable.nodename'))
    alarmtable_module = Column('AlarmTable_module', Unicode, ForeignKey('AlarmTable.module'))
    alarmtable_device = Column('AlarmTable_device', Unicode, ForeignKey('AlarmTable.device'))
    predictiontable_ts = Column('PredictionTable_ts', Time, ForeignKey('PredictionTable.ts'))
    predictiontable_nodename = Column('PredictionTable_nodename', Unicode, ForeignKey('PredictionTable.nodename'))
    predictiontable_module = Column('PredictionTable_module', Unicode, ForeignKey('PredictionTable.module'))
    predictiontable_device = Column('PredictionTable_device', Unicode, ForeignKey('PredictionTable.device'))

# end
