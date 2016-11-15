#hdfs dfs -cat /data/assignments/ex2/part2/stackSmall.txt| ./mapper-prep.py | sort -k1,1n
hdfs dfs -rm -r /user/$USER/assignment2/pretask4
hdfs dfs -rm -r /user/$USER/assignment2/counttask4
hdfs dfs -rm -r /user/$USER/assignment2/task4

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D stream.map.output.field.separator=";" \
-D stream.num.map.output.key.fields=2 \
-D mapreduce.map.output.key.field.separator=";" \
-D num.key.fields.for.partition=1 \
-D mapred.text.key.comparator.options="-k1,1n -k2,2" \
-D mapred.text.key.partition.options=-k1,1 \
-input /data/assignments/ex2/part2/stackLarge.txt/ \
-output /user/$USER/assignment2/pretask4 \
-mapper mapper-prep.py \
-file mapper-prep.py \
-reducer reducer-prep.py \
-file reducer-prep.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input /user/$USER/assignment2/pretask4 \
-output /user/$USER/assignment2/counttask4 \
-mapper mapper-count.py \
-file mapper-count.py \
-reducer reducer-count.py \
-file reducer-count.py

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapred.reduce.tasks=1 \
-D mapred.text.key.comparator.options=-k1,1nr \
-input /user/$USER/assignment2/counttask4 \
-output /user/$USER/assignment2/task4 \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py

hdfs dfs -cat /user/$USER/assignment2/task4/* > output.out
