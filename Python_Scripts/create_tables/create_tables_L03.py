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

def create_tables_l03():

	# L03:001
	cur.execute("""
				CREATE TABLE authority(

				id_authority INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				id_place INT,
				id_modern_region INT,
				id_modern_state INT,
				id_geographical_unit INT,
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

				FOREIGN KEY (id_place)
					REFERENCES place(id_place),

				FOREIGN KEY (id_modern_region)
					REFERENCES modern_region(id_modern_region),

				FOREIGN KEY (id_modern_state)
					REFERENCES modern_state(id_modern_state),

				FOREIGN KEY (id_geographical_unit)
					REFERENCES geographical_unit(id_geographical_unit),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)
	""")

	# L03:002
	cur.execute("""
				CREATE TABLE geographical_unit_part(

				id_geographical_unit_part INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_geographical_unit INT,
				id_modern_state INT,
				id_modern_region INT,
				id_place INT,
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_geographical_unit)
					REFERENCES geographical_unit(id_geographical_unit),

				FOREIGN KEY (id_modern_state)
					REFERENCES modern_state(id_modern_state),

				FOREIGN KEY (id_modern_region)
					REFERENCES modern_region(id_modern_region),

				FOREIGN KEY (id_place)
					REFERENCES place(id_place),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L03:003
	cur.execute("""
				CREATE TABLE mint(

				id_mint INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_place INT,
				id_modern_region INT,
				id_modern_state INT,
				id_geographical_unit INT,
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

				FOREIGN KEY (id_place)
					REFERENCES place(id_place),

				FOREIGN KEY (id_modern_region)
					REFERENCES modern_region(id_modern_region),

				FOREIGN KEY (id_modern_state)
					REFERENCES modern_state(id_modern_state),

				FOREIGN KEY (id_geographical_unit)
					REFERENCES geographical_unit(id_geographical_unit),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L03:004
	cur.execute("""
				CREATE TABLE modern_person_affiliation(

				id_modern_person_affiliation INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_modern_person INT,
				id_place INT,
				place_date_from DATE,
				place_date_to DATE,
				place_date_text_german VARCHAR(255),
				place_date_text_french VARCHAR(255),
				place_date_text_italian VARCHAR(255),
				place_date_text_english VARCHAR(255),
				id_organisation INT,
				organisation_date_from DATE,
				organisation_date_to DATE,
				organisation_date_text_german VARCHAR(255),
				organisation_date_text_french VARCHAR(255),
				organisation_date_text_italian VARCHAR(255),
				organisation_date_text_english VARCHAR(255),
				description_in_source VARCHAR(255),
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

				FOREIGN KEY (id_modern_person)
					REFERENCES modern_person(id_modern_person),

				FOREIGN KEY (id_place)
					REFERENCES place(id_place),

				FOREIGN KEY (id_organisation)
					REFERENCES organisation(id_organisation),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L03:005
	cur.execute("""
				CREATE TABLE organisation_name(

				id_organisation_name INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_organisation INT,
				name_main_entry_flag BOOLEAN,
				official_language_id_language INT,
				name_german VARCHAR(255),
				name_german_acronym VARCHAR(255),
				name_french VARCHAR(255),
				name_french_acronym VARCHAR(255),
				name_italian VARCHAR(255),
				name_italian_acronym VARCHAR(255),
				name_english VARCHAR(255),
				name_english_acronym VARCHAR(255),
				name_other VARCHAR(255),
				name_other_acronym VARCHAR(255),
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				id_place INT,
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				gnd_id INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_organisation)
					REFERENCES organisation(id_organisation),

				FOREIGN KEY (official_language_id_language)
					REFERENCES language(id_language),

				FOREIGN KEY (id_place)
					REFERENCES place(id_place),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L03:006
	cur.execute("""
				CREATE TABLE denomination_external_reference(

				id_denomination_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_denomination INT,
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

				FOREIGN KEY (id_denomination)
					REFERENCES denomination(id_denomination),

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

	# L03:007
	cur.execute("""
				CREATE TABLE place_external_reference(

				id_place_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_place INT,
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

				FOREIGN KEY (id_place)
					REFERENCES place(id_place),

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

	# L03:008
	cur.execute("""
				CREATE TABLE district_external_reference(

				id_district_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_district INT,
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

				FOREIGN KEY (id_district)
					REFERENCES district(id_district),

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
	
	# L03:009
	cur.execute("""
				CREATE TABLE commune(

				id_commune INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				fso_code INT,
				commune_active_flag BOOLEAN,
				official_language_id_language INT,
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				name_other VARCHAR(255),
				id_district INT,
				fso_mutation_start VARCHAR(255),
				fso_mutation_end VARCHAR(255),
				date_from DATE,
				date_to DATE,
				long_ch_lv95_e FLOAT,
				lat_ch_lv95_n FLOAT,
				altitude_ch FLOAT,
				lat_wgs84 FLOAT,
				long_wgs84 FLOAT,
				polygon VARCHAR(255),
				id_place INT,
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

				FOREIGN KEY (official_language_id_language)
					REFERENCES language(id_language),

				FOREIGN KEY (id_district)
					REFERENCES district(id_district),

				FOREIGN KEY (id_place)
					REFERENCES place(id_place),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L03:010
	cur.execute("""
				CREATE TABLE art_der_fundstelle_detail_external_reference(

				id_art_der_fundstelle_detail_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_art_der_fundstelle_detail INT,
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

				FOREIGN KEY (id_art_der_fundstelle_detail)
					REFERENCES art_der_fundstelle_detail(id_art_der_fundstelle_detail),

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

	# L03:011
	cur.execute("""
				CREATE TABLE bibliography_place_of_publication_junction(

				id_bibliography_place_of_publication_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_bibliography INT,
				id_place INT,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (id_place)
					REFERENCES place(id_place),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

 	# L03:012
	cur.execute("""
				CREATE TABLE primary_source_document_place_of_production_junction(

				id_primary_source_document_place_of_production_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document INT,
				id_place INT,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

				FOREIGN KEY (id_place)
					REFERENCES place(id_place),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

 	# L03:013
	cur.execute("""
				CREATE TABLE biblio_citation_external_reference(

				id_biblio_citation_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_biblio_citation INT,
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

				FOREIGN KEY (id_biblio_citation)
					REFERENCES biblio_citation(id_biblio_citation),

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

 	# L03:014
	cur.execute("""
				CREATE TABLE primary_source_document_aufbewahrer_external_reference(

				id_primary_source_document_aufbewahrer_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document_aufbewahrer INT,
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

				FOREIGN KEY (id_primary_source_document_aufbewahrer)
					REFERENCES primary_source_document_aufbewahrer(id_primary_source_document_aufbewahrer),

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

 	# L03:015
	cur.execute("""
				CREATE TABLE primary_source_document_citation_external_reference(

				id_primary_source_document_citation_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document_citation INT,
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

				FOREIGN KEY (id_primary_source_document_citation)
					REFERENCES primary_source_document_citation(id_primary_source_document_citation),

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

	print("L03-tables created")

	return
