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

def drop_tables_l02():

	cur.execute("DROP TABLE IF EXISTS denomination") # L02:001
	cur.execute("DROP TABLE IF EXISTS place") # L02:002
	cur.execute("DROP TABLE IF EXISTS field_of_numismatics_external_reference") # L02:003
	cur.execute("DROP TABLE IF EXISTS modern_person_name_external_reference") # L02:004
	cur.execute("DROP TABLE IF EXISTS modern_region_external_reference") # L02:005
	cur.execute("DROP TABLE IF EXISTS numismatic_time_slice_external_reference") # L02:006
	cur.execute("DROP TABLE IF EXISTS district") # L02:007
	cur.execute("DROP TABLE IF EXISTS ruler_external_reference") # L02:008
	cur.execute("DROP TABLE IF EXISTS type_external_reference") # L02:009
	cur.execute("DROP TABLE IF EXISTS other_object_type_external_reference") # L02:010
	cur.execute("DROP TABLE IF EXISTS other_object_name_external_reference") # L02:011
	cur.execute("DROP TABLE IF EXISTS archaeological_event_fremde_id") # L02:012
	cur.execute("DROP TABLE IF EXISTS archaeological_event_external_reference") # L02:013
	cur.execute("DROP TABLE IF EXISTS arch_event_new_arch_event_old_relation") # L02:014
	cur.execute("DROP TABLE IF EXISTS person_muenzadministration_external_reference") # L02:015
	cur.execute("DROP TABLE IF EXISTS art_der_fundstelle_type_external_reference") # L02:016
	cur.execute("DROP TABLE IF EXISTS art_der_fundstelle_detail") # L02:017
	cur.execute("DROP TABLE IF EXISTS bibliography_language_junction") # L02:018
	cur.execute("DROP TABLE IF EXISTS bibliography_bibliography_part") # L02:019
	cur.execute("DROP TABLE IF EXISTS bibliography_external_reference") # L02:020
	cur.execute("DROP TABLE IF EXISTS biblio_citation") # L02:021
	cur.execute("DROP TABLE IF EXISTS primary_source_document_aufbewahrer") # L02:022
	cur.execute("DROP TABLE IF EXISTS primary_source_document_author_junction") # L02:023
	cur.execute("DROP TABLE IF EXISTS primary_source_document_informative_value_junction") # L02:024
	cur.execute("DROP TABLE IF EXISTS primary_source_document_language_junction") # L02:025
	cur.execute("DROP TABLE IF EXISTS primary_source_document_manufacture_junction") # L02:026
	cur.execute("DROP TABLE IF EXISTS primary_source_document_external_reference") # L02:027
	cur.execute("DROP TABLE IF EXISTS prim_source_doc_prim_source_doc_part") # L02:028
	cur.execute("DROP TABLE IF EXISTS primary_source_document_citation") # L02:029
	cur.execute("DROP TABLE IF EXISTS remark_user_bibliography_text") # L02:030
	cur.execute("DROP TABLE IF EXISTS remark_user_bibliography_numeric") # L02:031
	cur.execute("DROP TABLE IF EXISTS archaeological_event_part") # L02:032

	print("L02-tables dropped")
	return
