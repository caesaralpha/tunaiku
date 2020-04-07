

import requests
from google.cloud import storage
from google.cloud import bigquery
import os

# Construct client objects.
clientbq = bigquery.Client()
clientst = storage.Client()


def upload_to_gcs(dest_filename,dest_folder,lcl_filename,lcl_folder):
    print('upload {dest_filename} to {dest_folder} in GCS started..'.format(dest_filename=dest_filename, dest_folder=dest_folder))
    bucket = clientst.get_bucket('sample-alpha')
    dest_path = "%s/%s" % (dest_folder, dest_filename)
    blob = bucket.blob(dest_path)
    lcl_path= "%s/%s" % (lcl_folder, lcl_filename)
    blob.upload_from_filename(lcl_path)
    print("{} has been uploaded successfully".format(dest_filename))

def split_file(lines,path):
    print("split file in {} is started".format(path))
    cmd="split -l {lines} {path} ./data/sample_".format(lines=lines,path=path)
    print("run command {} in local os".format(cmd))
    split = os.system(cmd)
    filename_list = os.system("ls ./data/ > ./data/filename_list.txt")
    data=[]
    f=open("./data/filename_list.txt",encoding="utf8")
    for line in f:
        data_line=line.split("\n ")
        data.append(data_line)

    data=[str(i).replace("\\n']","") for i in data]
    data=[str(i).replace("['","") for i in data]
    x=0
    for f in data:
        if f!='filename_list.txt':
            if x<2 :
                insert_data=os.system("cat ./data/{output} > ./data/{output}.csv".format(output=f))
                del_tmp=os.system("rm ./data/{output}".format(output=f))
            else:
                add_header=os.system("head -1 {path} > ./data/{output}.csv".format(path=path,output=f))
                insert_data=os.system("cat ./data/{output} >> ./data/{output}.csv".format(output=f))
                del_tmp=os.system("rm ./data/{output}".format(output=f))
        x=x+1
    
    print("output file location at ./data/ with name sample_<combination pattern>--> ex:sample_aa")
    return data
    

def housekeeping(path):
    print("deleting file in {}/* is started".format(path))
    delete = os.system("rm -r {}/*".format(path))
    print("done!")

def load_csv_to_bq(uri):
    dataset_id = 'sample_submission'
    dataset_ref = clientbq.dataset(dataset_id)
    job_config = bigquery.LoadJobConfig()
    job_config.schema = [
        bigquery.SchemaField("row_id", "STRING"),
        bigquery.SchemaField("meter_reading", "STRING"),
    ]
    job_config.skip_leading_rows = 1
    job_config.source_format = bigquery.SourceFormat.CSV
    print(uri)
    load_job = clientbq.load_table_from_uri(
        uri, dataset_ref.table("sample"), job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print("Job finished.")

    destination_table = clientbq.get_table(dataset_ref.table("sample"))
    print("Loaded {} rows.".format(destination_table.num_rows))

def main():
    print("program is running..")
    lcl_path_file='C:/Users/CaesarIrawan/Documents/Kaggle/Tunaiku/sample_submission.csv'
    tmp_path='.data'
    dest_folder='data'
    lcl_folder='./data'
    preparation=housekeeping(lcl_folder)
    file_list=split_file(600000,lcl_path_file)
    for fname in file_list:

        fname_dest=fname+'.csv'
        if fname != 'filename_list.txt':
            upload_to_gcs(fname_dest,dest_folder,fname_dest,lcl_folder)  
            uri = "gs://sample-alpha/{dest_folder}/{filename}".format(dest_folder=dest_folder,filename=fname_dest)
            load_csv_to_bq(uri)

    print("complete!!")


if __name__ == '__main__':
    main()   

