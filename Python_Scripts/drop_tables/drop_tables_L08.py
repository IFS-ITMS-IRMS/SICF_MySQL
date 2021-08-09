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

def drop_tables_l08():

	cur.execute("DROP TABLE IF EXISTS container_fremde_id") # L08:001
	cur.execute("DROP TABLE IF EXISTS container_inventory_number") # L08:002
	cur.execute("DROP TABLE IF EXISTS container_aufbewahrer") # L08:003
	cur.execute("DROP TABLE IF EXISTS container_container_material_junction") # L08:004
	cur.execute("DROP TABLE IF EXISTS container_external_reference") # L08:005
	cur.execute("DROP TABLE IF EXISTS find_object_fremde_id") # L08:006
	cur.execute("DROP TABLE IF EXISTS find_object_inventory_number") # L08:007
	cur.execute("DROP TABLE IF EXISTS find_object_finder") # L08:008
	cur.execute("DROP TABLE IF EXISTS find_object_bringer") # L08:009
	cur.execute("DROP TABLE IF EXISTS find_object_aufbewahrer") # L08:010
	cur.execute("DROP TABLE IF EXISTS find_object_bearbeiter") # L08:011
	cur.execute("DROP TABLE IF EXISTS find_object_peculiarity_of_production_junction") # L08:012
	cur.execute("DROP TABLE IF EXISTS find_object_secondary_treatment_junction") # L08:013
	cur.execute("DROP TABLE IF EXISTS find_object_conservation_state_junction") # L08:014
	cur.execute("DROP TABLE IF EXISTS find_object_external_reference") # L08:015
	cur.execute("DROP TABLE IF EXISTS coin") # L08:"016
	cur.execute("DROP TABLE IF EXISTS other_object") # L08:017
	cur.execute("DROP TABLE IF EXISTS find_object_period_junction") # L08:018
	cur.execute("DROP TABLE IF EXISTS find_object_biblio_junction") # L08:019
	cur.execute("DROP TABLE IF EXISTS find_object_primary_source_document_junction") # L08:020
	cur.execute("DROP TABLE IF EXISTS remark_user_find_object_numeric") # L08:021
	cur.execute("DROP TABLE IF EXISTS remark_user_find_object_text") # L08:022

	print("L08-tables dropped")
	return
