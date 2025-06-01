
# 🏡 Real Estate Data Engineering & Analytics Pipeline

This project is an end-to-end data engineering and analytics pipeline for the real estate sector. It simulates real-time property data streaming using Kafka, performs batch processing using PySpark, stores cleaned data in a cloud data warehouse (Snowflake), and visualizes insights through a Streamlit dashboard. The project is designed to demonstrate my skills across both data engineering and data analytics domains.

## 📌 Project Architecture

1. Real-time data simulation via Kafka
2. Data ingestion and consumption using Kafka producer/consumer in Python
3. ETL processing using PySpark
4. Storage of cleaned data into Snowflake
5. Business logic and modeling using dbt
6. Data visualization and prediction using Streamlit
7. Workflow orchestration using Apache Airflow

## 🧠 Technologies Used

| Stack         | Tool/Tech                         |
|---------------|-----------------------------------|
| Streaming     | Apache Kafka                      |
| Processing    | PySpark                           |
| Storage       | AWS S3 (or local as fallback)     |
| Data Warehouse| Snowflake                         |
| Orchestration | Apache Airflow                    |
| Modeling      | dbt                               |
| Visualization | Streamlit                         |
| Programming   | Python, SQL                       |

## ✅ Project Timeline & Progress

| Week | Focus Area                             | Status       |
|------|----------------------------------------|--------------|
| 1    | Kafka Setup + Real-time Data Ingestion | ✅ Completed |
| 2    | PySpark ETL & Silver Layer             | ⏳ In Progress |
| 3    | Snowflake Integration + dbt Modeling   | ❌ Not Started |
| 4    | ML + EDA + Streamlit Dashboard         | ❌ Not Started |
| 5    | Airflow DAG + Deployment               | ❌ Not Started |

## 📦 Week 1 Summary – Real-time Data Ingestion with Kafka

- Simulated property listings using a Kafka Producer (Python)
- Created Kafka Topic: real_estate_stream
- Wrote Kafka Consumer to store data locally in JSON/CSV
- Handled edge cases like malformed data and retry logic
- Used sample datasets from Kaggle for simulation

✅ Output: A stream of JSON-formatted real estate data flowing through Kafka to the local storage layer.

## 📂 Folder Structure

\`\`\`bash
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
\`\`\`

## 🚀 Upcoming Goals (Week 2)

- Set up PySpark environment
- Transform Kafka output into cleaned Parquet files
- Move to Silver layer (intermediate storage)
- Begin writing transformation logic for later ML pipeline

## 📸 Screenshots & Demo (to be added in Week 4)

(Dashboard visuals and prediction UI will be shared here.)

## 👨‍💻 Author

- Rishabh Rawat – Data Engineering & Analytics Enthusiast  
- GitHub: https://github.com/Rishabh1627rawat  
- LinkedIn: (Add your profile here)
