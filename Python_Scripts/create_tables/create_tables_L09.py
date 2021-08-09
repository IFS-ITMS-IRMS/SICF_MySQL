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

def create_tables_l09():

	# L09:001
	cur.execute("""
				CREATE TABLE coin_field_of_numismatics_junction(

				id_coin_field_of_numismatics_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_coin INT,
				id_field_of_numismatics INT,
				field_of_numismatics_qualifier BOOLEAN,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_coin)
					REFERENCES coin(id_coin),

				FOREIGN KEY (id_field_of_numismatics)
					REFERENCES field_of_numismatics(id_field_of_numismatics),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)
	""")

	# L09:002
	cur.execute("""
				CREATE TABLE coin_authority_junction(

				id_coin_authority_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_coin INT,
				id_authority_name INT,
				authority_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_coin)
					REFERENCES coin(id_coin),

				FOREIGN KEY (id_authority_name)
					REFERENCES authority_name(id_authority_name),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L09:003
	cur.execute("""
				CREATE TABLE coin_issuer_portrait_junction(

				id_coin_issuer_portrait_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_coin INT,
				issuer_id_ruler_name INT,
				portrait_id_ruler_name INT,
				issuer_portrait_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_coin)
					REFERENCES coin(id_coin),

				FOREIGN KEY (issuer_id_ruler_name)
					REFERENCES ruler_name(id_ruler_name),

				FOREIGN KEY (portrait_id_ruler_name)
					REFERENCES ruler_name(id_ruler_name),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L09:004
	cur.execute("""
				CREATE TABLE coin_mint_junction(

				id_coin_mint_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_coin INT,
				id_mint_name INT,
				mint_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_coin)
					REFERENCES coin(id_coin),

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

	# L09:005
	cur.execute("""
				CREATE TABLE coin_denomination_junction(

				id_coin_denomination_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_coin INT,
				id_denomination INT,
				denomination_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_coin)
					REFERENCES coin(id_coin),

				FOREIGN KEY (id_denomination)
					REFERENCES denomination(id_denomination),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L09:006
	cur.execute("""
				CREATE TABLE coin_type_junction(

				id_coin_type_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_coin INT,
				id_type INT,
				type_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_coin)
					REFERENCES coin(id_coin),

				FOREIGN KEY (id_type)
					REFERENCES type(id_type),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L09:007
	cur.execute("""
				CREATE TABLE coin_mintmaster_junction(

				id_coin_mintmaster_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_coin INT,
				mintmaster_id_person_muenzadministration_name INT,
				mintmaster_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_coin)
					REFERENCES coin(id_coin),

				FOREIGN KEY (mintmaster_id_person_muenzadministration_name)
					REFERENCES person_muenzadministration_name(id_person_muenzadministration_name),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L09:008
	cur.execute("""
				CREATE TABLE other_object_issuer_junction(

				id_other_object_issuer_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object INT,
				id_organisation_name INT,
				id_ruler_name INT,
				id_modern_person_name INT,
				issuer_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_other_object)
					REFERENCES other_object(id_other_object),

				FOREIGN KEY (id_organisation_name)
					REFERENCES organisation_name(id_organisation_name),

				FOREIGN KEY (id_ruler_name)
					REFERENCES ruler_name(id_ruler_name),

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

	# L09:009
	cur.execute("""
				CREATE TABLE other_object_portrait_junction(

				id_other_object_portrait_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object INT,
				id_ruler_name INT,
				id_modern_person_name INT,
				portrait_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_other_object)
					REFERENCES other_object(id_other_object),

				FOREIGN KEY (id_ruler_name)
					REFERENCES ruler_name(id_ruler_name),

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

	# L09:010
	cur.execute("""
				CREATE TABLE other_object_issuing_location_junction(

				id_other_object_issuing_location_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object INT,
				id_place INT,
				id_modern_region INT,
				id_modern_state INT,
				id_geographical_unit INT,
				issuing_location_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_other_object)
					REFERENCES other_object(id_other_object),

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

	# L09:011
	cur.execute("""
				CREATE TABLE other_object_producer_junction(

				id_other_object_producer_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object INT,
				id_person_muenzadministration_name INT,
				id_organisation_name INT,
				producer_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_other_object)
					REFERENCES other_object(id_other_object),

				FOREIGN KEY (id_person_muenzadministration_name)
					REFERENCES person_muenzadministration_name(id_person_muenzadministration_name),

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

	# L09:012
	cur.execute("""
				CREATE TABLE other_object_production_place_junction(

				id_other_object_production_place_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object INT,
				id_place INT,
				id_modern_region INT,
				id_modern_state INT,
				id_geographical_unit INT,
				production_place_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_other_object)
					REFERENCES other_object(id_other_object),

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

	# L09:013
	cur.execute("""
				CREATE TABLE other_object_type_junction(

				id_other_object_type_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object INT,
				id_other_object_type INT,
				other_object_type_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_other_object)
					REFERENCES other_object(id_other_object),

				FOREIGN KEY (id_other_object_type)
					REFERENCES other_object_type(id_other_object_type),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L09:014
	cur.execute("""
				CREATE TABLE other_object_name_junction(

				id_other_object_name_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object INT,
				id_other_object_name INT,
				other_object_name_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_other_object)
					REFERENCES other_object(id_other_object),

				FOREIGN KEY (id_other_object_name)
					REFERENCES other_object_name(id_other_object_name),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	print("L09-tables created")

	return
