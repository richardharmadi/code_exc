#hdfs dfs -cat /data/assignments/ex2/part2/stackSmall.txt| ./mapper-prep.py | sort -k1 | ./reducer-prep.py | ./mapper.py | sort -k1nr | ./reducer.py 
hdfs dfs -rm -r /user/$USER/assignment2/pretask3
hdfs dfs -rm -r /user/$USER/assignment2/task3

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.map.output.key.field.separator=";" \
-D num.key.fields.for.partition=1 \
-D mapreduce.partition.keypartitioner.options=-k1 \
-input /data/assignments/ex2/part2/stackLarge.txt/ \
-output /user/$USER/assignment2/pretask3 \
-mapper mapper-prep.py \
-file mapper-prep.py \
-combiner combiner-prep.py \
-file combiner-prep.py \
-reducer reducer-prep.py \
-file reducer-prep.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapred.reduce.tasks=1 \
-D mapred.text.key.comparator.options=-k1nr \
-input /user/$USER/assignment2/pretask3 \
-output /user/$USER/assignment2/task3 \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py

hdfs dfs -cat /user/$USER/assignment2/task3/* > output.out
