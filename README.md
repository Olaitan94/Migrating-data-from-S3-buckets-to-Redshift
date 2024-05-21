# Migrating-data-from-S3-buckets-to-Redshift

The startup has valuable datasets on songs and song play events, stored in JSON format across multiple S3 buckets. These datasets hold great potential for various strategic applications, such as trend analysis, user behavior analysis, and segmentation. Additionally, they can be leveraged to train machine learning models for personalized recommendations and user experience enhancements. However, in their current storage format, this data is not readily accessible for analytics.

To help them make good use I have built an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team.

## Data Modelling 

### Staging tables
I have created two staging tables, staging_songs & staging_events table which is where the songs data and log data will be held when extracted from the s3 buckets. This tables will also be used to move the data into the facts & dimension tables

### Final tables
To make data readily available for analytics, I have created a fact table and 4 dimension tables according to the star schema shown below 
1. songplays: this is a fact table that has the data on songs played by which artist at what time. It is extracted from log data
2. users: this is a dimension table which contains user information like name and level. It is also extracted from log data
3. songs: This is a dimension table which  has song info like title and length. It is extracted from song data
4. artists: This is a dimension table which has info on artist like the name and location. It is extracted from song data
5. time: This is a dimension table that has the units of time (hours, minutes etc.) for each timestamp. it is extracted from log data

   <img width="758" alt="Untitled" src="https://github.com/Olaitan94/Migrating-data-from-S3-buckets-to-Redshift/assets/93266165/fa954839-443e-4525-bb01-3f197262f8bb">


## Description of files
#### aws_cred.cfg
This document contains the credentials like access key, cluster info, s3 buckets arn for which redshift uses to interact with the s3 buckets 

#### sql_queries.py
This doc contains the queries used to create the staging and final tables,copying data from s3 buckets into staging tables as well as transforming data from staging tables into dimemsional tables. These queries are imported and utilized in create_tables.py & etl.py

#### create_tables.py
This doc contains commands for establishing connections to the warehouse and creating tables

#### etl.py
This doc contains commands for establishing connections to the warehouse, loading data into staging tables and inserting data from staging tables into the dimensional tables








