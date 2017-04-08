from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27917/')

tesla_s = {
    "manufacturer": "Tesla Motors",
    "class": "full-size",
    "body style": "5-door liftback",
    "production": [2012, 2013],
    "model years": [2013],
    "layout": ["Rear-motor", "rear-wheel drive"],
    "designer": {
        "firstname": "Franz",
        "surname": "von Holzhausen"
    },
    "assembly": [
        {
            "country": "United States",
            "city": "Fremont",
            "state": "California"
        },
        {
            "country": "The Netherlands",
            "city": "Tilburg"
        }
    ]
}

db = client.examples
db.autos.insert(tesla_s)

for a in db.autos.find():
    pprint.pprint(a)
