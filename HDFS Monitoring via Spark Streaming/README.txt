This folder consists of the following files and submitted towards the completion of Assignment 4 for Big Data Processing
1. Assignment_4.jar - This is the executable file
2. Assignment4.scala - This is the source code for the project
3. README - Consists of the instructions to execute the program

The assignment consisted of tasks A, B and C.

For task A of the assignment the output will look like follow:
(<The word based on the specifications>, <The number of times the word has occured>)

For task B of the assignment the output will look like follow:
((<word, <co-occuring word>>), <Number of times co-occurence has happened>)

For task C of the assignment the output will look like follow:
((<word, <co-occuring word>>), <Number of times co-occurence has happened and even considers the previous state of execution>)

How to run the code?

1. Place the Assignment_4.jar in the cluster master node.
2. Execute the following command from hadoop and make sure that we are in the same directory as Assignment_4.jar 
   "spark-submit --class rmit.Assignment4 --master yarn --deploy-mode client Assignment_4.jar <the hdfs folder to be monitored> <folder to generate output>"
   For example, "spark-submit --class rmit.Assignment4 --master yarn --deploy-mode client Assignment_4.jar hdfs:///user/joyaljoymadeckal hdfs:///output"
3. The output files will be generated in the specified folder by the user. If the example command is followed, the folder structure looks like follow:
	output
			taskA-001
			taskA-002
			taskB-001
			taskB-002
			taskC-001
			taskC-002
			
			
Note: When executing the program if encountered an error which says <filename>.__COPYING__ don't exist just run it again and once the streaming context has properly started upload the files. The program will work and will generate the required files

References:

All the materials and code from Week 7,8 and 9