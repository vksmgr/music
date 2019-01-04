
## imports
from pyspark.sql import SparkSession
import numpy as np
import pandas as pd
import re
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS

## creating the spark Session
spark = SparkSession.builder.master("spark://10.10.10.10:7077").appName("reco").getOrCreate()


## reading data form the hdfs
user_artist_data = spark.sparkContext.textFile("hdfs://10.10.10.10:8020/music/user_artist_data.txt")
#print(user_artist_data.getNumPartitions())

#for each in the python
def foreach(data):
    for i in data.take(10):
        print(i)
# foreach(user_artist_data)
#
# # converting the data it to the format
user_artist_data_df = user_artist_data.map(lambda line: line.split(" ")).map(lambda x: (int(x[0]),int(x[1]), int(x[2]))).toDF()

# foreach(user_artist_data_df);

#this will describe the data frame
# user_artist_data_df.show(5)

#show the dataframe
#user_artist_data_df.show(5)

# Renaming the columns
user_artist_data_df = user_artist_data_df.withColumnRenamed('_1', 'user')
user_artist_data_df = user_artist_data_df.withColumnRenamed('_2', 'artistId')
user_artist_data_df = user_artist_data_df.withColumnRenamed('_3', 'count')

#user_artist_data_df.agg({"user":"max", "user": "min","artist":"max", "artist":"min"}).show()

## To know the artist name we have to read the artist_data.txt file form the hdfs

artist_raw = spark.sparkContext.textFile("hdfs://namenode:8020/music/artist_data.txt")
# foreach(artist_raw)

def callme(line):
    newline = re.sub('\t', ' ', line)
    newline2 = re.sub(r'(?<=\d)\s+', ",,,", newline)
    return newline2.split(",,,")
def to_int(arr):
    if len(arr) == 1:
        arr.append("null")
    try:
        arr[0] = int(arr[0])
    except:
        arr[0] = 0

    return (arr[0], arr[1])
names = ['artistId', 'name']
artist_new = artist_raw.map(callme).map(to_int).toDF()
artist_name = artist_new.toDF(*names)

# artist_name.show(5)

artist_alias_raw = spark.sparkContext.textFile("hdfs://namenode:8020/music/artist_alias.txt")
#foreach(artist_alias_raw)

artist_alias = artist_alias_raw.map(callme).map(lambda x: (int(x[0]), int(x[1]))).toDF()
artist_alias = artist_alias.toDF('artistId', 'canonicalId')
# artist_alias.show(5)

# artist_name.show(5)

# user_artist_data_df.show(5)
# artist_name.where('artistId in (1208690, 1003926)').show()



# broadcast variable
#b_var = spark.sparkContext.broadcast(artist_alias)


## Fitting Model

(training, test) = user_artist_data_df.randomSplit([0.8, 0.2])
als = ALS(maxIter=5, regParam=0.01, userCol="user", implicitPrefs=True, itemCol="artistId", ratingCol="count", coldStartStrategy="drop")
model = als.fit(training)

prediction = model.transform(test)

evaluator = RegressionEvaluator(metricName="rmse", labelCol="count", predictionCol="prediction")

rmse = evaluator.evaluate(prediction)
print("Root-mean-square error = " + str(rmse))

userRecs = model.recommendForAllUsers(10)

artistRecs = model.recommendForAllItems(10)



#top 10 artist recomendations
users = user_artist_data_df.select(als.getUserCol()).distinct().limit(3)
userSubsetRecs = model.recommendForUserSubset(users, 10)


#top 10 user recommendations for a specified artist

artist = user_artist_data_df.select(als.getItemCol()).distinct().limit(3)
artistSubSetRecs = model.recommendForItemSubset(artist, 10)

print("Top 10 Recomendation : ")
userRecs.show(10)
print("============================")
artistRecs.show(10)
print("============================")
userSubsetRecs.show(10)
print("============================")
artistSubSetRecs.show(10)

spark.stop()