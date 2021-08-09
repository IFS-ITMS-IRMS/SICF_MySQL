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

def create_tables_l05():

	# L05:001
	cur.execute("""
				CREATE TABLE authority_name_external_reference(

				id_authority_name_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_authority_name INT,
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

				FOREIGN KEY (id_authority_name)
					REFERENCES authority_name(id_authority_name),

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

	# L05:002
	cur.execute("""
				CREATE TABLE mint_name_external_reference(

				id_mint_name_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_mint_name INT,
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

				FOREIGN KEY (id_mint_name)
					REFERENCES mint_name(id_mint_name),

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

	# L05:003
	cur.execute("""
				CREATE TABLE ruler_name_external_reference(

				id_ruler_name_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_ruler_name INT,
				id_external_reference_data_source INT,
				external_reference VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),

				FOREIGN KEY (id_ruler_name)
					REFERENCES ruler_name(id_ruler_name),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

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
	
	# L05:004
	cur.execute("""
				CREATE TABLE commune_section_external_reference(

				id_commune_section_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_commune_section INT,
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

				FOREIGN KEY (id_commune_section)
					REFERENCES commune_section(id_commune_section),

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
	
	# L05:005
	cur.execute("""
				CREATE TABLE fundstelle_ort_lieu_external_shorthand(

				id_fundstelle_ort_lieu_external_shorthand INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_fundstelle_ort_lieu INT,
				id_organisation INT,
				external_shorthand_fundstelle_ort_lieu VARCHAR(255),
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

				FOREIGN KEY (id_fundstelle_ort_lieu)
					REFERENCES fundstelle_ort_lieu(id_fundstelle_ort_lieu),

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
	
	# L05:006
	cur.execute("""
				CREATE TABLE fundstelle_ort_lieu_external_reference(

				id_fundstelle_ort_lieu_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_fundstelle_ort_lieu INT,
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

				FOREIGN KEY (id_fundstelle_ort_lieu)
					REFERENCES fundstelle_ort_lieu(id_fundstelle_ort_lieu),

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

	# L05:007
	cur.execute("""
				CREATE TABLE fundstelle_flur_lieu_dit(

				id_fundstelle_flur_lieu_dit INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_fundstelle_ort_lieu INT,
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				name_other VARCHAR(255),
				parzellennummern VARCHAR(255),
				katasternummern VARCHAR(255),
				date_from DATE,
				date_to DATE,
				long_ch_lv95_e FLOAT,
				lat_ch_lv95_n FLOAT,
				altitude_ch FLOAT,
				polygon VARCHAR(255),
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

				FOREIGN KEY (id_fundstelle_ort_lieu)
					REFERENCES fundstelle_ort_lieu(id_fundstelle_ort_lieu),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L05:008
	cur.execute("""
				CREATE TABLE person_muenzadministration_name(

				id_person_muenzadministration_name INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_person_muenzadministration INT,
				id_function_table INT,
				id_authority_name INT,
				id_mint_name INT,
				id_place INT,
				name_german VARCHAR(255),
				name_german_alternative VARCHAR(255),
				name_french VARCHAR(255),
				name_french_alternative VARCHAR(255),
				name_italian VARCHAR(255),
				name_italian_alternative VARCHAR(255),
				name_english VARCHAR(255),
				name_english_alternative VARCHAR(255),
				active_from DATE,
				active_to DATE,
				active_post DATE,
				active_ante DATE,
				active_text_german VARCHAR(255),
				active_text_french VARCHAR(255),
				active_text_italian VARCHAR(255),
				active_text_english VARCHAR(255),
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

				FOREIGN KEY (id_person_muenzadministration)
					REFERENCES person_muenzadministration(id_person_muenzadministration),

				FOREIGN KEY (id_function_table)
					REFERENCES function_table(id_function_table),

				FOREIGN KEY (id_authority_name)
					REFERENCES authority_name(id_authority_name),

				FOREIGN KEY (id_mint_name)
					REFERENCES mint_name(id_mint_name),

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

	# L05:009
	cur.execute("""
				CREATE TABLE period_ruler_junction(

				id_period_ruler_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_period INT,
				id_ruler_name INT,
				comment_internal VARCHAR(255),
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_period)
					REFERENCES period(id_period),

				FOREIGN KEY (id_ruler_name)
					REFERENCES ruler_name(id_ruler_name),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L05:010
	cur.execute("""
				CREATE TABLE period_mint_junction(

				id_period_mint_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_period INT,
				id_mint_name INT,
				comment_internal VARCHAR(255),
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_period)
					REFERENCES period(id_period),

				FOREIGN KEY (id_mint_name)
					REFERENCES mint_name(id_mint_name),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L05:011
	cur.execute("""
				CREATE TABLE period_external_reference(

				id_period_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_period INT,
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

				FOREIGN KEY (id_period)
					REFERENCES period(id_period),

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

	print("L05-tables created")

	return
