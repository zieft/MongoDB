# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.split(os.path.abspath('autos'))[0])  # 将autos.py加入path，这样才能从autos中import
from autos import process_file



def insert_autos(infile, db):
    data = process_file(infile)

    # Your code here. Insert the data in one command
    # autos will be a list of dictionaries, as in the example in the previous video
    # You have to insert data in a collection 'autos'
    db.autos.insert(data)


if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('autos-small.csv', db)
    print db.autos.find_one()
