# -*- coding: utf-8 -*-
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys, but you have to extract the attributes from the "insr" tag
# and add them to the list for the dictionary key "insr"
import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def my_get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):  # 提取文本的方法
        data = {}
        data['fnm'] = author.find("fnm").text
        data['snm'] = author.find("snm").text
        data['email'] = author.find("email").text
        data['insr'] = []  # 将字典内部的list直接初始化在字典里面，大大简化了后面的工作
        for i in author.findall('insr'):
            data['insr'].append(i.attrib['iid'])  # 提取tag的方法
        authors.append(data)

    return authors


def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
            "fnm": None,
            "snm": None,
            "email": None
        }
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text

        authors.append(data)

    return authors


def test():
    solution = [{'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'},
                {'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'},
                {'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'},
                {'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'},
                {'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'},
                {'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'},
                {'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'},
                {'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]

    root = get_root(article_file)
    data = get_authors(root)

    assert data[0] == solution[0]
    assert data[1]["fnm"] == solution[1]["fnm"]


test()
