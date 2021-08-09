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

def drop_tables_l01():

	cur.execute("DROP TABLE IF EXISTS field_of_numismatics") # L01:001
	cur.execute("DROP TABLE IF EXISTS numismatic_time_slice") # L01:002
	cur.execute("DROP TABLE IF EXISTS find_type_external_reference") # L01:003
	cur.execute("DROP TABLE IF EXISTS other_object_category_external_reference") # L01:004
	cur.execute("DROP TABLE IF EXISTS art_der_fundstelle_type") # L01:005
	cur.execute("DROP TABLE IF EXISTS type") # L01:006
	cur.execute("DROP TABLE IF EXISTS ruler") # L01:007
	cur.execute("DROP TABLE IF EXISTS modern_person_name") # L01:008
	cur.execute("DROP TABLE IF EXISTS modern_region") # L01:009
	cur.execute("DROP TABLE IF EXISTS authenticity_external_reference") # L01:010
	cur.execute("DROP TABLE IF EXISTS authenticity_interpretation_external_reference") # L01:011
	cur.execute("DROP TABLE IF EXISTS bearbeitungsstand_external_reference") # L01:012
	cur.execute("DROP TABLE IF EXISTS conservation_state_external_reference") # L01:013
	cur.execute("DROP TABLE IF EXISTS container_material_external_reference") # L01:014
	cur.execute("DROP TABLE IF EXISTS corrosion_external_reference") # L01:015
	cur.execute("DROP TABLE IF EXISTS datenqualitaet_external_reference") # L01:016
	cur.execute("DROP TABLE IF EXISTS era_external_reference") # L01:017
	cur.execute("DROP TABLE IF EXISTS external_nomenclature_external_reference") # L01:018
	cur.execute("DROP TABLE IF EXISTS face_external_reference") # L01:019
	cur.execute("DROP TABLE IF EXISTS discovery_method_external_reference") # L01:020
	cur.execute("DROP TABLE IF EXISTS form_aufsicht_external_reference") # L01:021
	cur.execute("DROP TABLE IF EXISTS form_querschnitt_external_reference") # L01:022
	cur.execute("DROP TABLE IF EXISTS geographical_unit_external_reference") # L01:023
	cur.execute("DROP TABLE IF EXISTS manufacture_external_reference") # L01:024
	cur.execute("DROP TABLE IF EXISTS material_external_reference") # L01:025
	cur.execute("DROP TABLE IF EXISTS modern_state_external_reference") # L01:026
	cur.execute("DROP TABLE IF EXISTS object_category_external_reference") # L01:027
	cur.execute("DROP TABLE IF EXISTS organisation_external_reference") # L01:028
	cur.execute("DROP TABLE IF EXISTS peculiarity_of_production_external_reference") # L01:029
	cur.execute("DROP TABLE IF EXISTS region_category_external_reference") # L01:030
	cur.execute("DROP TABLE IF EXISTS secondary_treatment_external_reference") # L01:031
	cur.execute("DROP TABLE IF EXISTS wear_external_reference") # L01:032
	cur.execute("DROP TABLE IF EXISTS modern_person_external_reference") # L01:033
	cur.execute("DROP TABLE IF EXISTS primary_source_document_manufacture_external_reference") # L01:034
	cur.execute("DROP TABLE IF EXISTS primary_source_document_type_external_reference") # L01:035
	cur.execute("DROP TABLE IF EXISTS publication_type_external_reference") # L01:036
	cur.execute("DROP TABLE IF EXISTS find_category_external_reference") # L01:037
	cur.execute("DROP TABLE IF EXISTS other_object_type") # L01:038
	cur.execute("DROP TABLE IF EXISTS other_object_name") # L01:039
	cur.execute("DROP TABLE IF EXISTS archaeological_event") # L01:040
	cur.execute("DROP TABLE IF EXISTS person_muenzadministration") # L01:041
	cur.execute("DROP TABLE IF EXISTS bibliography") # L01:042
	cur.execute("DROP TABLE IF EXISTS primary_source_document") # L01:043
	cur.execute("DROP TABLE IF EXISTS data_source_junction") # L01:044
	cur.execute("DROP TABLE IF EXISTS art_der_fundstelle_category_external_reference") # L01:045
	cur.execute("DROP TABLE IF EXISTS biblio_junction_detaillierungsgrad_external_reference") # L01:046
	cur.execute("DROP TABLE IF EXISTS prim_source_doc_informative_value_external_reference") # L01:047

	print("L01-tables dropped")
	return