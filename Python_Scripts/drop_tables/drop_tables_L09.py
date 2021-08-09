# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:43:45 2021

@author: marga
"""

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

def drop_tables_l09():

	cur.execute("DROP TABLE IF EXISTS coin_field_of_numismatics_junction") # L09:001
	cur.execute("DROP TABLE IF EXISTS coin_authority_junction") # L09:002
	cur.execute("DROP TABLE IF EXISTS coin_issuer_portrait_junction") # L09:003
	cur.execute("DROP TABLE IF EXISTS coin_mint_junction") # L09:004
	cur.execute("DROP TABLE IF EXISTS coin_denomination_junction") # L09:005
	cur.execute("DROP TABLE IF EXISTS coin_type_junction") # L09:006
	cur.execute("DROP TABLE IF EXISTS coin_mintmaster_junction") # L09:007
	cur.execute("DROP TABLE IF EXISTS other_object_issuer_junction") # L09:008
	cur.execute("DROP TABLE IF EXISTS other_object_portrait_junction") # L09:009
	cur.execute("DROP TABLE IF EXISTS other_object_issuing_location_junction") # L09:010
	cur.execute("DROP TABLE IF EXISTS other_object_producer_junction") # L09:011
	cur.execute("DROP TABLE IF EXISTS other_object_production_place_junction") # L09:012
	cur.execute("DROP TABLE IF EXISTS other_object_type_junction") # L09:013
	cur.execute("DROP TABLE IF EXISTS other_object_name_junction") # L09:014

	print("L09-tables dropped")
	return
