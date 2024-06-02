CREATE SCHEMA metadata;


CREATE TABLE [metadata].[config_table] (
	[task_id] int NULL, 
	[task_name] varchar(100) NULL, 
	[source_connection] varchar(8000) NULL, 
	[source_folder] varchar(100) NULL, 
	[source_database] varchar(100) NULL, 
	[source_schema] varchar(100) NULL, 
	[source_table] varchar(100) NULL, 
	[source_view] varchar(100) NULL, 
	[target_folder] varchar(100) NULL, 
	[target_database] varchar(100) NULL, 
	[target_schema] varchar(100) NULL, 
	[target_table] varchar(100) NULL, 
	[load_type] varchar(50) NULL,
    [phase] varchar(100) NULL,
	[enable] bit NULL
);

-- SELECT * FROM [metadata].[config_table] ORDER BY [task_id] ASC;
