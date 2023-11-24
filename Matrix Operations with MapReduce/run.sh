#!/bin/bash
nrow_M=2
ncol_M=3
nrow_N=3
ncol_N=2
nrow_X=2
ncol_X=2

hadoop jar ./hadoop-streaming-3.1.4.jar \
-D stream.num.map.output.key.fields=3 \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.reduce.tasks=3 \
-file ./mapper.py \
-mapper "./mapper.py $nrow_M $ncol_M $nrow_N $ncol_N $nrow_X $ncol_X" \
-file ./reducer.py \
-reducer ./reducer.py \
-input /input \
-output /output \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner