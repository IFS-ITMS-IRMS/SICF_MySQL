# SICF - Mock-up MySQL Database

## Purpose
The scripts in this repository can be run to create the tables of the SICF MySQL database. The intention is to show what attributes consititue an entity and by implementing the foreign key constraints, the relationships between the tables are modelled. This mock-up database is intended as a (data-type-wise and not-foreign-key-constraint-wise naive) scaffolding that the MySQL database containing the SICF-data will be built upon.

## Requirements
To be able to run the scripts the following should be installed on the computer:
- Python 3.8
- MySQL
- Python module: mysql.connector-python

In the Python scripts the connector uses the following configuration:
- `host="localhost"`
- `user="IFS"`
- `password="IFS_pw"`
- `database="Mock_up_DB"`

Therefore, in the local MySQL application the user `IFS` has to be created and the necessary configurations have to be made to allow the Python scripts to run, create, and manipulate the database.  
We recommend using the [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) to make the necessary local configurations.  
To install mysql.connector-python we recommend using pip3, running the following from the command line: `pip3 install mysql.connector-python`. Detailed instructions can be found [here](https://github.com/IFS-ITMS-IRMS/SICF_MySQL/tree/main/Documentation/Install-Mock-up-db-IFS).

## Structure of the Python Scripts

#### Folder Structure and Contained Files
```
SICF_MySQL
	|
	-> README.md
	-> Documentation
		|
		-> Coloured_Graph
		-> Generate-ER-Diagram
		-> Install-Mock-up-db-IFS
		-> ER_Schema.pdf
		-> (TODO: Word Rahel)
	-> Python_Scripts
		|
		-> main_MySQL_Database.py
		-> create_tables
			|
			-> create_tables_L00.py
			-> ...
			-> ...
			-> create_tables_L09.py
		-> drop_tables
			|
			-> drop_tables_L00.py
			-> ...
			-> ...
			-> drop_tables_L00.py
```

#### Creating the Database and Tables
The tables are ordered into numbered levels depending on their dependencies on other tables. As these dependencies give the order the tables have to be created resp. dropped in, they are sorted into their respective `create_tables_LXX.py` and `drop_tables_LXX.py` scripts.  
In the `main_MySQL_Database.py` script the create- and drop-function-calls can be commented or uncommented to steer what is done during any run of `main_MySQL_Database.py`.  
To generate the ER-Diagram using the MySQL Workbench these [instructions](https://github.com/IFS-ITMS-IRMS/SICF_MySQL/tree/main/Documentation/Generate-ER-Diagram) can be followed.

#### Documentation
All tables are given a number within their level and are identified as LXX:YYY, e.g., L02:005 is the fifth table in Level 2. The ordering of the tables within one level can be treated as arbitrary, but the same table is identified with its number in `create_tables_LXX.py`, `drop_tables_LXX.py` as well as in the ER-schema, [ER_Schema.pdf](https://github.com/IFS-ITMS-IRMS/SICF_MySQL/blob/main/Documentation/ER_Schema_MySQL_DB.pdf).  
Constraints that are not foreign key constraints are documented in the ER-schema.
