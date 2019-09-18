import requests
import json



print("This is a YTS Movie Download Script.")
print("1. Browse Movies")
print ("2. Search")
print ("3. exit")
menu=input("Select: ")

#function to fetch movie details
def disp(key,string):
            print(key," : ", detail1[string])

def disp1(key,string):
            print(key," : ", detail2[string])

#function to fetch download details

def down(key,Q,string):
    print(key," : ", download[Q][string])

#function to download torrent file

def torrent(Q):
    filename=detail2["title"]
    with open(filename+".torrent", "wb") as f:
        f.write(Q.content)

if menu == "1":

    #Listing Movies:

    Gen = input("Enter Genre : ")
    Qual = input("Enter Quality (720p, 1080p, 3D, All): ")
    rating = input("Enter Minimum Rating ( 0 to 9) : ")
    sort = input("Sort by (title, year, rating, peers, seeds, download_count, like_count, date_added): ")

    payload1 = {"genre":Gen,"quality":Qual,"minimum_rating":rating,"sort_by":sort,"limit":"20"}


    #yts api endpoint

    list_movies="https://yts.lt/api/v2/list_movies.json"

    g_list=requests.get(list_movies, params=payload1)



    #details_dictionary_call
    for i in range(20):
        try:
            detail1 = json.loads(g_list.content)["data"]["movies"][i]

            #display movie info
            print("\n")
            disp("ID", "id")
            disp("Title","title")
            disp("Year","year")
            disp("Rating","rating")
            disp("Time","runtime")
            disp("Language","language")
            disp("Genres","genres")
        except KeyError:
            continue
            
    print("\n \n")
    choose = input("Input ID of movie to view deails: ")

    payload2 = {"movie_id":choose}
    movie_det_ep="https://yts.lt/api/v2/movie_details.json"
    movie_det=requests.get(movie_det_ep, params=payload2)

    detail2 = json.loads(movie_det.content)["data"]["movie"]

    print("\n")
    disp1("ID", "id")
    disp1("Title","title")
    disp1("Year","year")
    disp1("Rating","rating")
    disp1("Time","runtime")
    disp1("Language","language")
    disp1("Genres","genres")
    disp1("Summary","description_full")

    user = input ("\n Do you want to download torrent? (yes / no): ")
    if user == "yes":
        select = input("Enter Quality (720p / 1080p): ")
        if select == "720p":
            url=download= json.loads(movie_det.content)["data"]["movie"]["torrents"][0]["url"]
            select=requests.get(url)
            torrent(select)
        elif select == "1080p":
            url=download= json.loads(movie_det.content)["data"]["movie"][0]["torrents"][1]["url"]
            select=requests.get(url)
            torrent(select)
        else:
            print("Invalid Choice")
    elif user == "no":
        print("Thank You!")
    else:
        print("Invalid Choice")
elif menu == "2":
    query = input("Enter Keyword You Want to Search: ")

    try:
        payload= {"query_term": query}
        api_end="https://yts.lt/api/v2/list_movies.json"
        url = requests.get(api_end, params=payload,timeout=10)

        detail1 = json.loads(url.content)["data"]["movies"][0]
        print("\n")
        disp("ID", "id")
        disp("Title","title")
        disp("Year","year")
        disp("Rating","rating")
        disp("Time","runtime")
        disp("Language","language")
        disp("Genres","genres")
        disp("Summary","description_full")


        print("\n \n")
        choose = input("Input ID of movie to view deails: ")

        payload2 = {"movie_id":choose}
        movie_det_ep="https://yts.lt/api/v2/movie_details.json"
        movie_det=requests.get(movie_det_ep, params=payload2)

        detail2 = json.loads(movie_det.content)["data"]["movie"]

        print("\n")
        disp1("ID", "id")
        disp1("Title","title")
        disp1("Year","year")
        disp1("Rating","rating")
        disp1("Time","runtime")
        disp1("Language","language")
        disp1("Genres","genres")
        disp1("Summary","description_full")

        user = input ("\n Do you want to download torrent? (yes / no): ")
        if user == "yes":
            select = input("Enter Quality (720p / 1080p): ")
            if select == "720p":
                url=download= json.loads(movie_det.content)["data"]["movie"]["torrents"][0]["url"]
                select=requests.get(url)
                torrent(select)
            elif select == "1080p":
                url=download= json.loads(movie_det.content)["data"]["movie"][0]["torrents"][1]["url"]
                select=requests.get(url)
                torrent(select)
            else:
                print("Invalid Choice")
        elif user == "no":
            print("Thank You!")
        else:
            print("Invalid Choice")
                
    except (http.client.RemoteDisconnected,urllib3.exceptions.ProtocolError,requests.exceptions.ConnectionError):
        print("Error Establishing Connection: Please Check Your Internet Connection.")

elif menu == "3":
    print("Thank You")
