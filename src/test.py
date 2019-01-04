
## imports
from pyspark.sql import SparkSession
import numpy as np
import pandas as pd
import re
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS

## creating the spark Session
spark = SparkSession.builder.master("spark://namenode:7077").appName("Recomendation").config("spark.submit.deployMode", "client").getOrCreate()


## reading data form the hdfs
user_artist_data = spark.sparkContext.textFile("hdfs://namenode:8020/music/user_artist_data.txt")
print(user_artist_data.getNumPartitions())

print(user_artist_data.count())

spark.stop()