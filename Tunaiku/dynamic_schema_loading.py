

import requests
from google.cloud import storage
from google.cloud import bigquery
import pandas as pd
import gcsfs
import pandas_gbq
import os

# Construct client objects.
clientbq = bigquery.Client()
clientst = storage.Client()

def auto_detecting_schema(uri,dest_table):
    dataset_id = 'sample_submission'
    dataset_ref = clientbq.dataset(dataset_id)
    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.source_format = bigquery.SourceFormat.CSV
    # uri = "gs://cloud-samples-data/bigquery/us-states/us-states.json"
    load_job = clientbq.load_table_from_uri(
        uri, dataset_ref.table("{}".format(dest_table)), job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print("Job finished.")

    destination_table = clientbq.get_table(dataset_ref.table("{}".format(dest_table)))
    print("Loaded {} rows.".format(destination_table.num_rows))

def get_table_info(projectid,dataset,tablename):  
    sql = """
    select column_name,data_type from `{projectid}`.{dataset}.INFORMATION_SCHEMA.COLUMNS where table_name='{tablename}';
    """.format(projectid=projectid,dataset=dataset,tablename=tablename)
    df = pandas_gbq.read_gbq(sql, project_id=projectid)
    return(df)

def is_dtype_same(row):
    if row['data_type_x'] == row['data_type_y']:
        val = True
    else:
        val = False
    return val

def is_new_col(row):
    if pd.isnull(row['data_type_y']):
        val = True
    else:
        val = False
    return val

def add_new_col_bq(table_id,colname,dtype):
    #table_id->your-project.your_dataset.your_table_name
    # table_id = "your-project.your_dataset.your_table_name"
    table = clientbq.get_table(table_id)  # Make an API request.
    original_schema = table.schema
    new_schema = original_schema[:]  # Creates a copy of the schema.
    new_schema.append(bigquery.SchemaField("{}".format(colname), "{}".format(dtype)))

    table.schema = new_schema
    table = clientbq.update_table(table, ["schema"])  # Make an API request.
    if len(table.schema) == len(original_schema) + 1 == len(new_schema):
        print("'{colname}' column with data type '{dtype}' has been added.".format(colname=colname,dtype=dtype))
    else:
        print("'{colname}' column with data type '{dtype}' has not been added.".format(colname=colname,dtype=dtype))

def schema_check(df_bq,uri):
    df = pd.read_csv(uri)
    info=df.dtypes
    df_dest=df_bq
    df_src = pd.DataFrame(columns=['column_name', 'data_type'])
    for col_name in info.index:
        df_src = df_src.append({'column_name':col_name , 'data_type': str(info[col_name]).upper()}, ignore_index=True)
    df_check=pd.merge(df_src, df_dest, how='left', left_on='column_name', right_on='column_name')
    df_check.data_type_x=df_check.data_type_x.apply(lambda x: 'STRING' if 'OBJECT' in x else x)
    df_check['dtypes_similarities']=df_check.apply(is_dtype_same,axis=1)
    df_check['is_new_col']=df_check.apply(is_new_col,axis=1)
    return df_check

def main():
    print("program is running..")
    first_file="sample1.csv"
    second_file="sample2.csv"
    projectid='charged-atlas-267313'
    dataset='sample_submission'
    tablename='sample_2'
    table_id='{projectid}.{dataset}.{tablename}'.format(projectid=projectid,dataset=dataset,tablename=tablename)
    print("first data from {} contain 2 columns is inserted..".format(first_file))
    uri1 = "gs://sample-alpha/{}".format(first_file)
    print("First data is loading..")
    auto_detecting_schema(uri1,tablename)

    print("second data from {} contain 4 columns is inserted..".format(second_file))
    uri2 = "gs://sample-alpha/{}".format(second_file)
    df_info=get_table_info(projectid,dataset,tablename)
    checking=schema_check(df_info,uri2)
    add_cols=checking['column_name'][checking['is_new_col']==True].values
    for col_name in add_cols:   
        print("the new column name '{}' is detected and it will be added to destination table".format(col_name)) 
        dtype=checking['data_type_x'][checking['column_name']==col_name].values
        print("with data type '{}'".format(dtype[0]))
        add_new_col_bq(table_id,'{}'.format(col_name),'{}'.format(dtype[0]))
    auto_detecting_schema(uri2,tablename)
    print("complete!!")
    

if __name__ == '__main__':
    main()   

