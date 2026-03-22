from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Create Spark session
spark = SparkSession.builder \
    .appName("PySpark_Test") \
    .getOrCreate()

# Sample data (like a small dataset)
data = [
    ("Sanjay", "IT", 50000),
    ("Amit", "HR", 40000),
    ("Neha", "IT", 60000),
    ("Ravi", "Finance", 45000),
    ("Pooja", "HR", 42000)
]

columns = ["Name", "Department", "Salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

print("=== Original Data ===")
df.show()

# 🔹 Filter (Salary > 45000)
filtered_df = df.filter(col("Salary") > 45000)

print("=== Filtered Data (Salary > 45000) ===")
filtered_df.show()

# 🔹 Aggregation (Average salary by department)
agg_df = df.groupBy("Department").agg(avg("Salary").alias("Avg_Salary"))

print("=== Average Salary by Department ===")
agg_df.show()

# 🔹 SQL Query
df.createOrReplaceTempView("employees")

sql_df = spark.sql("""
    SELECT Department, COUNT(*) as emp_count
    FROM employees
    GROUP BY Department
""")

print("=== Employee Count by Department (SQL) ===")
sql_df.show()

# Stop Spark
spark.stop()