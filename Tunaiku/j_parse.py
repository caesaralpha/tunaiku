import json

data_path = './census-diversity.json'

def get_jdata(data_path):
    with open(data_path) as f:
        data = json.load(f)
        return data

def main():
    print("program is running..")
    a=get_jdata(data_path)
    print(a[0])

if __name__ == '__main__':
    main()   