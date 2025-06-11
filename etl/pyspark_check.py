import os
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-11"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin;" + os.environ["PATH"]

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TestSparkSession") \
    .getOrCreate()

spark.range(5).show()
