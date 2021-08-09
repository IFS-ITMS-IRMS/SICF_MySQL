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

def create_tables_l00():

	# L00:001 - must be first to be created!
	cur.execute("""
				CREATE TABLE user(

				id_user INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255)

				)
	""")

	# L00:002 - must be second to be created!
	cur.execute("""
				CREATE TABLE data_source(

				id_data_source INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255)

				)

	""")

	# L00:003
	cur.execute("""
				CREATE TABLE modern_person(

				id_modern_person INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				date_birth DATE,
				date_death DATE,
				lived_post DATE,
				lived_ante DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:004
	cur.execute("""
				CREATE TABLE yes_no_unknown(

				id_yes_no_unknown INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255)

				)

	""")

	# L00:005
	cur.execute("""
				CREATE TABLE datenqualitaet(

				id_datenqualitaet INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				datenqualitaet_tag VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:006
	cur.execute("""
				CREATE TABLE bearbeitungsstand(

				id_bearbeitungsstand INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				bearbeitungsstand_tag VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:007
	cur.execute("""
				CREATE TABLE remark_user_tag(

				id_remark_user_tag INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				value VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:008
	cur.execute("""
				CREATE TABLE region_category(

				id_region_category INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:009
	cur.execute("""
				CREATE TABLE geographical_unit(

				id_geographical_unit INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				geographical_unit_acronym VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:010
	cur.execute("""
				CREATE TABLE primary_source_document_informative_value(

				id_primary_source_document_informative_value INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:011
	cur.execute("""
				CREATE TABLE era(

				id_era INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				era_acronym VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
				date_from DATE,
				date_to DATE,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:012
	cur.execute("""
				CREATE TABLE calendar(

				id_calendar INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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
				comment_public_german  VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal  VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:013
	cur.execute("""
				CREATE TABLE material(

				id_material INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				material_tag VARCHAR(255),
				value_german VARCHAR(255),
				value_german_alternative VARCHAR(255),
				value_french VARCHAR(255),
				value_french_alternative VARCHAR(255),
				value_italian VARCHAR(255),
				value_italian_alternative VARCHAR(255),
				value_english VARCHAR(255),
				value_english_alternative VARCHAR(255),
				chemical_composition VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:014
	cur.execute("""
				CREATE TABLE container_material(

				id_container_material INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				container_material_tag VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:015
	cur.execute("""
				CREATE TABLE manufacture(

				id_manufacture INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:016
	cur.execute("""
				CREATE TABLE peculiarity_of_production(

				id_peculiarity_of_production INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:017
	cur.execute("""
				CREATE TABLE secondary_treatment(

				id_secondary_treatment INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:018
	cur.execute("""
				CREATE TABLE conservation_state(

				id_conservation_state INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:019
	cur.execute("""
				CREATE TABLE external_nomenclature(

				id_external_nomenclature INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				nomisma_org_id VARCHAR(255)

				)

	""")

	# L00:020
	cur.execute("""
				CREATE TABLE discovery_method(

				id_discovery_method INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:021
	cur.execute("""
				CREATE TABLE art_der_fundstelle_category(

				id_art_der_fundstelle_category INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:022
	cur.execute("""
				CREATE TABLE find_category(

				id_find_category INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:023
	cur.execute("""
				CREATE TABLE object_category(

				id_object_category INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				shorthand_object_category VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:024
	cur.execute("""
				CREATE TABLE authenticity(

				id_authenticity INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:025
	cur.execute("""
				CREATE TABLE authenticity_interpretation(

				id_authenticity_interpretation INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:026
	cur.execute("""
				CREATE TABLE external_reference_data_source(

				id_external_reference_data_source INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
				data_source VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:027
	cur.execute("""
				CREATE TABLE wear(

				id_wear INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				wear_tag INT,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:028
	cur.execute("""
				CREATE TABLE corrosion(

				id_corrosion INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				corrosion_tag INT,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:029
	cur.execute("""
				CREATE TABLE face(

				id_face INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				shorthand_face VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				nomisma_org_id VARCHAR(255)

				)

	""")

	# L00:030
	cur.execute("""
				CREATE TABLE form_aufsicht(

				id_form_aufsicht INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:031
	cur.execute("""
				CREATE TABLE form_querschnitt(

				id_form_querschnitt INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:032
	cur.execute("""
				CREATE TABLE publication_type(

				id_publication_type INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				publication_type_tag VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:033
	cur.execute("""
				CREATE TABLE biblio_junction_type(

				id_biblio_junction_type INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				biblio_junction_type_tag VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255)

				)

	""")

	# L00:034
	cur.execute("""
				CREATE TABLE biblio_junction_boilerplate(

				id_biblio_junction_boilerplate INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				biblio_junction_boilerplate_tag VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:035
	cur.execute("""
				CREATE TABLE language(

				id_language INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				language_tag VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255)

				)

	""")

	# L00:036
	cur.execute("""
				CREATE TABLE primary_source_document_type(

				id_primary_source_document_type INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:037
	cur.execute("""
				CREATE TABLE primary_source_document_manufacture(

				id_primary_source_document_manufacture INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:038
	cur.execute("""
				CREATE TABLE gender(

				id_gender INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				gender_tag VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255)

				)

	""")


	# L00:039
	cur.execute("""
				CREATE TABLE modern_state(

				id_modern_state INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				modern_state_iso_code VARCHAR(3),
				polygon VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)
	""")

	# L00:040
	cur.execute("""
				CREATE TABLE organisation(

				id_organisation INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				gnd_id VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)
	""")

	# L00:041
	cur.execute("""
				CREATE TABLE find_type(

				id_find_type INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)
                
				)

	""")

	# L00:042
	cur.execute("""
				CREATE TABLE other_object_category(

				id_other_object_category INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				shorthand_other_object_category VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:043
	cur.execute("""
				CREATE TABLE biblio_junction_Detaillierungsgrad(

				id_biblio_junction_Detaillierungsgrad INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				biblio_junction_Detaillierungsgrad_tag VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L00:044
	cur.execute("""
				CREATE TABLE function_table(

				id_function_table INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
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

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	print("L00-tables created")

	return