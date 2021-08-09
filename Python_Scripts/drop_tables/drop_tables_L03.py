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

def drop_tables_l03():

	cur.execute("DROP TABLE IF EXISTS authority") # L03:001
	cur.execute("DROP TABLE IF EXISTS geographical_unit_part") # L03:002
	cur.execute("DROP TABLE IF EXISTS mint") # L03:003
	cur.execute("DROP TABLE IF EXISTS modern_person_affiliation") # L03:004
	cur.execute("DROP TABLE IF EXISTS organisation_name") # L03:005
	cur.execute("DROP TABLE IF EXISTS denomination_external_reference") # L03:006
	cur.execute("DROP TABLE IF EXISTS place_external_reference") # L03:007
	cur.execute("DROP TABLE IF EXISTS district_external_reference") # L03:008
	cur.execute("DROP TABLE IF EXISTS commune") # L03:009
	cur.execute("DROP TABLE IF EXISTS art_der_fundstelle_detail_external_reference") # L03:010
	cur.execute("DROP TABLE IF EXISTS bibliography_place_of_publication_junction") # L03:011
	cur.execute("DROP TABLE IF EXISTS primary_source_document_place_of_production_junction") # L03:012
	cur.execute("DROP TABLE IF EXISTS biblio_citation_external_reference") # L03:013
	cur.execute("DROP TABLE IF EXISTS primary_source_document_aufbewahrer_external_reference") # L03:014
	cur.execute("DROP TABLE IF EXISTS primary_source_document_citation_external_reference") # L03:015

	print("L03-tables dropped")
	return
