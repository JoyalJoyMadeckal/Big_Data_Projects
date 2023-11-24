package rmit

import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.{FileSystem, Path}
import org.apache.spark.rdd.RDD
import org.apache.spark.SparkConf
import org.apache.spark.streaming.dstream.DStream
import org.apache.spark.streaming.{Seconds, StreamingContext}

// __author__ = Joyal Joy Madeckal (s3860476)

// Defining the object for performing all the tasks
object Assignment4 {

  /**
   * This function is responsible for the creation of the output directory. If the directory exists
   * already then the directory won't be created
   * @param directory - The name of the directory
   */
  def createOutputDirectory (directory:String):Unit ={
    if (!fs.exists(new Path (directory))) {
    fs.mkdirs (new Path (directory))
    }
  }

  /**
   * This function will be generating the required files for all the tasks.
   * @param rdd This is incoming file for the function
   * @param directory Directory name where the file has to be generated
   * @param task Name of the task
   * @tparam T Incoming datatype of RDD. This is a dynamic datatype
   */
  def writeFile[T](rdd:RDD[T], directory:String, task:String):Unit = {
    var fileCount: Int = 1
    var fileSuffix: String = "001"
//    Checking if the incoming file is having content
    if (!rdd.isEmpty()) {
//      The loop will generate the name of the file to be produced
          while (fs.exists(new Path(s"$directory/task$task-$fileSuffix"))) {
              fileCount += 1
              if (fileCount / 10 == 0) {
                fileSuffix = s"00$fileCount"
              } else if (fileCount / 10 >= 1 && fileCount / 10 <= 9) {
                fileSuffix = s"0$fileCount"
              } else {
                fileSuffix = s"$fileCount"
              }
            }
//      This block will generate the file for the different tasks
      if (task == "C" && totalFileCount != previousFileCount) {
        previousFileCount = totalFileCount
        rdd.saveAsTextFile(s"$directory/task$task-$fileSuffix")
      } else if (task != "C") {
        rdd.saveAsTextFile(s"$directory/task$task-$fileSuffix")
      }
    }
  }

  /**
   * This is the root method for the generation of the output file
   * @param wordCounts Consist of the data for generating the output
   * @param directory Directory name where the file has to be generated
   * @param task Name of the task
   * @tparam T Incoming datatype of RDD. This is a dynamic datatype
   */
  def createOutputFile[T] (wordCounts:DStream[T], directory:String, task:String) :Unit = {
    wordCounts.foreachRDD(rdd => writeFile(rdd, directory, task))
  }

  /**
   * This method is used to generate the co-occurrence of all the words
   * @param x The array of words in a line
   * @return The combinations of words
   */
  def formWordCombinations(x:Array[String]): Array[((String, String), Int)] = {
    var wordCombinations: Array[((String, String), Int)] = Array()
    for (i <- x) {
      for (b <- x) {
        if (i != b) {
          wordCombinations = wordCombinations :+ ((i, b), 1)
        }
      }
    }
    wordCombinations
  }

  /**
   * This function updates the state from the previous state of counts
   * @param newValues This is the new aggregated data with counts for the tuples
   * @param runningCount This is the previous data
   * @return The new counts after the updating
   */
  def updateFunction(newValues:Seq[Int], runningCount: Option[Int]): Option[Int] = {
    val newCount = runningCount.getOrElse(0) + newValues.sum
    Some(newCount)
  }

//  Defining some of the common variables.
  val fs: FileSystem = FileSystem.get(new Configuration())
  var totalFileCount: Int = 0
  var previousFileCount: Int = 0

  /**
   * This is the main function and will be executed when the streaming program starts
   * @param args The arguments passed by the user. Should be having 2 arguments. The first argument
   *             tells the folder to monitor and second one tells where the output has to be generated.
   */
  def main(args: Array[String]): Unit = {
//    Ensuring there are 2 arguments.
    if (args.length < 2) {
      System.err.println("There are not enough arguments. 2 arguments are required.")
      System.exit(1)
    }

//    Creating the streaming context and checkpoint directory.
    val sparkConf: SparkConf = new SparkConf().setAppName("HdfsWordCount").setMaster("local")
    val ssc: StreamingContext = new StreamingContext(sparkConf, Seconds(5))
    ssc.checkpoint(".")

//    Reading the stream data for task A
    val lines = ssc.textFileStream(args(0))
    val words = lines.flatMap(_.split(" "))
    val wordCounts = words.map(x => (x, 1)).filter(x => x._1.matches("^[A-Za-z]+$")).reduceByKey(_ + _)

//    This is required for tracking the incoming file counts.
    lines.foreachRDD(rdd => {
      if (!rdd.isEmpty()) {
        totalFileCount += 1
      }
    })

//    Output directory and task A file generation
    createOutputDirectory(args(1))
    createOutputFile(wordCounts, args(1), "A")

    //    Reading the stream data for task B
    val wordsByLine = lines.map(x => x.split(" ").filter(x => x.length >= 5))
    val wordCombinations = wordsByLine.map(formWordCombinations).flatMap(x => x)
    val wordCombinationsCount = wordCombinations.reduceByKey(_ + _)

//    task B file generation
    createOutputFile(wordCombinationsCount, args(1), "B")

//    Updating the state of the function by using updateStateByKey
    val runningCounts = wordCombinationsCount.updateStateByKey[Int](updateFunction _)

//    task C file generation
    createOutputFile(runningCounts, args(1), "C")

//  This is where the streaming context starts
    ssc.start()
    ssc.awaitTermination()
  }
}

