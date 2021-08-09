# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:32:13 2021

@author: marga
"""

from drop_tables import drop_tables_L00 as dtl00 # L00-tables
from create_tables import create_tables_L00 as ctl00 # L00-tables

from drop_tables import drop_tables_L01 as dtl01 # L01-tables
from create_tables import create_tables_L01 as ctl01 # L01-tables

from drop_tables import drop_tables_L02 as dtl02 # L02-tables
from create_tables import create_tables_L02 as ctl02 # L02-tables

from drop_tables import drop_tables_L03 as dtl03 # L03-tables
from create_tables import create_tables_L03 as ctl03 # L03-tables

from drop_tables import drop_tables_L04 as dtl04 # L04-tables
from create_tables import create_tables_L04 as ctl04 # L04-tables

from drop_tables import drop_tables_L05 as dtl05 # L05-tables
from create_tables import create_tables_L05 as ctl05 # L05-tables

from drop_tables import drop_tables_L06 as dtl06 # L06-tables
from create_tables import create_tables_L06 as ctl06 # L06-tables

from drop_tables import drop_tables_L07 as dtl07 # L07-tables
from create_tables import create_tables_L07 as ctl07 # L07-tables

from drop_tables import drop_tables_L08 as dtl08 # L08-tables
from create_tables import create_tables_L08 as ctl08 # L08-tables

from drop_tables import drop_tables_L09 as dtl09 # L09-tables
from create_tables import create_tables_L09 as ctl09 # L09-tables

import mysql.connector

global mydb
mydb = mysql.connector.connect(
	host="localhost",
	user="IFS",
	password="IFS_pw",
	database = "Mock_up_DB"
)

global cur
cur = mydb.cursor()

"""
-------------------------------------------
"""

# Drop existing tables

# Drop L09-tables

dtl09.drop_tables_l09()

# Drop L08-tables

dtl08.drop_tables_l08()

# Drop L07-tables

dtl07.drop_tables_l07()

# Drop L06-tables

dtl06.drop_tables_l06()

# Drop L05-tables

dtl05.drop_tables_l05()

# Drop L04-tables

dtl04.drop_tables_l04()

# Drop L03-tables

dtl03.drop_tables_l03()

# Drop L02-tables

dtl02.drop_tables_l02()

# Drop L01-tables

dtl01.drop_tables_l01()

# Drop L00-tables

dtl00.drop_tables_l00()

"""
-------------------------------------------
"""

# L00: Create basic tables, meaning tables without dependencies to other tables

ctl00.create_tables_l00()

# L01: Create tables with dependencies to basic tables (L00-tables)

ctl01.create_tables_l01()

# L02: Create tables with dependencies to tables up to and including L01

ctl02.create_tables_l02()

# L03: Create tables with dependencies to tables up to and including L02

ctl03.create_tables_l03()

# L04: Create tables with dependencies to tables up to and including L03

ctl04.create_tables_l04()

# L05: Create tables with dependencies to tables up to and including L04

ctl05.create_tables_l05()

# L06: Create tables with dependencies to tables up to and including L05

ctl06.create_tables_l06()

# L07: Create tables with dependencies to tables up to and including L06

ctl07.create_tables_l07()

# L08: Create tables with dependencies to tables up to and including L07

ctl08.create_tables_l08()

# L09: Create tables with dependencies to tables up to and including L08

ctl09.create_tables_l09()
