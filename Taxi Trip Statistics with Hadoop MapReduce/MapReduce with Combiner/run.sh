#!/bin/bash
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-file ./task2-mapper.py \
-mapper ./task2-mapper.py \
-file ./task2-combiner.py \
-combiner ./task2-combiner.py \
-file ./task2-reducer.py \
-reducer ./task2-reducer.py \
-input /trip.txt \
-output /output-task2