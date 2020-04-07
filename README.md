# tunaiku
All Script and Data are located inside "tunaiku" forlder
1. Split a file which has n number of schema def. And store them in a dict of lists(no 3rd party imports)
input : a text file with comma delimiter has around 15 different schema data , split it accordingly

2. Regular expressions to remove unicode, delimiters, carriage returns all in one expression
input : some records have invisible unicode characters embedded in the strings, identify them

3. Load a file having size > 2gb from google cloud storage to a bigquery table by python

4. Explain and differentiate about dispositions in bq load job and query jobs, how to handle the data type changes in a file to bq, share a example code to load a json or csv file which have data type changes (integer in one record and string in the next record , float in one record and int in next record for a given field)

5. Implement a test SCD2 table in BQ, explain about the SCD2 tables

6. Add or alter the schema of a bq table whenever there is a new field added to a file or table from the source after a certain period of time in future
input : a input file has 10 columns today and after 1 week there are 12 columns , handle the schema 

7. Split a json tree having multiple table structures using python

8. Get the collections from a mongodb object with a date range filter using python 
example: get the data records for one day in a given table/object in mongodb

