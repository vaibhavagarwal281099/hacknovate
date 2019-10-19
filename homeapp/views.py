from django.shortcuts import render
from pymongo import MongoClient

def index(request):
    string = "There is drainage problem in my locality. I have complained but nothing happened."
    client = MongoClient("mongodb://tarun:tarun@hacknovate-shard-00-00-stlyh.mongodb.net:27017,hacknovate-shard-00-01-stlyh.mongodb.net:27017,hacknovate-shard-00-02-stlyh.mongodb.net:27017/test?ssl=true&replicaSet=Hacknovate-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database("site_data")
    records = db.sample
    record_list = list(records.find())
     if request.method == "POST":
        name=request.POST('myvalue')
        print(name)
    return render(request, 'index.html', {'text':string, 'list':record_list})



   
    
