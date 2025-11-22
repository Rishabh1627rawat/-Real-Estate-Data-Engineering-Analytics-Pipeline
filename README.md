# 🏡 Real-Estate Data Engineering & Analytics Pipeline

**End-to-end real-time data pipeline for property insights using Kafka, Airflow, PySpark, Snowflake, dbt & Streamlit.**

---

## 📌 Overview

In the real-estate industry, property information is spread across multiple listing platforms such as 99acres, MagicBricks, Housing.com etc. Each platform publishes thousands of property listings daily — including price, size, location, property type, amenities, and seller details. However, this data is highly fragmented, inconsistent, and unstructured.

Prices for the same property can differ across websites, property types may be defined differently (e.g., 2 BHK, 2 Bedroom, 2-Room), and location names vary by user input. Additionally, property listings constantly change due to price revisions, availability changes, and new inventory, making it difficult to track real-time market movements and historical trends.

Because of the lack of a centralized, automated data pipeline, real-estate companies, investors, and pricing analysts face major problems:

Delayed decision-making due to manual data collection and cleaning

Inaccurate price recommendations due to inconsistent or outdated listings

No visibility into long-term trends (e.g., how prices changed over months/years)

Difficulty identifying top performing cities or declining markets

No analytical layer to answer key questions like:

Which city is most affordable to buy in vs rent?

Which areas are showing the highest annual growth?

What’s the price difference per sq.ft based on property type or locality?

These limitations impact buyers, sellers, real-estate platforms, and investors — leading to poor investment decisions, pricing errors, and lost business opportunities.

🎯 Goal of the Project

The goal of this project is to build an end-to-end automated pipeline that:

Continuously collects real property listing data from multiple sources via web scraping

Normalizes, cleans, and transforms the data for consistency

Stores optimized and structured data in a warehouse for fast analytical queries

Provides dashboards and insights to support data-driven real-estate decision making

---

## 🧠 Problem Statement

Real-estate decision makers (buyers, sellers, investors, listing platforms) face challenges due to:

| Problem                               | Solution                             |
| ------------------------------------- | ------------------------------------ |
| Messy, inconsistent property listings | PySpark standardization & cleaning   |
| No visibility of historical trends    | dbt snapshots & versioned models     |
| Manual reporting of metrics           | automated dbt pipelines              |
| Hard to identify price growth cities  | Streamlit-based analytical dashboard |
| Slow & unstructured processing        | Snowflake warehouse for fast queries |

---

## 🏗 Architecture

```
Apache Airflow (Scheduler)
        ↓ triggers
Python Web Scraper / Producer Script
        ↓ publishes
Kafka Producer → Kafka Topic
        ↓
Kafka Console Consumer (for stream readability)
        ↓
PySpark ETL (Cleaning & Transformation)
        ↓
AWS S3 / Local Storage
        ↓
Snowflake Data Warehouse
        ↓
dbt Models (Facts, Dimensions & Snapshots)
        ↓
Streamlit Dashboard (Visual Analytics)
```

---

## 🔧 Technologies Used

| Category                | Tools          |
| ----------------------- | -------------- |
| Automation / Scheduling | Apache Airflow |
| Streaming               | Apache Kafka   |
| Processing              | PySpark        |
| Storage                 | AWS S3 / Local |
| Data Warehouse          | Snowflake      |
| Modeling                | dbt            |
| Visualization           | Streamlit      |
| Languages               | Python, SQL    |

---

## 📦 Core Features

* Real web scraping from public real-estate pages (e.g., 99acres)
* Automated ingestion triggered via Airflow DAG
* Streaming simulation using Kafka Producer & Console Consumer
* ETL transformation using PySpark
* Snowflake warehouse + dbt analytical models
* Interactive dashboard for insights & affordability scores

---

## 📊 Sample Insights Produced

* Average price by city & property type
* Year-over-year growth rates
* Affordability comparison (Rent vs Buy)
* Trending / declining investment cities

---

## 🚀 How to Run

### Start Kafka

```bash
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
```

### Create Kafka Topic

```bash
kafka-topics.sh --create --topic real_estate_stream --bootstrap-server localhost:9092
```

### Trigger scraper via Airflow

```bash
airflow dags trigger real_estate_ingestion_dag
```

### Consume stream

```bash
kafka-console-consumer.sh --topic real_estate_stream --bootstrap-server localhost:9092
```

### Run Streamlit Dashboard

```bash
streamlit run streamlit_dashboard/app.py
```

---

## 📂 Folder Structure

```
real-estate-data-pipeline/
├── airflow/dags/
├── kafka_ingestion/
│   ├── producer.py
│   ├── consumer.py
├── spark_etl/
│   └── spark_cleaning_job.py
├── snowflake_dbt/
│   └── models/
└── streamlit_dashboard/
    └── app.py
```

---

## 🔮 Future Enhancements

* Full Airflow orchestration across each pipeline stage
* Kafka streaming consumer using Spark Structured Streaming
* ML model for price prediction
* Deployment with CI/CD

---

## 👨‍💻 Author

**Rishabh Rawat**
Data Engineering | PySpark | Airflow | Cloud | Streaming | Analytics
📍 Jaipur, India
🔗 GitHub: [https://github.com/Rishabh1627rawat](https://github.com/Rishabh1627rawat)
🔗 LinkedIn: www.linkedin.com/in/rishabh-rawat-6921b017a

---

## ⭐ Contribute / Support

If you like this project, **please star ⭐ the repository** — it motivates more builds like this!
