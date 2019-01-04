<h2>Project : Music recomendations</h2>

this is *my first ML project on apache spark* in destributed envirement.

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


