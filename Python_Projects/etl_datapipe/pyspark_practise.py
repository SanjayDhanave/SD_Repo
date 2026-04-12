from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("My App").getOrCreate()

df = spark.read.csv("D:\\Repository\\SD_Repo\\Python_Projects\\etl_datapipe\\sample.csv", header = True, inferSchema = True)

df.show()

spark.stop()