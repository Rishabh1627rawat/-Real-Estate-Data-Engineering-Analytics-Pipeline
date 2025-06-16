# 🏡 Real Estate Data Engineering & Analytics Pipeline

This project is an end-to-end data engineering and analytics pipeline for the real estate sector. It simulates real-time property data streaming using Kafka, performs batch processing using PySpark, stores cleaned data in a cloud data warehouse (Snowflake), and visualizes insights through a Streamlit dashboard. The project is designed to demonstrate my skills across both data engineering and data analytics domains.

---
📌 Problem Statement

In the real estate industry, decision-makers—like home buyers, investors, and listing platforms—struggle to make informed decisions due to **fragmented, messy, and delayed data**.  

Properties across cities show varying prices, trends, and demand. Without a centralized, automated pipeline to process and track this data, platforms cannot deliver **accurate price recommendations, trend forecasts, or inventory insights**.

### 🎯 Goal

Build an **end-to-end data engineering pipeline** that:

- Ingests raw real estate data from multiple sources
- Cleans, transforms, and models it using PySpark and dbt
- Stores data in Snowflake for fast analytics
- Visualizes trends through dashboards
- Automates the entire process using Apache Airflow

---


## 📌 Project Architecture

1. Real-time data simulation via Kafka  
2. Data ingestion and consumption using Kafka producer/consumer in Python  
3. ETL processing using PySpark  
4. Storage of cleaned data into Snowflake  
5. Business logic and modeling using dbt  
6. Data visualization and prediction using Streamlit  
7. Workflow orchestration using Apache Airflow  

---

Problem | Solution |
|--------|----------|
| ❌ Price inconsistency across listings | ✅ PySpark cleaning & standardization |
| ❌ No tracking of historical price changes | ✅ dbt Snapshots + time-based models |
| ❌ Manual reporting of average price or growth trends | ✅ Automated dbt models (avg_price_by_city, YoY growth) |
| ❌ Unclear which city/area is booming | ✅ Insights through Streamlit dashboard |
| ❌ Scattered & slow data processing | ✅ Automated Airflow pipeline + Snowflake speed 

## 🧠 Technologies Used

| Stack          | Tool/Tech                         |
|----------------|-----------------------------------|
| Streaming      | Apache Kafka                      |
| Processing     | PySpark                           |
| Storage        | AWS S3 (or local as fallback)     |
| Data Warehouse | Snowflake                         |
| Orchestration  | Apache Airflow                    |
| Modeling       | dbt                               |
| Visualization  | Streamlit                         |
| Programming    | Python, SQL                       |

---




### 📊 Core Features / Models

- `avg_price_by_city.sql`: Average property prices grouped by city
- `property_growth_rate.sql`: Year-over-Year growth in prices
- `listing_price_history.sql`: Snapshots to track changes over time
- `dim_city`, `dim_property_type`: Lookup dimensions
- `fact_listings`: Clean, analyzable listing data

---

### 📈 Results / Benefits

- 📍 Identify top-growing cities
- 🏷 Recommend pricing strategies based on city/tier
- 📉 Detect areas with falling trends
- 📊 Enable faster reporting and insights generation
- 🔁 Fully automated, low-maintenance pipeline

---

### 👨‍💼 Ideal Use Cases

- Real Estate Platforms (e.g., 99acres, MagicBricks)
- PropTech Startups
- Real Estate Investors
- Business Analysts in Housing Sector

---


## ✅ Project Timeline & Progress

| Week | Focus Area                             | Status         |
|------|----------------------------------------|----------------|
| 1    | Kafka Setup + Real-time Data Ingestion | ✅ Completed    |
| 2    | PySpark ETL & Silver Layer             | ✅ Completed    |
| 3    | Snowflake Integration + dbt Modeling   | ⏳ In Progress  |
| 4    | ML + EDA + Streamlit Dashboard         | ❌ Not Started  |
| 5    | Airflow DAG + Deployment               | ❌ Not Started  |

---

## 📦 Week 1 Summary – Real-time Data Ingestion with Kafka

- Simulated property listings using a Kafka Producer (Python)  
- Created Kafka Topic: `real_estate_stream`  
- Wrote Kafka Consumer to store data locally in JSON/CSV  
- Handled edge cases like malformed data and retry logic  
- Used sample datasets from Kaggle for simulation  

✅ **Output**: A stream of JSON-formatted real estate data flowing through Kafka to the local storage layer.

---

## 🔁 Week 2 Summary – PySpark ETL & AWS S3 Integration

- Set up the PySpark environment and read Kafka-consumed JSON files  
- Performed data cleaning, handling nulls and malformed rows  
- Generated Parquet files representing the **Silver Layer**  
- Uploaded transformed data to **AWS S3** using the AWS CLI  

✅ **Output**: Cleaned and partitioned Parquet files stored in AWS S3 for downstream processing and analytics.

---

## 🧊 Week 3 Progress – Snowflake Integration & dbt Modeling

- Created Snowflake account, configured roles, and created warehouse  
- Created external stage and file format for S3 data loading  
- Testing data load using `COPY INTO` from AWS S3 to Snowflake table  
- Initialized `dbt` project with connection to Snowflake  
- Started creating base models in dbt (`stg_properties.sql`, `stg_location.sql`)  
- Working on transformations for KPIs: average price, city-wise growth, etc.  

⏳ **Current Focus**: Completing model logic and testing with sample dashboards.

---

## 📂 Folder Structure

```bash
real-estate-data-pipeline/
│
├── kafka_ingestion/
│   ├── producer.py
│   ├── consumer.py
│   └── sample_data/
│
├── spark_etl/
│   └── spark_cleaning_job.py
│
├── snowflake_dbt/
│   ├── dbt_project/
│   └── models/
│
├── streamlit_dashboard/
│   └── app.py
│
├── airflow_dag/
│   └── dag.py
│
└── README.md
```

---

## 🚀 Upcoming Goals (Week 4)

- Finalize dbt models and test business KPIs  
- Start ML model for price prediction  
- Build interactive Streamlit dashboard with filters and charts  
- Begin visual demo integration

---

## 📸 Screenshots & Demo (to be added in Week 4)

_(Dashboard visuals and prediction UI will be shared here)_

---

## 👨‍💻 Author

- **Rishabh Rawat** – Data Engineering & Analytics Enthusiast  
- GitHub: [github.com/Rishabh1627rawat](https://github.com/Rishabh1627rawat)  
- LinkedIn: _(Add your profile here)_
