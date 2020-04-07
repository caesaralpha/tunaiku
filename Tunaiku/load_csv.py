data_path = './dummy.csv'

class my_dictionary(dict):  
    def __init__(self): 
        self = dict() 
    def add(self, key, value): 
        self[key] = value 

def read_csv(data_path):
    print("Data is loading..")
    d=open(data_path,encoding="utf8").readline() 
    count_col=len(d.split(','))
    result_dict=my_dictionary()
    for num in range (0,count_col):   
        data=[]
        with open(data_path,encoding="utf8") as f:
            # next(f)
            for line in f:
                data_line = line.split(',')
                data.append(data_line[num])
            result_dict.add('col_{num}'.format(num=num),data)
    return result_dict


def main():
    print("program is running..")
    csv_dict=read_csv(data_path)
    print(csv_dict)


if __name__ == '__main__':
    main()   