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

def create_tables_l07():

	# L07:001
	cur.execute("""
				CREATE TABLE find_fremde_id(

				id_find_fremde_id INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

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

	# L07:002
	cur.execute("""
				CREATE TABLE find_finder(

				id_find_finder INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_organisation_name INT,
				id_modern_person_name INT,
				find_finder_qualifier BOOLEAN,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

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

	# L07:003
	cur.execute("""
				CREATE TABLE find_bringer(

				id_find_bringer INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_organisation_name INT,
				id_modern_person_name INT,
				find_bringer_qualifier BOOLEAN,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

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

	# L07:004
	cur.execute("""
				CREATE TABLE find_aufbewahrer(

				id_find_aufbewahrer INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				find_aufbewahrer_active_flag BOOLEAN,
				id_find INT,
				id_organisation INT,
				id_modern_person INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				find_aufbewahrer_qualifier BOOLEAN,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

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

	# L07:005
	cur.execute("""
				CREATE TABLE find_bearbeiter(

				id_find_bearbeiter INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_modern_person_name INT,
				id_modern_person_affiliation INT,
				id_organisation_name INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				find_Bearbeiter_qualifier BOOLEAN,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

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

	# L07:006
	cur.execute("""
				CREATE TABLE find_discovery_method_junction(

				id_find_discovery_method_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_discovery_method INT,
				discovery_method_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (id_discovery_method)
					REFERENCES discovery_method(id_discovery_method),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L07:007
	cur.execute("""
				CREATE TABLE find_find_category_junction(

				id_find_find_category_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_find_category INT,
				find_category_qualifier BOOLEAN,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (id_find_category)
					REFERENCES find_category(id_find_category),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L07:008
	cur.execute("""
				CREATE TABLE find_find_type_junction(

				id_find_find_type_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_find_type INT,
				find_type_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (id_find_type)
					REFERENCES find_type(id_find_type),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)
				)

	""")

	# L07:009
	cur.execute("""
				CREATE TABLE find_sicf_number(

				id_find_sicf_number INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				find_sicf_number_active_flag BOOLEAN,
				sicf_id_commune INT,
				sicf_id_district INT,
				sicf_Komplex INT,
				sicf_Unterkomplex INT,
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				name_old_german VARCHAR(255),
				name_old_french VARCHAR(255),
				name_old_italian VARCHAR(255),
				name_old_english VARCHAR(255),
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (sicf_id_commune)
					REFERENCES commune(id_commune),

				FOREIGN KEY (sicf_id_district)
					REFERENCES district(id_district),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L07:010
	cur.execute("""
				CREATE TABLE find_external_reference(

				id_find_external_reference INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

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

	# L07:011
	cur.execute("""
				CREATE TABLE find_find_part(

				id_find_find_part INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				komplex_id_find INT,
				unterkomplex_id_find INT,
				remark_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (komplex_id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (unterkomplex_id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L07:012
	cur.execute("""
				CREATE TABLE find_object(

				id_find_object INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				muenznummer INT,
				archaeological_details_edited_remark_german TEXT,
				archaeological_details_edited_remark_french TEXT,
				archaeological_details_edited_remark_italian TEXT,
				archaeological_details_edited_remark_english TEXT,
				long_ch_lv95_e FLOAT,
				lat_ch_lv95_n FLOAT,
				altitude_ch FLOAT,
				individual_object_coordinates_id_yes_no_unknown INT,
				geodata_text_german TEXT,
				geodata_text_french TEXT,
				geodata_text_italian TEXT,
				geodata_text_english TEXT,
				id_object_category INT,
				bears_date_transcription TEXT,
				bears_date_transliteration INT,
				bears_date_transliteration_id_calendar INT,
				date_from DATE,
				date_to DATE,
				date_text_german TEXT,
				date_text_french TEXT,
				date_text_italian TEXT,
				date_text_english TEXT,
				id_numismatic_time_slice_from INT,
				id_numismatic_time_slice_to INT,
				id_era INT,
				obverse_legend_german TEXT,
				obverse_legend_french TEXT,
				obverse_legend_italian TEXT,
				obverse_legend_english TEXT,
				obverse_description_german TEXT,
				obverse_description_french TEXT,
				obverse_description_italian TEXT,
				obverse_description_english TEXT,
				reverse_legend_german TEXT,
				reverse_legend_french TEXT,
				reverse_legend_italian TEXT,
				reverse_legend_english TEXT,
				reverse_description_german TEXT,
				reverse_description_french TEXT,
				reverse_description_italian TEXT,
				reverse_description_english TEXT,
				rim_description_german TEXT,
				rim_description_french TEXT,
				rim_description_italian TEXT,
				rim_description_english TEXT,
				weight FLOAT,
				diameter_max FLOAT,
				diameter_min FLOAT,
				measurements_remark_german TEXT,
				measurements_remark_french TEXT,
				measurements_remark_italian TEXT,
				measurements_remark_english TEXT,
				axis INT,
				id_material INT,
				material_qualifier BOOLEAN,
				material_remark_german TEXT,
				material_remark_french TEXT,
				material_remark_italian TEXT,
				material_remark_english TEXT,
				id_manufacture INT,
				manufacture_qualifier BOOLEAN,
				manufacture_remark_german TEXT,
				manufacture_remark_french TEXT,
				manufacture_remark_italian TEXT,
				manufacture_remark_english TEXT,
				id_authenticity INT,
				authenticity_qualifier BOOLEAN,
				id_authenticity_interpretation INT,
				authenticity_interpretation_qualifier BOOLEAN,
				authenticity_interpretation_remark_german TEXT,
				authenticity_interpretation_remark_french TEXT,
				authenticity_interpretation_remark_italian TEXT,
				authenticity_interpretation_remark_english TEXT,
				peculiarity_of_production_remark_german TEXT,
				peculiarity_of_production_remark_french TEXT,
				peculiarity_of_production_remark_italian TEXT,
				peculiarity_of_production_remark_english TEXT,
				secondary_treatment_remark_german TEXT,
				secondary_treatment_remark_french TEXT,
				secondary_treatment_remark_italian TEXT,
				secondary_treatment_remark_english TEXT,
				conservation_state_remark_german TEXT,
				conservation_state_remark_french TEXT,
				conservation_state_remark_italian TEXT,
				conservation_state_remark_english TEXT,
				obverse_id_wear INT,
				reverse_id_wear INT,
				obverse_id_corrosion INT,
				reverse_id_corrosion INT,
				id_form_aufsicht INT,
				id_form_querschnitt INT,
				form_remark_german TEXT,
				form_remark_french TEXT,
				form_remark_italian TEXT,
				form_remark_english TEXT,
				remark_public_german TEXT,
				remark_pubic_french TEXT,
				remark_public_italian TEXT,
				remark_public_english TEXT,
				remark_internal TEXT,
				id_datenqualitaet INT,
				id_bearbeitungsstand INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (individual_object_coordinates_id_yes_no_unknown)
					REFERENCES yes_no_unknown(id_yes_no_unknown),

				FOREIGN KEY (id_object_category)
					REFERENCES object_category(id_object_category),

				FOREIGN KEY (bears_date_transliteration_id_calendar)
					REFERENCES calendar(id_calendar),

				FOREIGN KEY (id_numismatic_time_slice_from)
					REFERENCES numismatic_time_slice(id_numismatic_time_slice),

				FOREIGN KEY (id_numismatic_time_slice_to)
					REFERENCES numismatic_time_slice(id_numismatic_time_slice),

				FOREIGN KEY (id_era)
					REFERENCES era(id_era),

				FOREIGN KEY (id_material)
					REFERENCES material(id_material),

				FOREIGN KEY (id_manufacture)
					REFERENCES manufacture(id_manufacture),

				FOREIGN KEY (id_authenticity)
					REFERENCES authenticity(id_authenticity),

				FOREIGN KEY (id_authenticity_interpretation)
					REFERENCES authenticity_interpretation(id_authenticity_interpretation),

				FOREIGN KEY (obverse_id_wear)
					REFERENCES wear(id_wear),

				FOREIGN KEY (reverse_id_wear)
					REFERENCES wear(id_wear),

				FOREIGN KEY (obverse_id_corrosion)
					REFERENCES corrosion(id_corrosion),

				FOREIGN KEY (reverse_id_corrosion)
					REFERENCES corrosion(id_corrosion),

				FOREIGN KEY (id_form_aufsicht)
					REFERENCES form_aufsicht(id_form_aufsicht),

				FOREIGN KEY (id_form_querschnitt)
					REFERENCES form_querschnitt(id_form_querschnitt),

				FOREIGN KEY (id_datenqualitaet)
					REFERENCES datenqualitaet(id_datenqualitaet),

				FOREIGN KEY (id_bearbeitungsstand)
					REFERENCES bearbeitungsstand(id_bearbeitungsstand),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L07:013
	cur.execute("""
				CREATE TABLE container(

				id_container INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				container_remark_german VARCHAR(255),
				container_remark_french VARCHAR(255),
				container_remark_italian VARCHAR(255),
				container_remark_english VARCHAR(255),
				date_from DATE,
				date_to DATE,
				date_text_german VARCHAR(255),
				date_text_french VARCHAR(255),
				date_text_italian VARCHAR(255),
				date_text_english VARCHAR(255),
				archaeological_details_edited_remark_german VARCHAR(255),
				archaeological_details_edited_remark_french VARCHAR(255),
				archaeological_details_edited_remark_italian VARCHAR(255),
				archaeological_details_edited_remark_english VARCHAR(255),
				remark_internal VARCHAR(255),
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L07:014
	cur.execute("""
				CREATE TABLE find_archaeological_event_junction(

				id_find_archaeological_event_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_archaeological_event INT,
				archaeological_event_qualifier BOOLEAN,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (id_archaeological_event)
					REFERENCES archaeological_event(id_archaeological_event),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L07:015
	cur.execute("""
				CREATE TABLE find_art_der_fundstelle_category_junction(

				id_find_art_der_fundstelle_category_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_art_der_fundstelle_category INT,
				art_der_fundstelle_category_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

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

	# L07:016
	cur.execute("""
				CREATE TABLE find_art_der_fundstelle_type_junction(

				id_find_art_der_fundstelle_type_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_art_der_fundstelle_type INT,
				art_der_fundstelle_type_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

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

	# L07:017
	cur.execute("""
				CREATE TABLE find_art_der_fundstelle_detail_junction(

				id_find_art_der_fundstelle_detail_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_art_der_fundstelle_detail INT,
				art_der_fundstelle_detail_qualifier BOOLEAN,
				manual_order_number INT,
				entry_created_date DATE,
				entry_creator_id_user INT,
				transfer_date DATE,
				transfer_id_data_source INT,
				last_modified_date DATE,
				last_modification_id_user INT,

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (id_art_der_fundstelle_detail)
					REFERENCES art_der_fundstelle_detail(id_art_der_fundstelle_detail),

				FOREIGN KEY (entry_creator_id_user)
					REFERENCES user(id_user),

				FOREIGN KEY (transfer_id_data_source)
					REFERENCES data_source(id_data_source),

				FOREIGN KEY (last_modification_id_user)
					REFERENCES user(id_user)

				)

	""")

	# L07:018
	cur.execute("""
				CREATE TABLE find_biblio_junction(

				id_find_biblio_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_biblio_citation INT,
				id_bibliography INT,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (id_biblio_citation)
					REFERENCES biblio_citation(id_biblio_citation),

				FOREIGN KEY (id_bibliography)
					REFERENCES bibliography(id_bibliography),

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

	# L07:019
	cur.execute("""
				CREATE TABLE find_primary_source_document_junction(

				id_find_primary_source_document_junction INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
				id_primary_source_document_citation INT,
				id_primary_source_document INT,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

				FOREIGN KEY (id_primary_source_document_citation)
					REFERENCES primary_source_document_citation(id_primary_source_document_citation),

				FOREIGN KEY (id_primary_source_document)
					REFERENCES primary_source_document(id_primary_source_document),

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

	# L07:020
	cur.execute("""
				CREATE TABLE remark_user_find_numeric(

				id_remark_user_find_numeric INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

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

	# L07:021
	cur.execute("""
				CREATE TABLE remark_user_find_text(

				id_remark_user_find_text INT AUTO_INCREMENT PRIMARY KEY,
				public BOOLEAN,
				id_find INT,
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

				FOREIGN KEY (id_find)
					REFERENCES find(id_find),

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

	print("L07-tables created")

	return
