import pymongo

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["kaggledata"]
    col = db["sample"]
    query = { "date": "2007-01-05" }
    doc = col.find(query)

    for post in doc:
        print(post)
    

if __name__ == '__main__':
    main()   