# -*- coding: utf-8 -*-

import sys
import os

os.chdir('/Users/zieft/Local_Documents/PycharmProjects/MongoDB/lesson_4/Inserting_Multiple_Documents')
sys.path.append(os.getcwd())  # 将autos.py所在的文件夹加入到sys.path中，这样才能从autos中import函数。
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

    insert_autos('/Users/zieft/Local_Documents/PycharmProjects/MongoDB/lesson_4/Inserting_Multiple_Documents/autos-small.csv', db)
    print db.autos.find_one()
