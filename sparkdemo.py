from pyspark import SparkContext

sc = SparkContext('local[2]', 'pyspark tutorial')

l = [1,2,3,4,45,5]


rdd = sc.parallelize(l)


print(rdd.collect())