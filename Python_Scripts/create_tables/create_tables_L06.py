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

def create_tables_l06():

	# L06:001
	cur.execute("""
				CREATE TABLE commune_section_part(

				id_commune_section_part INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_commune_section INT,
				id_fundstelle_ort_lieu INT,
				id_fundstelle_flur_lieu_dit INT,
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_commune_section)
					REFERENCES commune_section(id_commune_section),

				FOREIGN KEY (id_fundstelle_ort_lieu)
					REFERENCES fundstelle_ort_lieu(id_fundstelle_ort_lieu),

				FOREIGN KEY (id_fundstelle_flur_lieu_dit)
					REFERENCES fundstelle_flur_lieu_dit(id_fundstelle_flur_lieu_dit),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)
	""")

	# L06:002
	cur.execute("""
				CREATE TABLE fundstelle_flur_lieu_dit_new_old_relation(

				id_fundstelle_flur_lieu_dit_new_old_relation INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_fundstelle_flur_lieu_dit INT,
				old_id_fundstelle_flur_lieu_dit INT,
				comment_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_fundstelle_flur_lieu_dit)
					REFERENCES fundstelle_flur_lieu_dit(id_fundstelle_flur_lieu_dit),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L06:003
	cur.execute("""
				CREATE TABLE fundstelle_flur_lieu_dit_external_reference(

				id_fundstelle_flur_lieu_dit_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_fundstelle_flur_lieu_dit INT,
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

				FOREIGN KEY (id_fundstelle_flur_lieu_dit)
					REFERENCES fundstelle_flur_lieu_dit(id_fundstelle_flur_lieu_dit),

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

	# L06:004
	cur.execute("""
				CREATE TABLE find(

				id_find INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_fundstelle_flur_lieu_dit INT,
				part_name_german TEXT,
				part_name_french TEXT,
				part_name_italian TEXT,
				part_name_english TEXT,
				find_date_from DATE,
				find_date_to DATE,
				find_date_german TEXT,
				find_date_french TEXT,
				find_date_italian TEXT,
				find_date_english TEXT,
				reporting_date DATE,
				reporting_date_text_german TEXT,
				reporting_date_text_french TEXT,
				reporting_date_text_italian TEXT,
				reporting_date_text_english TEXT,
				number_of_coins_from INT,
				number_of_coins_to INT,
				number_of_coins_text_german TEXT,
				number_of_coins_text_french TEXT,
				number_of_coins_text_italian TEXT,
				number_of_coins_text_english TEXT,
				number_of_other_objects_from INT,
				number_of_other_objects_to INT,
				number_of_other_objects_text_german TEXT,
				number_of_other_objects_text_french TEXT,
				number_of_other_objects_text_italian TEXT,
				number_of_other_objects_text_english TEXT,
				datierung_komplexinhalt_from DATE,
				datierung_komplexinhalt_to DATE,
				long_ch_lv95_e FLOAT,
				lat_ch_lv95_n FLOAT,
				altitude_ch FLOAT,
				polygon TEXT,
				geodata_text_german TEXT,
				geodata_text_french TEXT,
				geodata_text_italian TEXT,
				geodata_text_english TEXT,
				id_datenqualitaet INT,
				id_bearbeitungsstand INT,
				discovery_method_text_german TEXT,
				discovery_method_text_french TEXT,
				discovery_method_text_italian TEXT,
				discovery_method_text_english TEXT,
				art_der_fundstelle_text_german TEXT,
				art_der_fundstelle_text_french TEXT,
				art_der_fundstelle_text_italian TEXT,
				art_der_fundstelle_text_english TEXT,
				art_des_fundes_text_german TEXT,
				art_des_fundes_text_french TEXT,
				art_des_fundes_text_italian TEXT,
				art_des_fundes_text_english TEXT,
				container_id_yes_no_unknown INT,
				objects_numismatic_objects_production_id_yes_no_unknown INT,
				objects_numismatic_objects_production_remark_german TEXT,
				objects_numismatic_objects_production_remark_french TEXT,
				objects_numismatic_objects_production_remark_italian TEXT,
				objects_numismatic_objects_production_remark_english TEXT,
				text_total TEXT,
				text_era_u TEXT,
				text_era_a TEXT,
				text_era_m TEXT,
				text_era_n TEXT,
				text_era_o TEXT,
				text_other_objects TEXT,
				number_of_coins_u INT,
				number_of_coins_a INT,
				number_of_coins_a01 INT,
				number_of_coins_a02 INT,
				number_of_coins_a03 INT,
				number_of_coins_a04 INT,
				number_of_coins_m INT,
				number_of_coins_m06 INT,
				number_of_coins_m07 INT,
				number_of_coins_m08 INT,
				number_of_coins_m09 INT,
				number_of_coins_m10 INT,
				number_of_coins_m11 INT,
				number_of_coins_m12 INT,
				number_of_coins_m13 INT,
				number_of_coins_m14 INT,
				number_of_coins_m15 INT,
				number_of_coins_n INT,
				number_of_coins_n16 INT,
				number_of_coins_n17 INT,
				number_of_coins_n18 INT,
				number_of_coins_n19 INT,
				number_of_coins_n20 INT,
				number_of_coins_n21 INT,
				number_of_coins_o INT,
				zusammensetzung_remark_german TEXT,
				zusammensetzung_remark_french TEXT,
				zusammensetzung_remark_italian TEXT,
				zusammensetzung_remark_english TEXT,
				regest_remark_german TEXT,
				regest_remark_french TEXT,
				regest_remark_italian TEXT,
				regest_remark_english TEXT,
				remark_public_german TEXT,
				remark_public_french TEXT,
				remark_public_italian TEXT,
				remark_public_english TEXT,
				remark_internal TEXT,
				zur_fundstelle_kommentar_remark_german TEXT,
				zur_fundstelle_kommentar_remark_french TEXT,
				zur_fundstelle_kommentar_remark_italian TEXT,
				zur_fundstelle_kommentar_remark_english TEXT,
				discovery_method_remark_german TEXT,
				discovery_method_remark_french TEXT,
				discovery_method_remark_italian TEXT,
				discovery_method_remark_english TEXT,
				zur_ueberlieferung_kommentar_remark_german TEXT,
				zur_ueberlieferung_kommentar_remark_french TEXT,
				zur_ueberlieferung_kommentar_remark_italian TEXT,
				zur_ueberlieferung_kommentar_remark_english TEXT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_fundstelle_flur_lieu_dit)
					REFERENCES fundstelle_flur_lieu_dit(id_fundstelle_flur_lieu_dit),

				FOREIGN KEY (id_datenqualitaet)
					REFERENCES datenqualitaet(id_datenqualitaet),

				FOREIGN KEY (id_bearbeitungsstand)
					REFERENCES bearbeitungsstand(id_bearbeitungsstand),

				FOREIGN KEY (container_id_yes_no_unknown)
					REFERENCES yes_no_unknown(id_yes_no_unknown),

				FOREIGN KEY (objects_numismatic_objects_production_id_yes_no_unknown)
					REFERENCES yes_no_unknown(id_yes_no_unknown),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L06:005
	cur.execute("""
				CREATE TABLE person_muenzadministration_name_external_reference(

				id_person_muenzadministration_name_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_person_muenzadministration_name INT,
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

				FOREIGN KEY (id_person_muenzadministration_name)
					REFERENCES person_muenzadministration_name(id_person_muenzadministration_name),

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

	print("L06-tables created")

	return
