# Global_Electronics_Retailer_Fabric
Build an End to End Data Engineer project for Analysis Global Electronics Retailer with Microsoft Fabric


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
![image](https://github.com/thanhphat2609/Global_Electronics_Retailer_Fabric/assets/84914537/b09eca19-b603-421b-9aad-6351736ad90c)


  
# **3. Building End to End solutions**

## 3.1. Dataset

Look at Data Dictonary.xlxs


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

**META**


- Notebook

| **Notebook**          | **Meaning** |
|-------------------|-------------- |
|Bronze_Transformation| Transform data from Lakehouse_Bronze and save as Delta table |


- Master Pipeline



**Source to Bronze Child Pipeline**



**Silver to Gold Child Pipeline**




- Results

**Pipeline**


 
**Source -> Bronze**



**Silver -> Gold**



**Log_Data**




# 4. Power BI

## 4.1. Data Model

### 4.1.1. Data Modelling Power BI



### 4.1.2. Manage Relationships
| **From Table**          | **To Table**     | **Relationship** | **Column for Relationship** |
|--------------------------|------------------|------------------|------------------------------|


## 4.2. Report

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

