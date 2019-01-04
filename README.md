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

User Recomendation
<table>
<tr><td>   user</td><td>     recommendations</td></tr>
<tr><<td>   3175</td><td>[[4295, 0.0104270...</td></tr>
<tr><td>   7340</td><td>[[1205, 0.4195645...</td></tr>
<tr><td>   8389</td><td>[[606, 0.15810448...</td></tr>
<tr><td>1000190</td><td>[[4951, 1.2102714...</td></tr>
<tr><td>1001043</td><td>[[1854, 0.7163441...</td></tr>
<tr><td>1001129</td><td>[[979, 1.0346313]...</td></tr>
<tr><td>1001139</td><td>[[59, 1.0844814],...</td></tr>
<tr><td>1002431</td><td>[[4267, 0.3903462...</td></tr>
<tr><td>1002605</td><td>[[1000113, 0.4840...</td></tr>
<tr><td>1004666</td><td>[[1256375, 1.4764...</td></tr>
</table>

Artist Recomendatins


<table>
<tr><td></td><td>artistId</td><td>     recommendations</td><td></td></tr>
<tr><td>+--------+--------------------+</td></tr>
<tr><td></td><td>     463</td><td>[[2223246, 1.6415...</td><td></td></tr>
<tr><td></td><td>     496</td><td>[[2049131, 0.4603...</td><td></td></tr>
<tr><td></td><td>     833</td><td>[[2058707, 1.6759...</td><td></td></tr>
<tr><td></td><td>    1088</td><td>[[2020632, 0.0259...</td><td></td></tr>
<tr><td></td><td>    1342</td><td>[[1059334, 0.0375...</td><td></td></tr>
<tr><td></td><td>    1580</td><td>[[2058707, 0.0203...</td><td></td></tr>
<tr><td></td><td>    1829</td><td>[[1077252, 0.2083...</td><td></td></tr>
<tr><td></td><td>    2122</td><td>[[2083814, 0.1416...</td><td></td></tr>
<tr><td></td><td>    2366</td><td>[[2058707, 0.2944...</td><td></td></tr>
<tr><td></td><td>    2866</td><td>[[2058707, 0.0043...</td><td></td></tr>
<tr><td>+--------+--------------------+</td></tr>
</table>

recomending for  users :

<table>
<tr><td>+-------+--------------------+</td></tr>
<tr><td></td><td>   user</td><td>     recommendations</td><td></td></tr>
<tr><td>+-------+--------------------+</td></tr>
<tr><td></td><td>1000070</td><td>[[82, 1.1568698],...</td><td></td></tr>
<tr><td></td><td>1000061</td><td>[[1002270, 0.2125...</td><td></td></tr>
<tr><td></td><td>1000313</td><td>[[1205, 0.2034896...</td><td></td></tr>
<tr><td>+-------+--------------------+</td></tr>
</table>

artist recomendation :

<table>
<tr><td>+--------+--------------------+</td></tr>
<tr><td></td><td>artistId</td><td>     recommendations</td><td></td></tr>
<tr><td>+--------+--------------------+</td></tr>
<tr><td></td><td>    3327</td><td>[[1070932, 1.3901...</td><td></td></tr>
<tr><td></td><td> 1001008</td><td>[[1060352, 0.9469...</td><td></td></tr>
<tr><td></td><td>    2184</td><td>[[1059334, 0.8299...</td><td></td></tr>
<tr><td>+--------+--------------------+</td></tr>
</table>


only showing top 10 rows


