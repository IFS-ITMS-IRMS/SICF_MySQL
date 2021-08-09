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

def drop_tables_l04():

	cur.execute("DROP TABLE IF EXISTS authority_name") # L04:001
	cur.execute("DROP TABLE IF EXISTS mint_name") # L04:002
	cur.execute("DROP TABLE IF EXISTS ruler_name") # L04:003
	cur.execute("DROP TABLE IF EXISTS authority_external_reference") # L04:004
	cur.execute("DROP TABLE IF EXISTS mint_external_reference") # L04:005
	cur.execute("DROP TABLE IF EXISTS modern_person_affiliation_external_reference") # L04:006
	cur.execute("DROP TABLE IF EXISTS organisation_name_external_reference") # L04:007
	cur.execute("DROP TABLE IF EXISTS commune_external_reference") # L04:008
	cur.execute("DROP TABLE IF EXISTS commune_section") # L04:009
	cur.execute("DROP TABLE IF EXISTS commune_external_shorthand") # L04:010
	cur.execute("DROP TABLE IF EXISTS commune_new_commune_old_relation") # L04:011
	cur.execute("DROP TABLE IF EXISTS fundstelle_ort_lieu") # L04:012
	cur.execute("DROP TABLE IF EXISTS period") # L04:013
	cur.execute("DROP TABLE IF EXISTS primary_source_document_editor_junction") # L04:014
	cur.execute("DROP TABLE IF EXISTS user_modern_person_junction") # L04:015

	print("L04-tables dropped")
	return
