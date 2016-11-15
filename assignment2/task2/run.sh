#hdfs dfs -cat /data/assignments/ex2/part2/stackLarge.txt | ./mapper.py
hdfs dfs -rm -r /user/$USER/assignment2/task2

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapred.reduce.tasks=1 \
-D mapred.text.key.comparator.options=-k1nr \
-input /data/assignments/ex2/part2/stackLarge.txt \
-output /user/$USER/assignment2/task2 \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py

hdfs dfs -cat /user/$USER/assignment2/task2/* > output.out
