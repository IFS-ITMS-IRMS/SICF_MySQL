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

def drop_tables_l07():

	cur.execute("DROP TABLE IF EXISTS find_fremde_id") # L07:001
	cur.execute("DROP TABLE IF EXISTS find_finder") # L07:002
	cur.execute("DROP TABLE IF EXISTS find_bringer") # L07:003
	cur.execute("DROP TABLE IF EXISTS find_aufbewahrer") # L07:004
	cur.execute("DROP TABLE IF EXISTS find_bearbeiter") # L07:005
	cur.execute("DROP TABLE IF EXISTS find_discovery_method_junction") # L07:006
	cur.execute("DROP TABLE IF EXISTS find_find_category_junction") # L07:007
	cur.execute("DROP TABLE IF EXISTS find_find_type_junction") # L07:008
	cur.execute("DROP TABLE IF EXISTS find_sicf_number") # L07:009
	cur.execute("DROP TABLE IF EXISTS find_external_reference") # L07:010
	cur.execute("DROP TABLE IF EXISTS find_find_part") # L07:011
	cur.execute("DROP TABLE IF EXISTS find_object") # L07:012
	cur.execute("DROP TABLE IF EXISTS container") # L07:013
	cur.execute("DROP TABLE IF EXISTS find_archaeological_event_junction") # L07:014
	cur.execute("DROP TABLE IF EXISTS find_art_der_fundstelle_category_junction") # L07:015
	cur.execute("DROP TABLE IF EXISTS find_art_der_fundstelle_type_junction") # L07:016
	cur.execute("DROP TABLE IF EXISTS find_art_der_fundstelle_detail_junction") # L07:017
	cur.execute("DROP TABLE IF EXISTS find_biblio_junction") # L07:018
	cur.execute("DROP TABLE IF EXISTS find_primary_source_document_junction") # L07:019
	cur.execute("DROP TABLE IF EXISTS remark_user_find_numeric") # L07:020
	cur.execute("DROP TABLE IF EXISTS remark_user_find_text") # L07:021

	print("L07-tables dropped")
	return
