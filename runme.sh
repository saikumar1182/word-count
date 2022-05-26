export PYSPARK_PYTHON=python3
export SPARK_MAJOR_VERSION=3

spark-submit \
   --master yarn \
   --conf spark.ui.port=0 \
   /home/itv002581/wordcount/word_count.py

