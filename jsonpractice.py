import json

this_is_a_file = open("./jsonfile.json",  "w")

SingerAndSongs = {
    "Sidhu Moosewala" : [ "295", "SYL", "The Last Ride", "Janaza"],
    "Karan Aujla" : ["Don't Look", "BTFU", "Gangsta", "Doctor"],
    "Anne-Marie" : ["2002", "Alarm", "Ciao-Adios", "Rockabye"],
    "Rotimi" : "in my bed",
    "Doja Cat" : [ "Juicy", "Vegas", "Candy", "Woman", "Need to Know", "Streets", "Get into it", "Kiss Me More"]
}

# python to json

jsontext = json.dumps(SingerAndSongs)
this_is_a_file.write(jsontext)
this_is_a_file.close()


print("*" * 30)

# load method to decode the json into python





