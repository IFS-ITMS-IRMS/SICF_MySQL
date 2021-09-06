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

def create_tables_l04():

	# L04:001
	cur.execute("""
				CREATE TABLE authority_name(

				id_authority_name INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_authority INT,
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				date_from DATE,
				date_to DATE,
				id_numismatic_time_slice_from INT,
				id_numismatic_time_slice_to INT,
				id_era INT,
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

				FOREIGN KEY (id_authority)
					REFERENCES authority(id_authority),

				FOREIGN KEY (id_numismatic_time_slice_from)
					REFERENCES numismatic_time_slice(id_numismatic_time_slice),

				FOREIGN KEY (id_numismatic_time_slice_to)
					REFERENCES numismatic_time_slice(id_numismatic_time_slice),

				FOREIGN KEY (id_era)
					REFERENCES era(id_era),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)
	""")

	# L04:002
	cur.execute("""
				CREATE TABLE mint_name(

				id_mint_name INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_mint INT,
				mint_acronym VARCHAR(255),
				order_number INT,
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				id_numismatic_time_slice_from INT,
				id_numismatic_time_slice_to INT,
				id_era INT,
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

				FOREIGN KEY (id_mint)
					REFERENCES mint(id_mint),

				FOREIGN KEY (id_numismatic_time_slice_from)
					REFERENCES numismatic_time_slice(id_numismatic_time_slice),

				FOREIGN KEY (id_numismatic_time_slice_to)
					REFERENCES numismatic_time_slice(id_numismatic_time_slice),

				FOREIGN KEY (id_era)
					REFERENCES era(id_era),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L04:003
	cur.execute("""
				CREATE TABLE ruler_name(

				id_ruler_name INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_ruler INT,
				id_authority INT,
				name_german VARCHAR(255),
				name_german_alternative VARCHAR(255),
				name_french VARCHAR(255),
				name_french_alternative VARCHAR(255),
				name_italian VARCHAR(255),
				name_italian_alternative VARCHAR(255),
				name_english VARCHAR(255),
				name_english_alternative VARCHAR(255),
				reign_from DATE,
				reign_to DATE,
				reign_text_german VARCHAR(255),
				reign_text_french VARCHAR(255),
				reign_text_italian VARCHAR(255),
				reign_text_english VARCHAR(255),
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

				FOREIGN KEY (id_ruler)
					REFERENCES ruler(id_ruler),

				FOREIGN KEY (id_authority)
					REFERENCES authority(id_authority),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L04:004
	cur.execute("""
				CREATE TABLE authority_external_reference(

				id_authority_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_authority INT,
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

				FOREIGN KEY (id_authority)
					REFERENCES authority(id_authority),

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

	# L04:005
	cur.execute("""
				CREATE TABLE mint_external_reference(

				id_mint_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_mint INT,
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

				FOREIGN KEY (id_mint)
					REFERENCES mint(id_mint),

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

	# L04:006
	cur.execute("""
				CREATE TABLE modern_person_affiliation_external_reference(

				id_modern_person_affiliation_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_modern_person_affiliation INT,
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

				FOREIGN KEY (id_modern_person_affiliation)
					REFERENCES modern_person_affiliation(id_modern_person_affiliation),

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

	# L04:007
	cur.execute("""
				CREATE TABLE organisation_name_external_reference(

				id_organisation_name_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_organisation_name INT,
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

				FOREIGN KEY (id_organisation_name)
					REFERENCES organisation_name(id_organisation_name),

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
	
	# L04:008
	cur.execute("""
				CREATE TABLE commune_external_reference(

				id_commune_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_commune INT,
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

				FOREIGN KEY (id_commune)
					REFERENCES commune(id_commune),

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
	
	# L04:009
	cur.execute("""
				CREATE TABLE commune_section(

				id_commune_section INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_commune INT,
				polygon VARCHAR(255),
				commune_section_shorthand VARCHAR(255),
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				name_other VARCHAR(255),
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

				FOREIGN KEY (id_commune)
					REFERENCES commune(id_commune),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L04:010
	cur.execute("""
				CREATE TABLE commune_external_shorthand(

				id_commune_external_shorthand INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_commune INT,
				id_organisation INT,
				external_shorthand_commune VARCHAR(255),
				date_from DATE,
				date_to DATE,
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

				FOREIGN KEY (id_commune)
					REFERENCES commune(id_commune),

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

	# L04:011
	cur.execute("""
				CREATE TABLE commune_new_commune_old_relation(

				id_commune_new_commune_old_relation INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				new_id_commune INT,
				old_id_commune INT,
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

				FOREIGN KEY (new_id_commune)
					REFERENCES commune(id_commune),

				FOREIGN KEY (old_id_commune)
					REFERENCES commune(id_commune),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")
	
	# L04:012
	cur.execute("""
				CREATE TABLE fundstelle_ort_lieu(

				id_fundstelle_ort_lieu INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_commune INT,
				fundstelle_ort_lieu_active_flag BOOLEAN,
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				name_other VARCHAR(255),
				long_ch_lv95_e FLOAT,
				lat_ch_lv95_n FLOAT,
				altitude_ch FLOAT,
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

				FOREIGN KEY (id_commune)
					REFERENCES commune(id_commune),

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

	# L04:013
	cur.execute("""
				CREATE TABLE period(

				id_period INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				period_tag VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				id_numismatic_time_slice_from INT,
				id_numismatic_time_slice_to INT,
				id_authority INT,
				data_provenance_id_organisation_name INT,
				data_provenance_id_modern_person_name INT,
				data_provenance_id_bibliography INT,
				data_provenance_time_stamp DATE,
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

				FOREIGN KEY (id_authority)
					REFERENCES authority(id_authority),

				FOREIGN KEY (data_provenance_id_organisation_name)
					REFERENCES organisation_name(id_organisation_name),

				FOREIGN KEY (data_provenance_id_modern_person_name)
					REFERENCES modern_person_name(id_modern_person_name),

				FOREIGN KEY (data_provenance_id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L04:014
	cur.execute("""
				CREATE TABLE primary_source_document_editor_junction(

				id_primary_source_document_editor_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document INT,
				id_organisation_name INT,
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

	# L04:015
	cur.execute("""
				CREATE TABLE user_modern_person_junction(

				id_user_modern_person_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_user INT,
				id_modern_person_affiliation INT,
				id_modern_person INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (id_modern_person_affiliation)
					REFERENCES modern_person_affiliation(id_modern_person_affiliation),

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

	# L04:016
	cur.execute("""
				CREATE TABLE  bibliography_editor_author_junction(

				id_bibliography_editor_author_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_bibliography INT,
				editor_flag BOOLEAN,
				id_modern_person_name INT,
				id_organisation_name INT,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_bibliography)
					REFERENCES bibliography(id_bibliography),

				FOREIGN KEY (id_modern_person_name)
					REFERENCES modern_person_name(id_modern_person_name),

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

	print("L04-tables created")

	return
