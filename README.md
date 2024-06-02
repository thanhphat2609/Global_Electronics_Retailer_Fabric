# Global_Electronics_Retailer_Fabric

_Table of contents_
- [**1. Microsoft Fabric**](#1-microsoft-fabric)
- [**2. Data Architecture**](#2-data-architecture)
  * [2.1. Conceptual Architecture base on Fabric](#21-conceptual-architecture-base-on-fabric)
  * [2.2. Physical Architecture](#22-physical-architecture)
- [**3. Building End to End solutions**](#3-building-end-to-end-solutions)
  * [3.1. Dataset](#31-dataset)
  * [3.2. Orchestration (Data Catalog)](#32-orchestration-data-catalog)
  * [3.3. Building Master Pipeline](#33-building-master-pipeline)
 - [**4. Power BI**](#4-power-bi)
  * [4.1. Data Model](#41-data-model)
    + [4.1.1. Data Model Power BI](#411-data-model-power-bi)
    + [4.1.2. Table Manage Relationships](#412-table-manage-relationships)
  * [4.2. Report](#42-report)
- [**5. Conclusion**](#5-conclusion)
- [**6. Lessons Learned**](#6-lessons-learned)
- [**7. Next step**](#7-next-step)


 # **1. Microsoft Fabric**
![Items](https://github.com/thanhphat2609/Global_Super_Store/assets/84914537/b2552438-9fc2-4308-ac2e-bd417c706f4b)



- **OneLake**: OneLake is a **single**, **unified**, **logical data lake** designed for your entire organization. Similar to **OneDrive** for documents, OneLake serves as the central repository for all your analytics data within the **Microsoft Fabric** ecosystem.
- **Data Factory**: Data Factory is a crucial tool for building and managing data pipelines within the Microsoft Fabric environment. It provides a flexible and powerful way to connect to various data sources, perform data transformations, and ensure data quality for downstream analytics.
- **Synapse Data Engineer**: As a Synapse Data Engineer, you play a vital role in designing, building, and maintaining data pipelines within Azure Synapse Analytics. Working closely with various data sources, perform essential data transformations and ensure data quality for subsequent analysis.

- **Synapse Data Warehousing, Synapse Data Science, and Synapse Real-Time Analytics**: These advanced solutions offer sophisticated data analysis capabilities, from batch data storage to real-time analytics and data science. Provide organization with the necessary tools to explore, analyze, and visualize data effectively, from building predictive models to generating dynamic analytical reports.

- **Power BI**: Power BI is a powerful tool for turning data into insightful and meaningful information. With deep integration with the Microsoft Fabric ecosystem, Power BI allows to visualize data from OneLake and other data sources easily and flexibly. This helps you grasp critical insights and make informed decisions based on real-time data.  

- **Data Activator**: Data Activator help Real-time detection and monitoring of data that can trigger notifications and actions when it finds specified patterns in data.

# **2. Data Architecture**

## 2.1. Conceptual Architecture base on Fabric
![Items (1)](https://github.com/thanhphat2609/Global_Super_Store/assets/84914537/600e237e-01d7-4c09-891c-1551acfbc45e)

- **Data Source**: These include the various systems from which data is **extracted**, such as: Relational Database, File systems, SaaS applications, Real-time data.
- **Staging**: Extract data from Source into Files of Lakehouse (csv, parquet) or Delta Tables.
- **Data Warehouse**: Data in the data warehouse is organized according to a unified data model, which makes it easy to query and analyze.
- **Analytics**: This last step we will use tools and techniques to analyze the data in the data warehouse, such as: Power BI, Tableau, ..

## 2.2. Physical Architecture
![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/7a179ac4-2ded-4903-9929-fe7c6551f8db)

- **Data Source** Layer: This layer is responsible for collecting and storing data from various sources, such as retail transaction data and customer data.

- **Data Transformation** Layer: Initially, data from the Source will be loaded into the Bronze layer (Files in Lakehouse) and stored in parquet format through a Pipeline (Source_to_Bronze). The data will then be validated and transformed, and stored in Delta format in the Silver layer (Tables in Lakehouse). Similar to the Bronze layer, there will be a Pipeline responsible for this task (Bronze_to_Silver). After obtaining data from the Silver layer, we proceed to create Dim and Fact tables in the Gold layer and upload them to Power BI using Direct Lake connectivity.

- **Reporting**: This layer is responsible for presenting data from the application layer to users in an understandable manner. This may include using web interfaces, mobile applications, or desktop applications.
  
# **3. Building End to End solutions**

## 3.1. Dataset

Look at **Data_Dictonary.xlxs**


## 3.2. Orchestration (Data Catalog)

- **config_table**

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/ba5ae819-530f-46a0-9aa7-c456dbe752a3)




## 3.3. Building Master Pipeline
- Create **Data Gateway Connection** for Fake Customer DB Source
![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/8b14e41a-6a42-465d-a821-b88301e41eae)

- Config ** Data Gateway **
![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/1b8202b3-9a5f-47a1-9182-f0c436d4da45)


- Items in Fabric
**DEV**
![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/e4b0f8f1-a459-4b47-a568-cf5df57a91b1)

**UAT**
![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/962122dd-5136-4417-8094-713f2b205de3)


**META**
![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/cd649bd8-ab9a-4016-8e64-dbd316b1a8d4)



- Notebook

| **Notebook**          | **Meaning** |
|-------------------|-------------- |
|Bronze_Transformation| Transform data from Lakehouse_Bronze and save as Delta table |


- Master Pipeline

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/8772c116-9154-41ae-a926-9a4ff170218d)

**Source to Bronze Child Pipeline**

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/aa2025b9-a562-4b74-92cf-d6bb904c996d)

**Silver to Gold Child Pipeline**

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/24b7b398-0c0a-4ca6-b6a3-610b05d464a1)




- Results

**Master Pipeline**

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/067e289e-6956-414d-b8c9-41b7b1526d0d)


 
**Source -> Bronze**

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/4d79388b-9718-4a9f-b586-3c88fca7c28a)

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/da346e5c-e6b4-46c2-a41e-ed8c1a0204a1)


**Bronze -> Silver**

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/66399679-2ca6-4219-af3f-b8484234553d)

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/9c40584d-3f40-4f95-86bf-55c4cc4035fe)


**Gold**

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/a8565d64-18a3-4711-a4d4-380fcd9fe8dd)



**Log_Data**
![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/74e78d30-4111-48be-87cb-b480348c9272)

1. Source to Bronze

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/68979b8f-ac1a-400e-8ab4-4289e1facd36)

2. Bronze to Silver

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/e1d0d0b2-696e-4f3a-9385-ff394aa7d418)




# 4. Power BI

## 4.1. Data Model


### 4.1.1. Data Modelling Power BI

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/f9b0e9fe-87f7-4777-b59e-255e109c0df6)


### 4.1.2. Manage Relationships

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/8a021161-7737-4412-acee-45f83f9932ce)



## 4.2. Report
**Home**

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/df69bff2-ced6-42ff-883d-2c4c460d6115)

**Summary**

**Stores**

**Products**

**Customers**

**Report Change Log**

![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/52db1c7e-2d8c-4dea-bee2-caa01fe70d61)


# 5. Conclusion
Through project, its helps me alot to improve my skill in PySpark, not base on too much Fabric Warehouse.


# 6. Lesson Learned
1. Know how to log by using PySpark. Can log SparkAppID, SparkAppName, RowInserted, RowUpdated like using Procedure.
2. Reducing time by not using much Warehouse for read and write data because of Warehouse.
3. PySpark skills just enough, must upgrade skills.


# 7. Next step
1. Create just one Lakehouse_Job for 2 phase Bronze and Silver
2. Optimize code for reducing time
3. Log more field like userID, userName last change Data Model or Notebook

