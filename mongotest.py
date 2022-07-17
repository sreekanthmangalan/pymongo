import pymongo

client = pymongo.MongoClient("mongodb+srv://sreekanth_mangalan:ineuron@sreekanthdb.fspxrkc.mongodb.net/?retr"
                             "yWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"sreekanth",
    "email" : "sreekanth.mangalan@gmail.com",
    "surname" : "mangalan"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )