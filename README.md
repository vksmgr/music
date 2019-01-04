<h2>Project : Music recomendations</h2>

this is **my first ML project on apache spark** in destributed envirement.

i installed hadoop 3.0.1 and apache spark 2
i have one namenode and 4 datanodes.

first i created the spark session using master node as namenode

data is stored in the hdfs so we i feach it.

## the data cleaning :
there are many unwanted things in data so to make it in proper format
i used the regular expression.


## choosing algorithm :
 as the data in proper format we need an ml algorithm to work on
 so i choose the [ALS](https://spark.apache.org/docs/latest/ml-collaborative-filtering.html) (alternating least squares)
 We need to choose a recommender algorithm that is suitable for this implicit feed‐back data. The data set consists entirely of interactions between users and artists’ songs. It contains no information about the users, or about the artists other than their names. We need an algorithm that learns without access to user or artist attributes. These are typically called collaborative filtering algorithms. For example, deciding that two users might share similar tastes because they are the same age is not an example of collaborative filtering. Deciding that two users might both like the same song because they play many other same songs is an example.
![alt text](data/img/b1.png)

## Model Accuracy :

to calculate model accuracy i have used the Root mean square error method

## Recomendations :
finally i calculate some recommendations for the user
top 10 recommendations for user
top 10 user for an artist


## Screenshots :

DAG while Running ALS :

![alt text](data/img/scr1.jpg)

DAG2 while calculating the Result

![alt text](data/img/scr2.jpg)


### Final Result :
Root-mean-square error = 18.78284225081599

+-------+--------------------+
|   user|     recommendations|
+-------+--------------------+
|   3175|[[4295, 0.0104270...|
|   7340|[[1205, 0.4195645...|
|   8389|[[606, 0.15810448...|
|1000190|[[4951, 1.2102714...|
|1001043|[[1854, 0.7163441...|
|1001129|[[979, 1.0346313]...|
|1001139|[[59, 1.0844814],...|
|1002431|[[4267, 0.3903462...|
|1002605|[[1000113, 0.4840...|
|1004666|[[1256375, 1.4764...|
+-------+--------------------+
only showing top 10 rows


