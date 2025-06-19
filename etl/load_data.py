from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType
from pyspark.sql.functions import regexp_extract, trim, when, col, split, lit
from dotenv import load_dotenv
import os

load_dotenv()

# Set Python interpreter for Spark
os.environ["PYSPARK_PYTHON"] = "C:/Users/nikhi/AppData/Local/Programs/Python/Python312/python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/nikhi/AppData/Local/Programs/Python/Python312/python.exe"

# Set AWS credentials (ensure these are set as environment variables before running)
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

if not aws_access_key or not aws_secret_key:
    raise ValueError("AWS credentials not set in environment variables.")

# Start Spark Session
spark = SparkSession.builder \
    .appName("RealEstateETL") \
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.6,com.amazonaws:aws-java-sdk-bundle:1.12.367") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.access.key", aws_access_key) \
    .config("spark.hadoop.fs.s3a.secret.key", aws_secret_key) \
    .config("spark.hadoop.fs.s3a.endpoint", "s3.ap-south-1.amazonaws.com") \
    .getOrCreate()

# Read function
def read_city_json(path, city):
    return spark.read.option("multiline", "true").json(path).withColumn("MAIN_CITY", lit(city))

# Read all city files
df1 = read_city_json("C:/Users/nikhi/Desktop/real-estate-data-project/data/Hyderabad.json", "Hyderabad")
df2 = read_city_json("C:/Users/nikhi/Desktop/real-estate-data-project/data/kolkata.json", "Kolkata")
df3 = read_city_json("C:/Users/nikhi/Desktop/real-estate-data-project/data/Mumbai.json", "Mumbai")
df4 = read_city_json("C:/Users/nikhi/Desktop/real-estate-data-project/data/Gurgaon.json", "Gurgaon")

# Combine data
join_data = df1.union(df2).union(df3).union(df4)
print(f"Total rows before cleaning: {join_data.count()}")

# Drop rows with critical nulls
cleansed_data = join_data.dropna(subset=[
    'PRICE', 'AGE', 'BEDROOM_NUM', 'CITY', 'PRICE_PER_UNIT_AREA',
    'PRICE_SQFT', 'PROPERTY_TYPE', 'PROP_ID', 'TOTAL_FLOOR'
])
print(f"Total rows after cleaning: {cleansed_data.count()}")

# Clean PRICE column
cleansed_data = cleansed_data.withColumn("PRICE", trim(col("PRICE")))
cleansed_data = cleansed_data.withColumn(
    "PRICE_CLEANED",
    when(col("PRICE").rlike(".*Cr.*"),
         regexp_extract(split(col("PRICE"), " - ")[0], r"([\d.]+)", 1).cast("float") * 10000000)
    .when(col("PRICE").rlike(".*L.*"),
         regexp_extract(split(col("PRICE"), " - ")[0], r"([\d.]+)", 1).cast("float") * 100000)
    .otherwise(None)
)


# Replace PRICE column
cleansed_data2 = cleansed_data.drop("PRICE").withColumnRenamed("PRICE_CLEANED", "PRICE")
cleansed_data2 = cleansed_data2.withColumn("PRICE", col("PRICE").cast(FloatType()))

# Add LABEL column
df_final = cleansed_data2.withColumn(
    "PRICE_CLEANED_LABEL",
    when((col("PRICE").isNull()) | (col("PRICE") == 0), "PRICE ON REQUEST")
    .otherwise(col("PRICE").cast("string"))
)

# Local write for testing
df_final.coalesce(1).write.mode("overwrite").partitionBy("MAIN_CITY") \
    .parquet("C:/Users/nikhi/Desktop/real-estate-data-project/silver_layer_parquet")

# Write to S3
try:
    df_final.write.mode("overwrite").partitionBy("MAIN_CITY") \
        .parquet("s3a://realestate-dataenginner-project/silver_layer_parquet/")
    print("✅ Successfully wrote to S3")
except Exception as e:
    print(f"❌ Failed to write to S3: {str(e)}")
