#!/bin/bash
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-file ./task3-mapperInMapCombiner.py \
-mapper ./task3-mapperInMapCombiner.py \
-file ./task3-reducer.py \
-reducer ./task3-reducer.py \
-input /trip.txt \
-output /output-task3