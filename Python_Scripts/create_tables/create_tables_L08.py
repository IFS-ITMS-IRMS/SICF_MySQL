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

def create_tables_l08():

	# L08:001
	cur.execute("""
				CREATE TABLE container_fremde_id(

				id_container_fremde_id INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_container INT,
				id_organisation INT,
				id_modern_person INT,
				fremde_id  VARCHAR(255),
				date_fremde_id_last_check_active DATE,
				date_fremde_id_inactive DATE,
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_container)
					REFERENCES container(id_container),

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

	# L08:002
	cur.execute("""
				CREATE TABLE container_inventory_number(

				id_container_inventory_number INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_container INT,
				id_organisation INT,
				id_modern_person INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				fundnummer VARCHAR(255),
				inventory_number VARCHAR(255),
				bearbeitungsnummer VARCHAR(255),
				fundkomplex VARCHAR(255),
				position VARCHAR(255),
				archaeological_details_remark_german VARCHAR(255),
				archaeological_details_remark_french VARCHAR(255),
				archaeological_details_remark_italian VARCHAR(255),
				archaeological_details_remark_english VARCHAR(255),
				remark_public_german VARCHAR(255),
				remark_public_french VARCHAR(255),
				remark_public_italian VARCHAR(255),
				remark_public_english VARCHAR(255),
				remark_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_container)
					REFERENCES container(id_container),

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

	# L08:003
	cur.execute("""
				CREATE TABLE container_aufbewahrer(

				id_container_aufbewahrer INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				container_aufbewahrer_active_flag BOOLEAN,
				id_container INT,
				id_organisation INT,
				id_modern_person INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				container_aufbewahrer_qualifier BOOLEAN,
				remark_public_german VARCHAR(255),
				remark_public_french VARCHAR(255),
				remark_public_italian VARCHAR(255),
				remark_public_english VARCHAR(255),
				remark_internal VARCHAR(255),
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_container)
					REFERENCES container(id_container),

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

	# L08:004
	cur.execute("""
				CREATE TABLE container_container_material_junction(

				id_container_container_material_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_container INT,
				id_container_material INT,
				container_material_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_container)
					REFERENCES container(id_container),

				FOREIGN KEY (id_container_material)
					REFERENCES container_material(id_container_material),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L08:005
	cur.execute("""
				CREATE TABLE container_external_reference(

				id_container_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_container INT,
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

				FOREIGN KEY (id_container)
					REFERENCES container(id_container),

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

	# L08:006
	cur.execute("""
				CREATE TABLE find_object_fremde_id(

				id_find_object_fremde_id INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
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

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

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

	# L08:007
	cur.execute("""
				CREATE TABLE find_object_inventory_number(

				id_find_object_inventory_number INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_organisation INT,
				id_modern_person INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				fundnummer VARCHAR(255),
				inventory_number VARCHAR(255),
				bearbeitungsnummer VARCHAR(255),
				fundkomplex VARCHAR(255),
				position VARCHAR(255),
				archaeological_details_remark_german VARCHAR(255),
				archaeological_details_remark_french VARCHAR(255),
				archaeological_details_remark_italian VARCHAR(255),
				archaeological_details_remark_english VARCHAR(255),
				remark_public_german VARCHAR(255),
				remark_public_french VARCHAR(255),
				remark_public_italian VARCHAR(255),
				remark_public_english VARCHAR(255),
				remark_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

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

	# L08:008
	cur.execute("""
				CREATE TABLE find_object_finder(

				id_find_object_finder INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_organisation_name INT,
				id_modern_person_name INT,
				find_object_finder_qualifier BOOLEAN,
				remark_public_german VARCHAR(255),
				remark_public_french VARCHAR(255),
				remark_public_italian VARCHAR(255),
				remark_public_english VARCHAR(255),
				remark_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (id_organisation_name)
					REFERENCES organisation_name(id_organisation_name),

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

	# L08:009
	cur.execute("""
				CREATE TABLE find_object_bringer(

				id_find_object_bringer INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_organisation_name INT,
				id_modern_person_name INT,
				find_object_bringer_qualifier BOOLEAN,
				remark_public_german VARCHAR(255),
				remark_public_french VARCHAR(255),
				remark_public_italian VARCHAR(255),
				remark_public_english VARCHAR(255),
				remark_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (id_organisation_name)
					REFERENCES organisation_name(id_organisation_name),

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

	# L08:010
	cur.execute("""
				CREATE TABLE find_object_aufbewahrer(

				id_find_object_aufbewahrer INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				find_object_aufbewahrer_active_flag BOOLEAN,
				id_find_object INT,
				id_organisation INT,
				id_modern_person INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				find_object_aufbewahrer_qualifier BOOLEAN,
				remark_public_german VARCHAR(255),
				remark_public_french VARCHAR(255),
				remark_public_italian VARCHAR(255),
				remark_public_english VARCHAR(255),
				remark_internal VARCHAR(255),
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

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

	# L08:011
	cur.execute("""
				CREATE TABLE find_object_bearbeiter(

				id_find_object_bearbeiter INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_modern_person_name INT,
				id_modern_person_affiliation INT,
				id_organisation_name INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				find_object_bearbeiter_qualifier BOOLEAN,
				remark_public_german VARCHAR(255),
				remark_public_french VARCHAR(255),
				remark_public_italian VARCHAR(255),
				remark_public_english VARCHAR(255),
				remark_internal VARCHAR(255),
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (id_modern_person_name)
					REFERENCES modern_person_name(id_modern_person_name),

				FOREIGN KEY (id_modern_person_affiliation)
					REFERENCES modern_person_affiliation(id_modern_person_affiliation),

				FOREIGN KEY (id_organisation_name)
					REFERENCES organisation_name(id_organisation_name),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L08:012
	cur.execute("""
				CREATE TABLE find_object_peculiarity_of_production_junction(

				id_find_object_peculiarity_of_production_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_peculiarity_of_production INT,
				peculiarity_of_production_qualifier BOOLEAN,
				peculiarity_of_production_id_face INT,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (id_peculiarity_of_production)
					REFERENCES peculiarity_of_production(id_peculiarity_of_production),

				FOREIGN KEY (peculiarity_of_production_id_face)
					REFERENCES face(id_face),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L08:013
	cur.execute("""
				CREATE TABLE find_object_secondary_treatment_junction(

				id_find_object_secondary_treatment_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_secondary_treatment INT,
				secondary_treatment_qualifier BOOLEAN,
				secondary_treatment_id_face INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (id_secondary_treatment)
					REFERENCES secondary_treatment(id_secondary_treatment),

				FOREIGN KEY (secondary_treatment_id_face)
					REFERENCES face(id_face),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L08:014
	cur.execute("""
				CREATE TABLE find_object_conservation_state_junction(

				id_find_object_conservation_state_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_conservation_state INT,
				conservation_state_qualifier BOOLEAN,
				conservation_state_id_face INT,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (id_conservation_state)
					REFERENCES conservation_state(id_conservation_state),

				FOREIGN KEY (conservation_state_id_face)
					REFERENCES face(id_face),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L08:015
	cur.execute("""
				CREATE TABLE find_object_external_reference(

				id_find_object_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
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

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

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

	# L08:016
	cur.execute("""
				CREATE TABLE coin(

				id_coin INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				authority_remark_german TEXT,
				authority_remark_french TEXT,
				authority_remark_italian TEXT,
				authority_remark_english TEXT,
				issuer_portrait_remark_german TEXT,
				issuer_portrait_remark_french TEXT,
				issuer_portrait_remark_italian TEXT,
				issuer_portrait_remark_english TEXT,
				mintmaster_remark_german TEXT,
				mintmaster_remark_french TEXT,
				mintmaster_remark_italian TEXT,
				mintmaster_remark_english TEXT,
				mint_remark_german TEXT,
				mint_remark_french TEXT,
				mint_remark_italian TEXT,
				mint_remark_english TEXT,
				denomination_remark_german TEXT,
				denomination_remark_french TEXT,
				denomination_remark_italian TEXT,
				denomination_remark_english TEXT,
				type_remark_german TEXT,
				type_remark_french TEXT,
				type_remark_italian TEXT,
				type_remark_english TEXT,
				obverse_mint_mark_german TEXT,
				obverse_mint_mark_french TEXT,
				obverse_mint_mark_italian TEXT,
				obverse_mint_mark_english TEXT,
				reverse_mint_mark_german TEXT,
				reverse_mint_mark_french TEXT,
				reverse_mint_mark_italian TEXT,
				reverse_mint_mark_english TEXT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L08:017
	cur.execute("""
				CREATE TABLE other_object(

				id_other_object INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_other_object_category INT,
				issuer_portrait_remark_german TEXT,
				issuer_portrait_remark_french TEXT,
				issuer_portrait_remark_italian TEXT,
				issuer_portrait_remark_english TEXT,
				location_remark_german TEXT,
				location_remark_french TEXT,
				location_remark_italian TEXT,
				location_remark_english TEXT,
				other_object_type_remark_german TEXT,
				other_object_type_remark_french TEXT,
				other_object_type_remark_italian TEXT,
				other_object_type_remark_english TEXT,
				other_object_name_remark_german TEXT,
				other_object_name_remark_french TEXT,
				other_object_name_remark_italian TEXT,
				other_object_name_remark_english TEXT,
				occasion_german TEXT,
				occasion_french TEXT,
				occasion_italian TEXT,
				occasion_english TEXT,
				obverse_signatures_german TEXT,
				obverse_signatures_french TEXT,
				obverse_signatures_italian TEXT,
				obverse_signatures_english TEXT,
				reverse_signatures_german TEXT,
				reverse_signatures_french TEXT,
				reverse_signatures_italian TEXT,
				reverse_signatures_english TEXT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (id_other_object_category)
					REFERENCES other_object_category(id_other_object_category),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L08:018
	cur.execute("""
				CREATE TABLE find_object_period_junction(

				id_find_object_period_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_period INT,
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (id_period)
					REFERENCES period(id_period),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L08:019
	cur.execute("""
				CREATE TABLE find_object_biblio_junction(

				id_find_object_biblio_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_biblio_citation INT,
				id_bibliography INT,
				id_biblio_junction_type INT,
				id_biblio_junction_boilerplate INT,
				archaeological_id_biblio_junction_detaillierungsgrad INT,
				numismatic_id_biblio_junction_detaillierungsgrad INT,
				text_german VARCHAR(255),
				text_french VARCHAR(255),
				text_italian VARCHAR(255),
				text_english VARCHAR(255),
				remark_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (id_biblio_citation)
					REFERENCES biblio_citation(id_biblio_citation),

				FOREIGN KEY (id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (id_biblio_junction_type)
					REFERENCES biblio_junction_type(id_biblio_junction_type),

				FOREIGN KEY (id_biblio_junction_boilerplate)
					REFERENCES biblio_junction_boilerplate(id_biblio_junction_boilerplate),

				FOREIGN KEY (archaeological_id_biblio_junction_detaillierungsgrad)
					REFERENCES biblio_junction_detaillierungsgrad(id_biblio_junction_detaillierungsgrad),

				FOREIGN KEY (numismatic_id_biblio_junction_detaillierungsgrad)
					REFERENCES biblio_junction_detaillierungsgrad(id_biblio_junction_detaillierungsgrad),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L08:020
	cur.execute("""
				CREATE TABLE find_object_primary_source_document_junction(

				id_find_object_primary_source_document_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
				id_primary_source_document_citation INT,
				id_primary_source_document INT,
				id_biblio_junction_type INT,
				id_primary_source_document_informative_value INT,
				archaeological_id_biblio_junction_detaillierungsgrad INT,
				numismatic_id_biblio_junction_detaillierungsgrad INT,
				text_german VARCHAR(255),
				text_french VARCHAR(255),
				text_italian VARCHAR(255),
				text_english VARCHAR(255),
				remark_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

				FOREIGN KEY (id_primary_source_document_citation)
					REFERENCES primary_source_document_citation(id_primary_source_document_citation),

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (id_biblio_junction_type)
					REFERENCES biblio_junction_type(id_biblio_junction_type),

				FOREIGN KEY (id_primary_source_document_informative_value)
					REFERENCES primary_source_document_informative_value(id_primary_source_document_informative_value),

				FOREIGN KEY (archaeological_id_biblio_junction_detaillierungsgrad)
					REFERENCES biblio_junction_detaillierungsgrad(id_biblio_junction_detaillierungsgrad),

				FOREIGN KEY (numismatic_id_biblio_junction_detaillierungsgrad)
					REFERENCES biblio_junction_detaillierungsgrad(id_biblio_junction_detaillierungsgrad),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L08:021
	cur.execute("""
				CREATE TABLE remark_user_find_object_numeric(

				id_remark_user_find_object_numeric INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
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

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

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

	# L08:022
	cur.execute("""
				CREATE TABLE remark_user_find_object_text(

				id_remark_user_find_object_text INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_object INT,
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

				FOREIGN KEY (id_find_object)
					REFERENCES find_object(id_find_object),

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

	print("L08-tables created")

	return
