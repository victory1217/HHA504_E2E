#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:11:25 2021

@author: victoria_rodriguez
"""

## Import needed packages 

from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd 

##Connect to SQL instance 

MYSQL_HOSTNAME = '52.186.53.148' 
MYSQL_USER = 'dba'
MYSQL_PASSWORD = 'ahi2020'
MYSQL_DATABASE = 'e2e'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

## Load CSV File 

csvfile = pd.read_csv('/Users/victoria_rodriguez/Downloads/H1N1_Flu_Vaccines.csv')
csvfile.to_sql('H1N1_Flu_Vaccines', con=engine, if_exists ='append') 
##Note - checked on MySQL Workbench to confirm that the table was loaded

## Create a Trigger 

SELECT * FROM H1N1_Flu_Vaccines LIMIT 15;
DELIMITER $$
CREATE TRIGGER H1N1_concern_trigger BEFORE INSERT ON H1N1_Flu_Vaccines
FOR EACH ROW 
BEGIN IF NEW.alert <=3 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'H1N1 concern should be a numerical value between 0 and 3. Please try again.'
;END IF;
END; $$

