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

def create_tables_l02():

	# L02:001
	cur.execute("""
				CREATE TABLE denomination(

				id_denomination INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				denomination_acronym VARCHAR(255),
				value_german VARCHAR(255),
				value_german_alternative VARCHAR(255),
				value_french VARCHAR(255),
				value_french_alternative VARCHAR(255),
				value_italian VARCHAR(255),
				value_italian_alternative VARCHAR(255),
				value_english VARCHAR(255),
				value_english_alternative VARCHAR(255),
				id_numismatic_time_slice_from INT,
				id_numismatic_time_slice_to INT,
				id_era_from INT,
				id_era_to INT,
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				nomisma_org_id VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_numismatic_time_slice_from)
					REFERENCES numismatic_time_slice(id_numismatic_time_slice),

				FOREIGN KEY (id_numismatic_time_slice_to)
					REFERENCES numismatic_time_slice(id_numismatic_time_slice),

				FOREIGN KEY (id_era_from)
					REFERENCES era(id_era),

				FOREIGN KEY (id_era_to)
					REFERENCES era(id_era),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)
	""")

	# L02:002
	cur.execute("""
				CREATE TABLE place(

				id_place INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				official_language_id_language INT,
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				name_other VARCHAR(255),
				id_modern_region INT,
				id_modern_state INT,
				lat_wgs84 FLOAT,
				long_wgs84 FLOAT,
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				pleiades_id INT,
				geonames_id INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (official_language_id_language)
					REFERENCES language(id_language),

				FOREIGN KEY (id_modern_region)
					REFERENCES modern_region(id_modern_region),

				FOREIGN KEY (id_modern_state)
					REFERENCES modern_state(id_modern_state),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:003
	cur.execute("""
				CREATE TABLE field_of_numismatics_external_reference(

				id_field_of_numismatics_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_field_of_numismatics INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_field_of_numismatics)
					REFERENCES field_of_numismatics(id_field_of_numismatics),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:004
	cur.execute("""
				CREATE TABLE modern_person_name_external_reference(

				id_modern_person_name_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_modern_person_name INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_modern_person_name)
					REFERENCES modern_person_name(id_modern_person_name),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:005
	cur.execute("""
				CREATE TABLE modern_region_external_reference(

				id_modern_region_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_modern_region INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_modern_region)
					REFERENCES modern_region(id_modern_region),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:006
	cur.execute("""
				CREATE TABLE numismatic_time_slice_external_reference(

				id_numismatic_time_slice_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_numismatic_time_slice INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_numismatic_time_slice)
					REFERENCES numismatic_time_slice(id_numismatic_time_slice),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:007
	cur.execute("""
				CREATE TABLE district(
				
				id_district INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				fso_code INT,
				district_active_flag BOOLEAN,
				official_language_id_language INT,
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				name_other VARCHAR(255),
				id_modern_region INT,
				id_modern_state INT,
				fso_mutation_start VARCHAR(255),
				fso_mutation_end VARCHAR(255),
				date_from DATE,
				date_to DATE,
				polygon VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (official_language_id_language)
					REFERENCES language(id_language),

				FOREIGN KEY (id_modern_region)
					REFERENCES modern_region(id_modern_region),

				FOREIGN KEY (id_modern_state)
					REFERENCES modern_state(id_modern_state),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:008
	cur.execute("""
				CREATE TABLE ruler_external_reference(

				id_ruler_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_ruler INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_ruler)
					REFERENCES ruler(id_ruler),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:009
	cur.execute("""
				CREATE TABLE type_external_reference(

				id_type_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_type INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_type)
					REFERENCES type(id_type),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")
	
	# L02:010
	cur.execute("""
				CREATE TABLE other_object_type_external_reference(

				id_other_object_type_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object_type INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_other_object_type)
					REFERENCES other_object_type(id_other_object_type),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:011
	cur.execute("""
				CREATE TABLE other_object_name_external_reference(

				id_other_object_name_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object_name INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_other_object_name)
					REFERENCES other_object_name(id_other_object_name),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")
	
	# L02:012
	cur.execute("""
				CREATE TABLE archaeological_event_fremde_id(

				id_archaeological_event_fremde_id INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_archaeological_event INT,
				id_organisation INT,
				id_modern_person INT,
				fremde_id VARCHAR(255),
				date_fremde_id_last_check_active DATE,
				date_fremde_id_inactive DATE,
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_archaeological_event)
					REFERENCES archaeological_event(id_archaeological_event),

				FOREIGN KEY (id_organisation)
					REFERENCES organisation(id_organisation),

				FOREIGN KEY (id_modern_person)
					REFERENCES modern_person(id_modern_person),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:013
	cur.execute("""
				CREATE TABLE archaeological_event_external_reference(

				id_archaeological_event_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_archaeological_event INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_archaeological_event)
					REFERENCES archaeological_event(id_archaeological_event),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:014
	cur.execute("""
				CREATE TABLE arch_event_new_arch_event_old_relation(

				id_arch_event_new_arch_event_old_relation INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_archaeological_event INT,
				old_id_archaeological_event INT,
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_archaeological_event)
					REFERENCES archaeological_event(id_archaeological_event),

				FOREIGN KEY (old_id_archaeological_event)
					REFERENCES archaeological_event(id_archaeological_event),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:015
	cur.execute("""
				CREATE TABLE person_muenzadministration_external_reference(

				id_person_muenzadministration_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_person_muenzadministration INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_person_muenzadministration)
					REFERENCES person_muenzadministration(id_person_muenzadministration),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:016
	cur.execute("""
				CREATE TABLE art_der_fundstelle_type_external_reference(

				id_art_der_fundstelle_type_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_art_der_fundstelle_type INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_art_der_fundstelle_type)
					REFERENCES art_der_fundstelle_type(id_art_der_fundstelle_type),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:017
	cur.execute("""
				CREATE TABLE art_der_fundstelle_detail(

				id_art_der_fundstelle_detail INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_art_der_fundstelle_type INT,
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				nomisma_org_id VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_art_der_fundstelle_type)
					REFERENCES art_der_fundstelle_type(id_art_der_fundstelle_type),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:018
	cur.execute("""
				CREATE TABLE bibliography_language_junction(

				id_bibliography_language_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_bibliography INT,
				id_language INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (id_language)
					REFERENCES language(id_language),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:019
	cur.execute("""
				CREATE TABLE bibliography_bibliography_relation(

				id_bibliography_bibliography_relation INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_bibliography INT,
				part_id_bibliography INT,
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (part_id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:020
	cur.execute("""
				CREATE TABLE bibliography_external_reference(

				id_bibliography_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_bibliography INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:021
	cur.execute("""
				CREATE TABLE biblio_citation(

				id_biblio_citation INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_bibliography INT,
				pages VARCHAR(255),
				numbers VARCHAR(255),
				figures VARCHAR(255),
				plates VARCHAR(255),
				quotation_text VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:022
	cur.execute("""
				CREATE TABLE primary_source_document_aufbewahrer(

				id_primary_source_document_aufbewahrer INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				primary_source_document_aufbewahrer_active_flag BOOLEAN,
				id_primary_source_document INT,
				id_organisation INT,
				id_modern_person INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				archival_code VARCHAR(255),
				archival_code_remark_german VARCHAR(255),
				archival_code_remark_french VARCHAR(255),
				archival_code_remark_italian VARCHAR(255),
				archival_code_remark_english VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (id_organisation)
					REFERENCES organisation(id_organisation),

				FOREIGN KEY (id_modern_person)
					REFERENCES modern_person(id_modern_person),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:023
	cur.execute("""
				CREATE TABLE primary_source_document_author_junction(

				id_primary_source_document_author_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document INT,
				id_modern_person_name INT,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (id_modern_person_name)
					REFERENCES modern_person_name(id_modern_person_name),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:024
	cur.execute("""
				CREATE TABLE primary_source_document_informative_value_junction(

				id_primary_source_document_informative_value_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document INT,
				id_primary_source_document_informative_value INT,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (id_primary_source_document_informative_value)
					REFERENCES primary_source_document_informative_value(id_primary_source_document_informative_value),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:025
	cur.execute("""
				CREATE TABLE primary_source_document_language_junction(

				id_primary_source_document_language_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document INT,
				id_language INT,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (id_language)
					REFERENCES language(id_language),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:026
	cur.execute("""
				CREATE TABLE primary_source_document_manufacture_junction(

				id_primary_source_document_manufacture_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document INT,
				id_primary_source_document_manufacture INT,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (id_primary_source_document_manufacture)
					REFERENCES primary_source_document_manufacture(id_primary_source_document_manufacture),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:027
	cur.execute("""
				CREATE TABLE primary_source_document_external_reference(

				id_primary_source_document_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (id_external_reference_data_source)
					REFERENCES external_reference_data_source(id_external_reference_data_source),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:028
	cur.execute("""
				CREATE TABLE prim_source_doc_prim_source_doc_relation(

				id_prim_source_doc_prim_source_doc_relation INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document INT,
				part_id_primary_source_document INT,
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (part_id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:029
	cur.execute("""
				CREATE TABLE primary_source_document_citation(

				id_primary_source_document_citation INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document INT,
				pages VARCHAR(255),
				numbers VARCHAR(255),
				figures VARCHAR(255),
				plates VARCHAR(255),
				summary_german VARCHAR(255),
				summary_french VARCHAR(255),
				summary_italian VARCHAR(255),
				summary_english VARCHAR(255),
				quotation_text VARCHAR(255),
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:030
	cur.execute("""
				CREATE TABLE remark_user_bibliography_text(

				id_remark_user_bibliography_text INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_bibliography INT,
				id_user INT,
				id_organisation INT,
				id_remark_user_tag INT,
				value VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (id_organisation)
					REFERENCES organisation(id_organisation),

				FOREIGN KEY (id_remark_user_tag)
					REFERENCES remark_user_tag(id_remark_user_tag),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L02:031
	cur.execute("""
				CREATE TABLE remark_user_bibliography_numeric(

				id_remark_user_bibliography_numeric INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_bibliography INT,
				id_user INT,
				id_organisation INT,
				id_remark_user_tag INT,
				value FLOAT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (id_organisation)
					REFERENCES organisation(id_organisation),

				FOREIGN KEY (id_remark_user_tag)
					REFERENCES remark_user_tag(id_remark_user_tag),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	print("L02-tables created")

	return
