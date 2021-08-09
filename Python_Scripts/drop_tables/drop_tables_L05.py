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

def drop_tables_l05():

	cur.execute("DROP TABLE IF EXISTS authority_name_external_reference") # L05:001
	cur.execute("DROP TABLE IF EXISTS mint_name_external_reference") # L05:002
	cur.execute("DROP TABLE IF EXISTS ruler_name_external_reference") # L05:003
	cur.execute("DROP TABLE IF EXISTS commune_section_external_reference") # L05:004
	cur.execute("DROP TABLE IF EXISTS fundstelle_ort_lieu_external_shorthand") # L05:005
	cur.execute("DROP TABLE IF EXISTS fundstelle_ort_lieu_external_reference") # L05:006
	cur.execute("DROP TABLE IF EXISTS fundstelle_flur_lieu_dit") # L05:007
	cur.execute("DROP TABLE IF EXISTS person_muenzadministration_name") # L05:008
	cur.execute("DROP TABLE IF EXISTS period_ruler_junction") # L05:009
	cur.execute("DROP TABLE IF EXISTS period_mint_junction") # L05:010
	cur.execute("DROP TABLE IF EXISTS period_external_reference") # L05:011

	print("L05-tables dropped")
	return
