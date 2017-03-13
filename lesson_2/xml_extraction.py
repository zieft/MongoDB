import xml.etree.ElementTree as ET
import pprint

tree = ET.parse('exampleResearchArticle.xml')
root = tree.getroot()


title = root.find('./fm/bibl/title')
title_text = ""
for p in title:
    title_text += p.text
print "\nTitle:\n", title_text


print "\nAuthor email address:"
for a in root.findall('./fm/bibl/aug/au'):
    email = a.find('email')
    if email is not None:
        print email.text

