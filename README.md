🏡 Real Estate Data Engineering & Analytics Pipeline
This project is an end-to-end data engineering and analytics pipeline for the real estate sector. It simulates real-time property data streaming using Kafka, performs batch processing using PySpark, stores cleaned data in a cloud data warehouse (Snowflake), and visualizes insights through a Streamlit dashboard. The project is designed to demonstrate my skills across both data engineering and data analytics domains.

📌 Project Architecture
Real-time data simulation via Kafka

Data ingestion using Kafka producer/consumer in Python

ETL processing using PySpark

Storage of cleaned data in AWS S3 (using AWS CLI) for scalability and cloud integration

Cleaned data is loaded into Snowflake

Business logic and transformation using dbt

Data visualization and prediction using Streamlit

Workflow orchestration using Apache Airflow

🧠 Technologies Used
Stack	Tool/Tech
Streaming	Apache Kafka
Processing	PySpark
Storage	AWS S3 (via AWS CLI)
Data Warehouse	Snowflake
Orchestration	Apache Airflow
Modeling	dbt
Visualization	Streamlit
Programming	Python, SQL

✅ Project Timeline & Progress
Week	Focus Area	Status
1	Kafka Setup + Real-time Ingestion	✅ Completed
2	PySpark ETL & Silver Layer	✅ Completed
3	Snowflake Integration + dbt Modeling	⏳ In Progress
4	ML + EDA + Streamlit Dashboard	❌ Not Started
5	Airflow DAG + Deployment	❌ Not Started

📦 Week 1 Summary – Real-time Data Ingestion with Kafka
Simulated property listings using a Kafka Producer (Python)

Created Kafka Topic: real_estate_stream

Wrote Kafka Consumer to store data locally in JSON/CSV

Handled edge cases like malformed data and retry logic

Used sample datasets from Kaggle for simulation

✅ Output: A stream of JSON-formatted real estate data flowing through Kafka to local storage.

🧹 Week 2 Summary – PySpark ETL & Silver Layer
Set up PySpark environment

Read Kafka consumer output (JSON/CSV)

Cleaned and transformed data using PySpark

Converted raw data into Parquet files (Silver Layer)

Saved cleaned data to AWS S3 using AWS CLI

Handled inconsistent pricing formats, nulls, and data types

Data stored in organized, partitioned S3 directories

✅ Output: Cleaned and structured Parquet files stored in AWS S3 (Silver Layer), ready for Snowflake.

🧊 Week 3 – Load to Snowflake + SQL Modeling with dbt
🎯 Goal:
Push cleaned data to Snowflake

Learn and build SQL models in dbt

📚 Learn:
Snowflake concepts: Warehouses, tables, stages

dbt concepts: Models, seeds, sources, snapshots

Writing modular SQL models for business metrics

🛠️ Build:
Create Snowflake tables and load transformed Parquet data

Set up and initialize a dbt project

Write models such as:

avg_price_by_city

top_5_areas_by_growth

listings_by_property_type

📂 Folder Structure
go
Copy
Edit
real-estate-data-pipeline/
├── kafka_ingestion/
│   ├── producer.py
│   ├── consumer.py
│   └── sample_data/
├── spark_etl/
│   └── spark_cleaning_job.py
├── snowflake_dbt/
│   ├── dbt_project/
│   └── models/
├── streamlit_dashboard/
│   └── app.py
├── airflow_dag/
│   └── dag.py
└── README.md
📸 Screenshots & Demo (Coming Soon – Week 4)
Dashboard visuals and prediction interface will be added once Streamlit integration is completed.

☁️ Cloud & CLI Integration
AWS S3 is used as a central data lake for storing the Silver Layer output.

AWS CLI is configured for seamless upload of transformed files to S3 buckets.

This setup ensures cloud scalability, portability, and ease of Snowflake integration for large-scale analytics.

👨‍💻 Author
Rishabh Rawat – Data Engineering & Analytics Enthusiast
📂 GitHub: github.com/Rishabh1627rawat
