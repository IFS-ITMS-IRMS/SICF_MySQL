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

def create_tables_l01():

	# L01:001
	cur.execute("""
				CREATE TABLE field_of_numismatics(

				id_field_of_numismatics INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				field_of_numismatics_tag VARCHAR(255),
				id_era INT,
				value_german VARCHAR(255),
				value_german_alternative VARCHAR(255),
				value_french VARCHAR(255),
				value_french_alternative VARCHAR(255),
				value_italian VARCHAR(255),
				value_italian_alternative VARCHAR(255),
				value_english VARCHAR(255),
				value_english_alternative VARCHAR(255),
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

	# L01:002
	cur.execute("""
				CREATE TABLE numismatic_time_slice(

				id_numismatic_time_slice INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				numismatic_time_slice_acronym VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
				date_from DATE,
				date_to DATE,
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

	# L01:003
	cur.execute("""
				CREATE TABLE find_type_external_reference(

				id_find_type_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_type INT,
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

				FOREIGN KEY (id_find_type)
					REFERENCES find_type(id_find_type),

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

	# L01:004
	cur.execute("""
				CREATE TABLE other_object_category_external_reference(

				id_other_object_category_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object_category INT,
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

				FOREIGN KEY (id_other_object_category)
					REFERENCES other_object_category(id_other_object_category),

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

	# L01:005
	cur.execute("""
				CREATE TABLE art_der_fundstelle_type(

				id_art_der_fundstelle_type INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_art_der_fundstelle_category INT,
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

				FOREIGN KEY (id_art_der_fundstelle_category)
					REFERENCES art_der_fundstelle_category(id_art_der_fundstelle_category),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L01:006
	cur.execute("""
				CREATE TABLE type(

				id_type INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				type_tag VARCHAR(255),
				value_german VARCHAR(255),
				value_french VARCHAR(255),
				value_italian VARCHAR(255),
				value_english VARCHAR(255),
				id_face INT,
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

				FOREIGN KEY (id_face)
					REFERENCES face(id_face),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L01:007
	cur.execute("""
				CREATE TABLE ruler(

				id_ruler INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				date_birth DATE,
				date_death DATE,
				lived_post DATE,
				lived_ante DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				id_gender INT,
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				gnd_id VARCHAR(255),
				nomisma_org_id VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_gender)
					REFERENCES gender(id_gender),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L01:008
	cur.execute("""
				CREATE TABLE modern_person_name(

				id_modern_person_name INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_modern_person INT,
				modern_person_acronym VARCHAR(255),
				surname VARCHAR(255),
				first_names VARCHAR(255),
				first_names_initials VARCHAR(255),
				id_gender INT,
				name_main_entry_flag BOOLEAN,
				name_erroneous_flag BOOLEAN,
				name_nom_de_plume_flag BOOLEAN,
				date_from DATE,
				date_to DATE,
				date_post DATE,
				date_ante DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
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

				FOREIGN KEY (id_gender)
					REFERENCES gender(id_gender),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L01:009
	cur.execute("""
				CREATE TABLE modern_region(

				id_modern_region INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_modern_state INT,
				id_region_category INT,
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				modern_region_iso_code VARCHAR(255),
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

				FOREIGN KEY (id_modern_state)
					REFERENCES modern_state(id_modern_state),

				FOREIGN KEY (id_region_category)
					REFERENCES region_category(id_region_category),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L01:010
	cur.execute("""
				CREATE TABLE authenticity_external_reference(

				id_authenticity_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_authenticity INT,
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

				FOREIGN KEY (id_authenticity)
					REFERENCES authenticity(id_authenticity),

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

	# L01:011
	cur.execute("""
				CREATE TABLE authenticity_interpretation_external_reference(

				id_authenticity_interpretation_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_authenticity_interpretation INT,
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

				FOREIGN KEY (id_authenticity_interpretation)
					REFERENCES authenticity_interpretation(id_authenticity_interpretation),

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

	# L01:012
	cur.execute("""
				CREATE TABLE bearbeitungsstand_external_reference(

				id_bearbeitungsstand_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_bearbeitungsstand INT,
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

				FOREIGN KEY (id_bearbeitungsstand)
					REFERENCES bearbeitungsstand(id_bearbeitungsstand),

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

	# L01:013
	cur.execute("""
				CREATE TABLE conservation_state_external_reference(

				id_conservation_state_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_conservation_state INT,
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

				FOREIGN KEY (id_conservation_state)
					REFERENCES conservation_state(id_conservation_state),

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

	# L01:014
	cur.execute("""
				CREATE TABLE container_material_external_reference(

				id_container_material_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_container_material INT,
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

				FOREIGN KEY (id_container_material)
					REFERENCES container_material(id_container_material),

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

	# L01:015
	cur.execute("""
				CREATE TABLE corrosion_external_reference(

				id_corrosion_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_corrosion INT,
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

				FOREIGN KEY (id_corrosion)
					REFERENCES corrosion(id_corrosion),

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

	# L01:016
	cur.execute("""
				CREATE TABLE datenqualitaet_external_reference(

				id_datenqualitaet_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_datenqualitaet INT,
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

				FOREIGN KEY (id_datenqualitaet)
					REFERENCES datenqualitaet(id_datenqualitaet),

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

	# L01:017
	cur.execute("""
				CREATE TABLE era_external_reference(

				id_era_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_era INT,
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

				FOREIGN KEY (id_era)
					REFERENCES era(id_era),

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

	# L01:018
	cur.execute("""
				CREATE TABLE external_nomenclature_external_reference(

				id_external_nomenclature_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_external_nomenclature INT,
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

				FOREIGN KEY (id_external_nomenclature)
					REFERENCES external_nomenclature(id_external_nomenclature),

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

	# L01:019
	cur.execute("""
				CREATE TABLE face_external_reference(

				id_face_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_face INT,
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

				FOREIGN KEY (id_face)
					REFERENCES face(id_face),

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

	# L01:020
	cur.execute("""
				CREATE TABLE discovery_method_external_reference(

				id_discovery_method_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_discovery_method INT,
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

				FOREIGN KEY (id_discovery_method)
					REFERENCES discovery_method(id_discovery_method),

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

	# L01:021
	cur.execute("""
				CREATE TABLE form_aufsicht_external_reference(

				id_form_aufsicht_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_form_aufsicht INT,
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

				FOREIGN KEY (id_form_aufsicht)
					REFERENCES form_aufsicht(id_form_aufsicht),

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

	# L01:022
	cur.execute("""
				CREATE TABLE form_querschnitt_external_reference(

				id_form_querschnitt_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_form_querschnitt INT,
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

				FOREIGN KEY (id_form_querschnitt)
					REFERENCES form_querschnitt(id_form_querschnitt),

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

	# L01:023
	cur.execute("""
				CREATE TABLE geographical_unit_external_reference(

				id_geographical_unit_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_geographical_unit INT,
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

				FOREIGN KEY (id_geographical_unit)
					REFERENCES geographical_unit(id_geographical_unit),

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

	# L01:024
	cur.execute("""
				CREATE TABLE manufacture_external_reference(

				id_manufacture_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_manufacture INT,
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

				FOREIGN KEY (id_manufacture)
					REFERENCES manufacture(id_manufacture),

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

	# L01:025
	cur.execute("""
				CREATE TABLE material_external_reference(

				id_material_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_material INT,
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

				FOREIGN KEY (id_material)
					REFERENCES material(id_material),

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

	# L01:026
	cur.execute("""
				CREATE TABLE modern_state_external_reference(

				id_modern_state_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_modern_state INT,
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

				FOREIGN KEY (id_modern_state)
					REFERENCES modern_state(id_modern_state),

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

	# L01:027
	cur.execute("""
				CREATE TABLE object_category_external_reference(

				id_object_category_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_object_category INT,
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

				FOREIGN KEY (id_object_category)
					REFERENCES object_category(id_object_category),

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

	# L01:028
	cur.execute("""
				CREATE TABLE organisation_external_reference(

				id_organisation_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_organisation INT,
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

				FOREIGN KEY (id_organisation)
					REFERENCES organisation(id_organisation),

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

	# L01:029
	cur.execute("""
				CREATE TABLE peculiarity_of_production_external_reference(

				id_peculiarity_of_production_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_peculiarity_of_production INT,
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

				FOREIGN KEY (id_peculiarity_of_production)
					REFERENCES peculiarity_of_production(id_peculiarity_of_production),

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

	# L01:030
	cur.execute("""
				CREATE TABLE region_category_external_reference(

				id_region_category_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_region_category INT,
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

				FOREIGN KEY (id_region_category)
					REFERENCES region_category(id_region_category),

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

	# L01:031
	cur.execute("""
				CREATE TABLE secondary_treatment_external_reference(

				id_secondary_treatment_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_secondary_treatment INT,
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

				FOREIGN KEY (id_secondary_treatment)
					REFERENCES secondary_treatment(id_secondary_treatment),

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

	# L01:032
	cur.execute("""
				CREATE TABLE wear_external_reference(

				id_wear_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_wear INT,
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

				FOREIGN KEY (id_wear)
					REFERENCES wear(id_wear),

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

	# L01:033
	cur.execute("""
				CREATE TABLE modern_person_external_reference(

				id_modern_person_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_modern_person INT,
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

				FOREIGN KEY (id_modern_person)
					REFERENCES modern_person(id_modern_person),

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

	# L01:034
	cur.execute("""
				CREATE TABLE primary_source_document_manufacture_external_reference(

				id_primary_source_document_manufacture_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document_manufacture INT,
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

				FOREIGN KEY (id_primary_source_document_manufacture)
					REFERENCES primary_source_document_manufacture(id_primary_source_document_manufacture),

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

	# L01:035
	cur.execute("""
				CREATE TABLE primary_source_document_type_external_reference(

				id_primary_source_document_type_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document_type INT,
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

				FOREIGN KEY (id_primary_source_document_type)
					REFERENCES primary_source_document_type(id_primary_source_document_type),

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

	# L01:036
	cur.execute("""
				CREATE TABLE publication_type_external_reference(

				id_publication_type_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_publication_type INT,
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

				FOREIGN KEY (id_publication_type)
					REFERENCES publication_type(id_publication_type),

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

	# L01:037
	cur.execute("""
				CREATE TABLE find_category_external_reference(

				id_find_category_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find_category INT,
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

				FOREIGN KEY (id_find_category)
					REFERENCES find_category(id_find_category),

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
	
	# L01:038
	cur.execute("""
				CREATE TABLE other_object_type(

				id_other_object_type INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object_category INT,
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
	
	# L01:039
	cur.execute("""
				CREATE TABLE other_object_name(

				id_other_object_name INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_other_object_category INT,
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
	
	# L01:040
	cur.execute("""
				CREATE TABLE archaeological_event(

				id_archaeological_event INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				name_official_active_flag BOOLEAN,
				name_official_flag BOOLEAN,
				name_alias_flag BOOLEAN,
				owner_id_organisation INT,
				archaeological_event_tag VARCHAR(255),
				name_german VARCHAR(255),
				name_french VARCHAR(255),
				name_italian VARCHAR(255),
				name_english VARCHAR(255),
				id_external_nomenclature INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
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

				FOREIGN KEY (owner_id_organisation)
					REFERENCES organisation(id_organisation),

				FOREIGN KEY (id_external_nomenclature)
					REFERENCES external_nomenclature(id_external_nomenclature),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")
	
	# L01:041
	cur.execute("""
				CREATE TABLE person_muenzadministration(

				id_person_muenzadministration INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				date_birth DATE,
				date_death DATE,
				lived_post DATE,
				lived_ante DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				id_gender INT,
				comment_public_german VARCHAR(255),
				comment_public_french VARCHAR(255),
				comment_public_italian VARCHAR(255),
				comment_public_english VARCHAR(255),
				comment_internal VARCHAR(255),
				gnd_id INT,
				nomisma_org_id VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_gender)
					REFERENCES gender(id_gender),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")
	
	# L01:042
	cur.execute("""
				CREATE TABLE bibliography(

				id_bibliography INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				Supersammelbegriff BOOLEAN,
				author_editor_text_german TEXT,
				author_editor_text_french TEXT,
				author_editor_text_italian TEXT,
				author_editor_text_english TEXT,
				bibliography_title_german TEXT,
				bibliography_title_french TEXT,
				bibliography_title_italian TEXT,
				bibliography_title_english TEXT,
				bibliography_title_other TEXT,
				bibliography_abbreviation_german TEXT,
				bibliography_abbreviation_french TEXT,
				bibliography_abbreviation_italian TEXT,
				bibliography_abbreviation_english TEXT,
				bibliography_abbreviation_other TEXT,
				publication_date_from DATE,
				publication_date_to DATE,
				publication_date_text_german TEXT,
				publication_date_text_french TEXT,
				publication_date_text_italian TEXT,
				publication_date_text_english TEXT,
				place_of_publication_text_german TEXT,
				place_of_publication_text_french TEXT,
				place_of_publication_text_italian TEXT,
				place_of_publication_text_english TEXT,
				publication_status BOOLEAN,
				id_publication_type INT,
				language_text_german TEXT,
				language_text_french TEXT,
				language_text_italian TEXT,
				language_text_english TEXT,
				shorthand_SICF BOOLEAN,
				shorthand_SICF_german TEXT,
				shorthand_SICF_french TEXT,
				shorthand_SICF_italian TEXT,
				shorthand_SICF_english TEXT,
				shorthand_authors_year TEXT,
				band TEXT,
				jahrgang TEXT,
				issue TEXT,
				pages TEXT,
				figures TEXT,
				plates TEXT,
				quotation_text TEXT,
				comment_public_german TEXT,
				comment_public_french TEXT,
				comment_public_italian TEXT,
				comment_public_english TEXT,
				comment_internal TEXT,
				zenon_record INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_publication_type)
					REFERENCES publication_type(id_publication_type),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")
	
	# L01:043
	cur.execute("""
				CREATE TABLE primary_source_document(

				id_primary_source_document INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				editor_text_german TEXT,
				editor_text_french TEXT,
				editor_text_italian TEXT,
				editor_text_english TEXT,
				author_text_german TEXT,
				author_text_french TEXT,
				author_text_italian TEXT,
				author_text_english TEXT,
				primary_source_document_title_german TEXT,
				primary_source_document_title_french TEXT,
				primary_source_document_title_italian TEXT,
				primary_source_document_title_english TEXT,
				primary_source_document_title_other TEXT,
				bears_date_transcription TEXT,
				bears_date_transliteration TEXT,
				bears_date_transliteration_id_calendar INT,
				date_from DATE,
				date_to DATE,
				date_text_german TEXT,
				date_text_french TEXT,
				date_text_italian TEXT,
				date_text_english TEXT,
				place_of_production_text_german TEXT,
				place_of_production_text_french TEXT,
				place_of_production_text_italian TEXT,
				place_of_production_text_english TEXT,
				id_primary_source_document_type INT,
				primary_source_document_type_remark_german TEXT,
				primary_source_document_type_remark_french TEXT,
				primary_source_document_type_remark_italian TEXT,
				primary_source_document_type_remark_english TEXT,
				manufacture_remark_german TEXT,
				manufacture_remark_french TEXT,
				manufacture_remark_italian TEXT,
				manufacture_remark_english TEXT,
				language_remark_german TEXT,
				language_remark_french TEXT,
				language_remark_italian TEXT,
				language_remark_english TEXT,
				informative_value_remark_german TEXT,
				informative_value_remark_french TEXT,
				informative_value_remark_italian TEXT,
				informative_value_remark_english TEXT,
				volume TEXT,
				issue TEXT,
				pages TEXT,
				figures TEXT,
				plates TEXT,
				abstract_german TEXT,
				abstract_french TEXT,
				abstract_italian TEXT,
				abstract_english TEXT,
				quotation_text TEXT,
				comment_public_german TEXT,
				comment_public_french TEXT,
				comment_public_italian TEXT,
				comment_public_english TEXT,
				comment_internal TEXT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (bears_date_transliteration_id_calendar)
					REFERENCES calendar(id_calendar),

				FOREIGN KEY (bears_date_transliteration_id_calendar)
					REFERENCES calendar(id_calendar),

				FOREIGN KEY (id_primary_source_document_type)
					REFERENCES primary_source_document_type(id_primary_source_document_type),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")
	
	# L01:044
	cur.execute("""
				CREATE TABLE data_source_junction(

				id_data_source_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_data_source INT,
				id_modern_person INT,
				id_organisation INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (id_modern_person)
					REFERENCES modern_person(id_modern_person),

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
	
	# L01:045
	cur.execute("""
				CREATE TABLE art_der_fundstelle_category_external_reference(

				id_art_der_fundstelle_category_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_art_der_fundstelle_category INT,
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

				FOREIGN KEY (id_art_der_fundstelle_category)
					REFERENCES art_der_fundstelle_category(id_art_der_fundstelle_category),

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
	
	# L01:046
	cur.execute("""
				CREATE TABLE biblio_junction_detaillierungsgrad_external_reference(

				id_biblio_junction_detaillierungsgrad_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_biblio_junction_detaillierungsgrad INT,
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

				FOREIGN KEY (id_biblio_junction_detaillierungsgrad)
					REFERENCES biblio_junction_detaillierungsgrad(id_biblio_junction_detaillierungsgrad),

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
	
	# L01:047
	cur.execute("""
				CREATE TABLE prim_source_doc_informative_value_external_reference(

				id_prim_source_doc_informative_value_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_primary_source_document_informative_value INT,
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

				FOREIGN KEY (id_primary_source_document_informative_value)
					REFERENCES primary_source_document_informative_value(id_primary_source_document_informative_value),

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

	print("L01-tables created")

	return