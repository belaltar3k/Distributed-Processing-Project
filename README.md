Hadoop MapReduce Weather Analysis

How to Run the Project

Follow these steps inside WSL Ubuntu.

1️⃣ Copy Dataset from Windows → WSL
cp /mnt/c/Users/belal/OneDrive/Desktop/College/7thTerm/Distributed/Project/toronto_climate.csv .

2️⃣ Start Hadoop Services
sudo service ssh start
start-dfs.sh
start-yarn.sh

3️⃣ Upload Dataset to HDFS
hdfs dfs -mkdir -p /data/weather
hdfs dfs -put toronto_climate.csv /data/weather/
hdfs dfs -ls /data/weather

4️⃣ Create and Prepare MapReduce Python Files
Year stats
nano mapper_year_stats.py
nano reducer_year_stats_csv.py
chmod +x mapper_year_stats.py
chmod +x reducer_year_stats_csv.py

Max temperature
nano mapper_max_temp.py
nano reducer_max_temp_csv.py
chmod +x mapper_max_temp.py
chmod +x reducer_max_temp_csv.py

Min temperature
nano mapper_min_temp.py
nano reducer_min_temp_csv.py
chmod +x mapper_min_temp.py
chmod +x reducer_min_temp_csv.py

5️⃣ Run MapReduce Jobs
A. Year Stats (avg mean temp + total precipitation)

Remove old output:

hdfs dfs -rm -r -f /output/year_stats_csv


Run job:

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /data/weather/toronto_climate.csv \
  -output /output/year_stats_csv \
  -mapper ./mapper_year_stats.py \
  -reducer ./reducer_year_stats_csv.py \
  -file mapper_year_stats.py \
  -file reducer_year_stats_csv.py


Export CSV:

hdfs dfs -cat /output/year_stats_csv/part-* > year_stats.csv

B. Highest Temperature of Each Year

Remove old output:

hdfs dfs -rm -r -f /output/max_temp_csv


Run job:

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /data/weather/toronto_climate.csv \
  -output /output/max_temp_csv \
  -mapper ./mapper_max_temp.py \
  -reducer ./reducer_max_temp_csv.py \
  -file mapper_max_temp.py \
  -file reducer_max_temp_csv.py


Export CSV:

hdfs dfs -cat /output/max_temp_csv/part-* > max_temp_per_year.csv

C. Lowest Temperature of Each Year

Remove old output:

hdfs dfs -rm -r -f /output/min_temp_csv


Run job:

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /data/weather/toronto_climate.csv \
  -output /output/min_temp_csv \
  -mapper ./mapper_min_temp.py \
  -reducer ./reducer_min_temp_csv.py \
  -file mapper_min_temp.py \
  -file reducer_min_temp_csv.py


Export CSV:

hdfs dfs -cat /output/min_temp_csv/part-* > min_temp_per_year.csv

6️⃣ Copy Final Results Back to Windows
cp year_stats.csv max_temp_per_year.csv min_temp_per_year.csv \
  /mnt/c/Users/belal/OneDrive/Desktop/College/7thTerm/Distributed/Project/

📄 Output Files

Once all jobs run successfully, you will have:

year_stats.csv

max_temp_per_year.csv

min_temp_per_year.csv

