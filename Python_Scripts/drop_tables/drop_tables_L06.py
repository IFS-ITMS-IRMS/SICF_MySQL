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

def drop_tables_l06():

	cur.execute("DROP TABLE IF EXISTS commune_section_part") # L06:001
	cur.execute("DROP TABLE IF EXISTS fundstelle_flur_lieu_dit_name") # L06:002
	cur.execute("DROP TABLE IF EXISTS fundstelle_flur_lieu_dit_new_old_relation") # L06:002
	cur.execute("DROP TABLE IF EXISTS fundstelle_flur_lieu_dit_external_reference") # L06:003
	cur.execute("DROP TABLE IF EXISTS find") # L06:004
	cur.execute("DROP TABLE IF EXISTS person_muenzadministration_name_external_reference") # L06:005

	print("L06-tables dropped")
	return
