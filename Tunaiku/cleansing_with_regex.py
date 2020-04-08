import re

data_path = './dirty_sample.csv'
def cleansing(data_path):
    data=[]
    with open(data_path,encoding="utf8") as f:
        for line in f:
            data_line = re.sub(r"[^a-zA-Z0-9\s]*[\r(?!\n)]*","", line)
            data.append(data_line)
    return data

def ori_line(data_path):
    data=[]
    with open(data_path,encoding="utf8") as f:
        for line in f:
            data_line = line
            data.append(data_line)
    return data

def main():
    print("before cleansing: {}".format(ori_line(data_path)))
    print("after cleansing: {}".format(cleansing(data_path)))
    
if __name__ == '__main__':
    main()   