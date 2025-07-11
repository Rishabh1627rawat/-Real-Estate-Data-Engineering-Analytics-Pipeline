# 🏡 Real Estate Data Engineering & Analytics Pipeline

This project is an end-to-end data engineering and analytics pipeline for the real estate sector. It simulates real-time property data using Kafka, processes it using PySpark, stores the cleaned data in Snowflake, models key metrics using dbt, and visualizes insights through a Streamlit dashboard. The project is designed to demonstrate my skills across both **data engineering** and **analytics** domains.

---

## 📌 Problem Statement

In the real estate industry, decision-makers—like home buyers, investors, and listing platforms—struggle to make informed decisions due to **fragmented, messy, and delayed data**.  

Properties across cities show varying prices, trends, and demand. Without a centralized, automated pipeline to process and track this data, platforms cannot deliver **accurate price recommendations, trend forecasts, or inventory insights**.

---

### 🎯 Goal

Build an **end-to-end data engineering pipeline** that:

- Ingests raw real estate data from multiple sources
- Cleans, transforms, and models it using PySpark and dbt
- Stores data in Snowflake for fast analytics
- Visualizes trends through dashboards using Streamlit

---

## 📌 Project Architecture

1. Real-time data simulation via Kafka  
2. Data ingestion and consumption using Kafka producer/consumer in Python  
3. ETL processing using PySpark  
4. Storage of cleaned data into Snowflake  
5. Business logic and modeling using dbt  
6. Data visualization and insights using Streamlit  

---

## 🔍 What Business Problems This Solves

| Problem | Solution |
|--------|----------|
| ❌ Price inconsistency across listings | ✅ PySpark cleaning & standardization |
| ❌ No tracking of historical price changes | ✅ dbt Snapshots + time-based models |
| ❌ Manual reporting of average price or growth trends | ✅ Automated dbt models (avg_price_by_city, YoY growth) |
| ❌ Unclear which city/area is booming | ✅ Insights through Streamlit dashboard |
| ❌ Scattered & slow data processing | ✅ dbt + Snowflake fast pipeline |

---

## 🧠 Technologies Used

| Stack          | Tool/Tech                         |
|----------------|-----------------------------------|
| Streaming      | Apache Kafka                      |
| Processing     | PySpark                           |
| Storage        | AWS S3 (or local fallback)        |
| Data Warehouse | Snowflake                         |
| Modeling       | dbt                               |
| Visualization  | Streamlit                         |
| Programming    | Python, SQL                       |

---

## 📊 Core Features / Models

- `avg_price_by_city.sql`: Average property prices grouped by city
- `property_growth_rate.sql`: Year-over-Year growth in prices
- `listing_price_history.sql`: Snapshots to track changes over time
- `dim_city`, `dim_property_type`: Lookup dimensions
- `fact_listings`: Clean, analyzable listing data
- `fct_property_summary`: Affordability metrics, rent vs buy logic

---

## 📈 Results / Benefits

- 📍 Identify top-growing cities
- 🏷 Recommend pricing strategies based on city/tier
- 📉 Detect areas with falling trends
- 📊 Enable faster reporting and insights generation
- 🔁 Reusable and scalable dbt modeling pipeline

---

## 👨‍💼 Ideal Use Cases

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
| 3    | Snowflake Integration + dbt Modeling   | ✅ Completed    |
| 4    | Streamlit Dashboard + Visual Insights  | ⏳ In Progress  |
| 5    | ML Model + Deployment (Optional)       | ❌ Not Started  |

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

## 🧊 Week 3 Summary – Snowflake + dbt Modeling

- Created Snowflake warehouse, stage, and file format  
- Loaded S3 data into Snowflake using `COPY INTO`  
- Initialized and configured dbt project  
- Built core dbt models (fact & dimensions)
- Created `fct_property_summary` for buy-vs-rent logic and affordability

✅ **Output**: All property metrics modeled in Snowflake using dbt — ready for dashboarding.

---

## 📊 Week 4 Summary – Streamlit Dashboard

- Built interactive dashboard using Streamlit
- Added filters: city, property type, price range
- Visualized:
  - Average prices
  - Years to afford at 10% and 20% savings
  - Rent vs Buy recommendation (ratio)
- Used `fct_property_summary` dbt model as backend source

✅ **Output**: Working dashboard to compare affordability and buy-vs-rent across cities.

---

> 🔍 Note: Airflow was originally planned for pipeline orchestration, but this version focuses on the full data pipeline from ingestion to analytics via dbt and Streamlit. Future versions may integrate Airflow for automation.

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
└── README.md




## 📸 Screenshots & Demo (to be added in Week 4)

_(Dashboard visuals and prediction UI will be shared here)_

---

## 👨‍💻 Author

- **Rishabh Rawat** – Data Engineering & Analytics Enthusiast  
- GitHub: [github.com/Rishabh1627rawat](https://github.com/Rishabh1627rawat)  
- LinkedIn: _(Add your profile here)_
