import getpass
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, count, lit
 
username = getpass.getuser()
spark = SparkSession. \
    builder. \
    appName(f'{username} - Word Count'). \
    master('yarn'). \
    getOrCreate()
 
lines = spark.read.text('/public/randomtextwriter/part-m-0000*'). \
    toDF('line')
 
word_count = lines. \
    select(explode(split('line', ' ')).alias('word')). \
    groupBy('word'). \
    agg(count(lit(1)).alias('word_count'))
 
word_count. \
    write. \
    mode('overwrite'). \
    csv(f'/user/{username}/word_count')
