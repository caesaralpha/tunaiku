# tunaiku
All Script and Data are located inside "Tunaiku" folder
1. Split a file which has n number of schema def. And store them in a dict of lists(no 3rd party imports)
input : a text file with comma delimiter has around 15 different schema data , split it accordingly\
Answer:\
[click here!](https://github.com/caesaralpha/tunaiku/blob/master/Tunaiku/load_csv.py) to access the script which is located in /Tunaiku/load_csv.py and the input file is in /Tunaiku/dummy.csv

2. Regular expressions to remove unicode, delimiters, carriage returns all in one expression
input : some records have invisible unicode characters embedded in the strings, identify them\
Answer:\
The script can be accesssed in /Tunaiku/cleansing_with_regex.py or [click here!](https://github.com/caesaralpha/tunaiku/blob/master/Tunaiku/cleansing_with_regex.py) and the input file in /Tunaiku/dirty_sample.csv\
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/regex.PNG)

3. Load a file having size > 2gb from google cloud storage to a bigquery table by python\
Answer:\
Related script is in /Tunaiku/load_to_bq.py or [click here!](https://github.com/caesaralpha/tunaiku/blob/master/Tunaiku/load_to_bq.py) and the input file in /Tunaiku/sample_submission.rar
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide1_new.PNG)
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide2.PNG)
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide3.PNG)
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide4.PNG)

4. Explain and differentiate about dispositions in bq load job and query jobs, how to handle the data type changes in a file to bq, share a example code to load a json or csv file which have data type changes (integer in one record and string in the next record , float in one record and int in next record for a given field)\
I am not familiar with disposition actually. Nevertheless, for the use case, my idea is to collect the metadata both, for table and file like what I have demonstrate in the question number 5. Then, put the file data into data frame and convert the column based on target table in BQ. After that, insert the data frame by using insert statement in BQ query that is run on top of python (using import pandas_gbq)\
function example:\
*import pandas_gbq\
def run_bq_sql(project_id,sql):\
&nbsp;&nbsp;df = pandas_gbq.read_gbq(sql, project_id=project_id)\
&nbsp;&nbsp;return(df)*

5. Implement a test SCD2 table in BQ, explain about the SCD2 tables\
Answer:
SDC2 is actually a procedure or method how to keep track any update or new added row by providing technical field "updated_date" and "expired_date". So that, whenever we want to access the previous data, it can be gotten easily and understandble related to the data history.\
The sql script can be accessed in /Tunaiku/sdc2.sql or [click here!](https://github.com/caesaralpha/tunaiku/blob/master/Tunaiku/sdc2.sql)\
These are the previus condition between two tables, target table "sample_sdc2" and stagging table "sample_stg"
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/bbf1.PNG)
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/bbf2.PNG)
Use case:
Stagging table has new data and an updated quantity for target table. The expected result is the new product or data will be added and the updated value will be added as well then the expired date of previous data that has been updated will be filled by current date. It will be used to notify that the data is the past data and the new one has null value in expired date.
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/aaf1.PNG)

6. Add or alter the schema of a bq table whenever there is a new field added to a file or table from the source after a certain period of time in future
input : a input file has 10 columns today and after 1 week there are 12 columns , handle the schema \
Answer:\
The script can be accessed in /Tunaiku/dynamic_schema_loading.py or [click here!](https://github.com/caesaralpha/tunaiku/blob/master/Tunaiku/dynamic_schema_loading.py) and the sample files are in /Tunaiku/sample1.csv and sample2.csv\
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide11.PNG)
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide12.PNG)
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide13.PNG)

7. Split a json tree having multiple table structures using python
Answer:
Actually, I don't get the point of the question. So in my script, I just demonstrate how to select component in JSON data.\
The script can be accessed by [click here!](https://github.com/caesaralpha/tunaiku/blob/master/Tunaiku/j_parse.py) and the input file [click here!](https://github.com/caesaralpha/tunaiku/blob/master/Tunaiku/census-diversity.json)

8. Get the collections from a mongodb object with a date range filter using python 
example: get the data records for one day in a given table/object in mongodb\
Answer:
Script can be accessed in /Tunaiku/get_mongodb.py or [click here!](https://github.com/caesaralpha/tunaiku/blob/master/Tunaiku/get_mongodb.py) \
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/mongo.PNG)
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/mongo_r.PNG)


