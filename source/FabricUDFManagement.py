# Class to store all functions related to Workspace and Items in Workspace of Fabric
class FabricUtils:

    def __init__(self):
        pass

    def get_workspace_info(self, fabric, spark):
        """
        Get workspace information.
        
        Args:
        - fabric: Fabric object to interact with workspaces.
        - spark: Spark session to create DataFrame.
        
        Returns:
        - DataFrame containing workspace ID and Name.
        """
        workspaces = fabric.list_workspaces()
        workspaces_df = spark.createDataFrame(workspaces)
        workspaces_df = workspaces_df.select("Id", "Name")
        return workspaces_df

    def get_workspace_id(self, fabric):
        """
        Get the current workspace ID.
        
        Args:
        - fabric: Fabric object to interact with workspaces.
        
        Returns:
        - Workspace ID as a string.
        """
        workspace_id = fabric.get_notebook_workspace_id()
        return workspace_id

    def get_items_in_workspace(self, fabric, client, pd, spark):
        """
        Get items in the current workspace.
        
        Args:
        - fabric: Fabric object to interact with workspaces.
        - client: Client object to make HTTP requests.
        - pd: Pandas module to normalize JSON.
        - spark: Spark session to create DataFrame.
        
        Returns:
        - DataFrame containing items in the workspace.
        """
        workspace_id = fabric.get_workspace_id()
        response = client.get(f"/v1/workspaces/{workspace_id}/items")
        items = pd.json_normalize(response.json()['value'])
        items_df = spark.createDataFrame(items)
        return items_df


# Class log data for Pipelie
class PipelineLogger:
    
    def __init__(self):
        pass

    def log_data(self, pipelineruntime, task_id, task_name, 
                 start_time, end_time, src_rows_read, numInserted, numUpdated, columnMissing, columnNull, error, status, 
                 types, spark):
        """
        Log the pipeline data.

        Args:
        - pipelineruntime: The runtime of the pipeline.
        - task_id: The task ID.
        - task_name: The task name.
        - start_time: The start time of the task.
        - end_time: The end time of the task.
        - src_rows_read: Number of source rows read.
        - numInserted: Number of rows inserted.
        - numUpdated: Number of rows updated.
        - columnNull: Columns with null counts.
        - error: Error message if any.
        - status: Status of the task.
        - types: instance of pyspark.sql.types
        - spark: SparkSession

        Returns:
        - DataFrame containing items in the workspace.
        """
        # Define schema
        log_schema = types.StructType() \
                        .add("PipelineRunTime", types.StringType(), True) \
                        .add("TaskId", types.IntegerType(), True) \
                        .add("TaskName", types.StringType(), True) \
                        .add("StartTime", types.StringType(), True) \
                        .add("EndTime", types.StringType(), True) \
                        .add("SourceRowsRead", types.IntegerType(), True) \
                        .add("NumTargetInserted", types.IntegerType(), True) \
                        .add("NumTargetUpdated", types.IntegerType(), True) \
                        .add("Status", types.StringType(), True) \
                        .add("ColumnMissing", types.StringType(), True) \
                        .add("ColumnNull", types.StringType(), True) \
                        .add("Error", types.StringType(), True) \

        # Create new row
        new_log_row = [types.Row(pipelineruntime, task_id, task_name, start_time, end_time, 
                                src_rows_read, numInserted, numUpdated, status, columnMissing, columnNull, error)]
        
        new_df = spark.createDataFrame(new_log_row, log_schema)

        # Return value
        return new_df
    

# Class validate data
class ValidateData:

    def __init__(self):
        pass

    # Check column match from dataframe
    def check_schema(self, validator, column_check_match):
        """
        Validate for schema

        Args:
        - validator: Instance for great expectatios
        - column: Column check match

        Returns:
        - String value for schema check
        """

        # Validator
        validator.expect_table_columns_to_match_set(column_check_match, exact_match = True)
        
        # Get validator result
        validation_results = validator.validate()

        # List for append value of missing columns
        missing_columns_list = []

        # Iterating through the results
        for result in validation_results['results']:
            # Checking if the expectation failed
            if not result['success']:
                # Extracting information about mismatched and missing columns
                mismatched_info = result['result']['details']['mismatched']
                unexpected_columns = mismatched_info['unexpected']
                missing_columns = mismatched_info['missing']

                # Concat and add to list
                missing_info = f"Missed column: {missing_columns}, Unexpected column: {unexpected_columns}"
                missing_columns_list.append(missing_info)

        # Convert to string for list
        missing_column_str = '\n'.join(missing_columns_list)

        return missing_column_str 


    # Check null from dataframe
    def check_null(self, validator, colum_check_null):
        """
        Validate for null value

        Args:
        - validator: Instance for great expectatios
        - column: Column check null

        Returns:
        - String value for null column and count
        """

        # expect the following column values to not be null (perhaps these are needed for downstream analytics)
        validator.expect_column_values_to_not_be_null(column = colum_check_null)

        # Run the validator
        validation_results = validator.validate()

        # List
        column_null_list = []

        for result in validation_results['results']:
            # Checking if the expectation failed
            if not result['success']:
                # Extracting information about null values
                null_info = result['result']
                element_count = null_info['element_count']
                unexpected_count = null_info['unexpected_count']

                # Get value and add to list
                column_null_info = f"Column: {colum_check_null}, Number of record: {element_count}, Number of null: {unexpected_count}"
                column_null_list.append(column_null_info)

        # Convert to strings
        null_column_str = '\n'.join(column_null_list)

        return null_column_str

