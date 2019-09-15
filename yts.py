import requests
import json

#Listing Movies:

Gen = input("Enter Genre : ")
Qual = input("Enter Quality (720p, 1080p, 3D, All): ")
rating = input("Enter Minimum Rating ( 0 to 9) : ")
sort = input("Sort by (title, year, rating, peers, seeds, download_count, like_count, date_added): ")

payload = {"genre":Gen,"quality":Qual,"minimum_rating":rating,"sort_by":sort,"limit":"1"}


#yts api endpoint

list_movies="https://yts.lt/api/v2/list_movies.json"

g_list=requests.get(list_movies, params=payload)



#details_dictionary_call

detail = json.loads(g_list.content)["data"]["movies"][0]
download= json.loads(g_list.content)["data"]["movies"][0]["torrents"]


print(type(download))

#function to fetch movie details

def disp(key,string):
    print("\n",key," : ", detail[string])

#function to fetch download details

def down(key,Q,string):
    print("\n",key," : ", download[Q][string])

#function to download torrent file

def torrent(Q):
    filename=detail["title"]
    with open(filename+".torrent", "wb") as f:
        f.write(Q.content)

#display movie info
    
disp("Title","title")
disp("Year","year")
disp("Rating","rating")
disp("Time","runtime")
disp("Summary","summary")
disp("Language","language")
disp("Genres","genres")

#display download info
print("\n \n")

down("File",0,"url")
down("Quality",0,"quality")
down("Seeds",0,"seeds")
down("Peers",0,"peers")
down("Size",0,"size")
down("Date Uploaded",0,"date_uploaded")


print("\n \n")

down("File",0,"url")
down("Quality",0,"quality")
down("Seeds",0,"seeds")
down("Peers",0,"peers")
down("Size",0,"size")
down("Date Uploaded",0,"date_uploaded")

#Download Torrent file
user = input ("Do you want to download torrent? (yes / no): ")
if user == "yes":
    select = input("Enter Quality (720p / 1080p): ")
    if select == "720p":
        url=download= json.loads(g_list.content)["data"]["movies"][0]["torrents"][0]["url"]
        select=requests.get(url)
        torrent(select)
    elif select == "1080p":
        url=download= json.loads(g_list.content)["data"]["movies"][0]["torrents"][1]["url"]
        select=requests.get(url)
        torrent(select)
    else:
        print("Invalid Choice")
elif user == "no":
    print("Thank You!")
else:
    print("Invalid Choice")
