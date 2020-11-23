#copy hadoop streaming jar to local folder
#Create input and output folders in hdfs
#copy input data file to hdfs using hadoop fs -copyFrom Local localpath hdfspath

hadoop jar hadoop-streaming.jar/ -input testMapReduce/dataset -output testMapReduce/mapreduce-output -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py