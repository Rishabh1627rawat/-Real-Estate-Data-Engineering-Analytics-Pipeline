from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType, IntegerType
from pyspark.sql.functions import regexp_extract, trim, when, col, split,udf,lit
import os 


os.environ["PYSPARK_PYTHON"] = "C:/Users/nikhi/AppData/Local/Programs/Python/Python312/python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/nikhi/AppData/Local/Programs/Python/Python312/python.exe"

spark = SparkSession.builder \
    .appName("RealEstateETL") \
    .config("spark.hadoop.io.nativeio.disable", "true") \
    .config("spark.hadoop.fs.s3a.access.key", "XXXXXXXXXXXXXX") \
    .config("spark.hadoop.fs.s3a.secret.key", "xxxxxxxxxxxxxxxxxxxxxx")\
    .config("spark.hadoop.fs.s3a.endpoint", "xxxxxxxxxxxxxxxxxxxxxxxx") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3FileSystem")\
    .config("spark.hadoop.fs.s3apath.stule.access","true")\
    .getOrCreate()


# Read multiline JSON (array of objects)
df1 = spark.read.option("multiline", "true") \
                .json("C:/Users/nikhi/Desktop/real-estate-data-project/data/Hyderabad.json") \
                .withColumn("MAIN_CITY", lit("Hyderabad"))

df2 = spark.read.option("multiline", "true") \
                 .json("C:/Users/nikhi/Desktop/real-estate-data-project/data/kolkata.json") \
                 .withColumn("MAIN_CITY", lit("Kolkata"))


df3 = spark.read.option("multiline", "true")\
                .json("C:/Users/nikhi/Desktop/real-estate-data-project/data/Mumbai.json") \
                .withColumn("MAIN_CITY", lit("Mumbai"))


df4 = spark.read.option("multiline", "true")\
                .json("C:/Users/nikhi/Desktop/real-estate-data-project/data/Gurgaon.json") \
                .withColumn("MAIN_CITY", lit("Gurgaon"))

# Show schema and sample data

df1.show(5, truncate=False)
df2.show(5, truncate=False)
df3.show(5, truncate=False)
df4.show(5, truncate=False)

join_data = df1.union(df2).union(df3).union(df4)

# join_data.show(10, truncate=False)

#checking data before cleaning the data
print(f"Total rows before cleaning the data: {join_data.count()}")

cleansed_data = join_data.dropna(subset=['PRICE','AGE','BEDROOM_NUM','CITY','PRICE','PRICE_PER_UNIT_AREA','PRICE_SQFT','PROPERTY_TYPE','PROP_ID','TOTAL_FLOOR'])
# cleansed_data.show(30, truncate=False)

#checking data after cleaning the data 
print(f"Total rows after droping the duplicates value {cleansed_data.count()}")


cleansed_data = cleansed_data.withColumn("PRICE", trim(col("PRICE")))


#Cleansed the data and change the column with in price column cr and L into numbers
cleansed_data = cleansed_data.withColumn("PRICE_CLEANED",
    when(col("PRICE").rlike(".*Cr.*"),
         regexp_extract(split(col("PRICE"), " - ")[0], r"([\d.]+)", 1).cast("float") * 10000000)
    .when(col("PRICE").rlike(".*L.*"),
         regexp_extract(split(col("PRICE"), " - ")[0], r"([\d.]+)", 1).cast("float") * 100000)
    .otherwise(None)
)

cleansed_data = cleansed_data.withColumn("PRICE_CLEANED", col("PRICE_CLEANED").cast(FloatType()))
cleansed_data2 = cleansed_data.drop("PRICE").withColumnRenamed("PRICE_CLEANED", "PRICE")

cleansed_data2.show(30, truncate=False)

df_cleansed_data = cleansed_data2.withColumn(
    "PRICE_CLEANSED_LABEL",
    when((col("PRICE").isNull()) | (col("PRICE")== 0), "PRICE ON REQUEST")
    .otherwise(col("PRICE").cast("string"))
)

df_cleansed_data.show(30, truncate=False)

# To this (using absolute path)
cleansed_data2.coalesce(1) \
    .write \
    .mode("overwrite") \
    .partitionBy("MAIN_CITY") \
    .parquet("C:/Users/nikhi/Desktop/real-estate-data-project/silver_layer_parquet")

cleansed_data2.write.mode("overwrite").partitionBy("MAIN_CITY").parquet("s3a://real-estate-dataenginner-project/silver_layer_parquet/")