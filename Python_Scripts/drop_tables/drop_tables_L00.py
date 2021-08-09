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

def drop_tables_l00():
	
	
	cur.execute("DROP TABLE IF EXISTS primary_source_document_junction_boilerplate") # L00:--- old

	cur.execute("DROP TABLE IF EXISTS modern_person") # L00:003
	cur.execute("DROP TABLE IF EXISTS yes_no_unknown") # L00:004
	cur.execute("DROP TABLE IF EXISTS datenqualitaet") # L00:005
	cur.execute("DROP TABLE IF EXISTS bearbeitungsstand") # L00:006
	cur.execute("DROP TABLE IF EXISTS remark_user_tag") # L00:007
	cur.execute("DROP TABLE IF EXISTS region_category") # L00:008
	cur.execute("DROP TABLE IF EXISTS geographical_unit") # L00:009
	cur.execute("DROP TABLE IF EXISTS primary_source_document_informative_value") # L00:010
	cur.execute("DROP TABLE IF EXISTS era") # L00:011
	cur.execute("DROP TABLE IF EXISTS calendar") # L00:012
	cur.execute("DROP TABLE IF EXISTS material") # L00:013
	cur.execute("DROP TABLE IF EXISTS container_material") # L00:014
	cur.execute("DROP TABLE IF EXISTS manufacture") # L00:015
	cur.execute("DROP TABLE IF EXISTS peculiarity_of_production") # L00:016
	cur.execute("DROP TABLE IF EXISTS secondary_treatment") # L00:017
	cur.execute("DROP TABLE IF EXISTS conservation_state") # L00:018
	cur.execute("DROP TABLE IF EXISTS external_nomenclature") # L00:019
	cur.execute("DROP TABLE IF EXISTS discovery_method") # L00:020
	cur.execute("DROP TABLE IF EXISTS art_der_fundstelle_category") # L00:021
	cur.execute("DROP TABLE IF EXISTS find_category") # L00:022
	cur.execute("DROP TABLE IF EXISTS object_category") # L00:023
	cur.execute("DROP TABLE IF EXISTS authenticity") # L00:024
	cur.execute("DROP TABLE IF EXISTS authenticity_interpretation") # L00:025
	cur.execute("DROP TABLE IF EXISTS external_reference_data_source") # L00:026
	cur.execute("DROP TABLE IF EXISTS wear") # L00:027
	cur.execute("DROP TABLE IF EXISTS corrosion") # L00:028
	cur.execute("DROP TABLE IF EXISTS face") # L00:029
	cur.execute("DROP TABLE IF EXISTS form_aufsicht") # L00:030
	cur.execute("DROP TABLE IF EXISTS form_querschnitt") # L00:031
	cur.execute("DROP TABLE IF EXISTS publication_type") # L00:032
	cur.execute("DROP TABLE IF EXISTS biblio_junction_type") # L00:033
	cur.execute("DROP TABLE IF EXISTS biblio_junction_boilerplate") # L00:034
	cur.execute("DROP TABLE IF EXISTS language") # L00:035
	cur.execute("DROP TABLE IF EXISTS primary_source_document_type") # L00:036
	cur.execute("DROP TABLE IF EXISTS primary_source_document_manufacture") # L00:037
	cur.execute("DROP TABLE IF EXISTS gender") # L00:038
	cur.execute("DROP TABLE IF EXISTS modern_state") # L00:039
	cur.execute("DROP TABLE IF EXISTS organisation") # L00:040
	cur.execute("DROP TABLE IF EXISTS find_type") # L00:041
	cur.execute("DROP TABLE IF EXISTS other_object_category") # L00:042
	cur.execute("DROP TABLE IF EXISTS biblio_junction_Detaillierungsgrad") # L00:043
	cur.execute("DROP TABLE IF EXISTS function_table") # L00:044
	
	
	
	cur.execute("DROP TABLE IF EXISTS data_source") # must be second to last to drop! L00:002
	cur.execute("DROP TABLE IF EXISTS user") # must be last to drop! L00:001

	print("L00-tables dropped")
	return