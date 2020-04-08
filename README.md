# tunaiku
All Script and Data are located inside "Tunaiku" forlder
1. Split a file which has n number of schema def. And store them in a dict of lists(no 3rd party imports)
input : a text file with comma delimiter has around 15 different schema data , split it accordingly
[click here!] (https://github.com/caesaralpha/tunaiku/blob/master/Tunaiku/load_csv.py) to access the script which is located in /Tunaiku/load_csv.py and the input file is in /Tunaiku/dummy.csv

2. Regular expressions to remove unicode, delimiters, carriage returns all in one expression
input : some records have invisible unicode characters embedded in the strings, identify them

3. Load a file having size > 2gb from google cloud storage to a bigquery table by python
Related script is in /Tunaiku/load_to_bq.py or [click here!](https://github.com/caesaralpha/tunaiku/blob/master/Tunaiku/load_to_bq.py) and the input file in /Tunaiku/sample_submission.rar
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide1.PNG)
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide2.PNG)
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide3.PNG)
![alt text](https://github.com/caesaralpha/tunaiku/blob/master/pic/Slide4.PNG)

4. Explain and differentiate about dispositions in bq load job and query jobs, how to handle the data type changes in a file to bq, share a example code to load a json or csv file which have data type changes (integer in one record and string in the next record , float in one record and int in next record for a given field)

5. Implement a test SCD2 table in BQ, explain about the SCD2 tables

6. Add or alter the schema of a bq table whenever there is a new field added to a file or table from the source after a certain period of time in future
input : a input file has 10 columns today and after 1 week there are 12 columns , handle the schema 

7. Split a json tree having multiple table structures using python

8. Get the collections from a mongodb object with a date range filter using python 
example: get the data records for one day in a given table/object in mongodb

