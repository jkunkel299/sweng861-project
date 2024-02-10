import json
import requests

def find_artist_id(access_token, artist_search):
    if artist_search == "":
        artist_id = ""
    else: 
        get_id_url = 'https://api.spotify.com/v1/search?q='+artist_search+'&type=artist' 
        headers = {
            'Authorization': f"Bearer {access_token}",
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        get_id_res = requests.get(url=get_id_url, headers=headers)
        if get_id_res.status_code == 200:
            get_id_res_data = get_id_res.json()['artists']
            if not get_id_res_data['items']:
                artist_id = ""
                artist_name = ""
            else: 
                artist_id = get_id_res_data['items'][0]['id']
                artist_name = get_id_res_data['items'][0]['name']
        elif get_id_res.status_code == 500:
            artist_id = ""
            artist_name = ""
        elif get_id_res.status_code == 400:
            artist_id = ""
            artist_name = ""
    
    return artist_id, artist_name

def recent_albums_return(access_token, artist_id):
    if artist_id == "":
        recent_albums = ""
    else:
        get_recent_albums_url = 'https://api.spotify.com/v1/artists/'+artist_id+'/albums?include_groups=album&market=US&limit=5'
        headers = {
            'Authorization': f"Bearer {access_token}",
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        get_recent_albums_res = requests.get(url=get_recent_albums_url, headers=headers)
        if get_recent_albums_res.status_code == 200:
            get_recent_albums_res_data = get_recent_albums_res.json()['items']
            length = len(get_recent_albums_res_data)
            recent_albums = []
            for i in range(length):
                album = {
                    'cover':get_recent_albums_res_data[i]['images'][2]['url'],
                    'name':get_recent_albums_res_data[i]['name'],
                    'date':get_recent_albums_res_data[i]['release_date']
                }
                recent_albums.append(album)
            #print(recent_albums)
        elif get_recent_albums_res.status_code == 500:
            recent_albums = ""
        elif get_recent_albums_res.status_code == 400:
            recent_albums = ""
    
    return recent_albums

def top_songs(access_token, artist_id):
    if artist_id == "":
        songs = ""
    else:
        get_top_songs_url = 'https://api.spotify.com/v1/artists/'+artist_id+'/top-tracks?market=US'
        headers = {
            'Authorization': f"Bearer {access_token}",
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        get_top_songs_res = requests.get(url=get_top_songs_url, headers=headers)
        if get_top_songs_res.status_code == 200:
            get_top_songs_res_data = get_top_songs_res.json()['tracks']
            songs = []
            for i in range(5):
                song = {
                        'id':get_top_songs_res_data[i]['id'],
                        'cover':get_top_songs_res_data[i]['album']['images'][2]['url'],
                        'name':get_top_songs_res_data[i]['name'], 
                        'preview':get_top_songs_res_data[i]['preview_url'],
                        'album':get_top_songs_res_data[i]['album']['name'], 
                        'date':get_top_songs_res_data[i]['album']['release_date']
                    }
                songs.append(song)
        elif get_top_songs_res.status_code == 500:
            songs = ""
        elif get_top_songs_res.status_code == 400:
            songs = ""
    return(songs)

def get_tracks_from_search(access_token, search_term):
    if search_term == "":
        songs = ""
    else: 
        get_songs_url = 'https://api.spotify.com/v1/search?q='+search_term+'&type=track&market=US&limit=10' 
        headers = {
            'Authorization': f"Bearer {access_token}",
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        get_songs_res = requests.get(url=get_songs_url, headers=headers)
        if get_songs_res.status_code == 200:
            get_songs_res_data = get_songs_res.json()['tracks']
            if not get_songs_res_data['items']:
                songs = ""
            else:
                songs = []
                for i in range(10):
                    song = {
                            'cover':get_songs_res_data['items'][i]['album']['images'][2]['url'],
                            'name':get_songs_res_data['items'][i]['name'], 
                            'preview':get_songs_res_data['items'][i]['preview_url'],
                            'artist':get_songs_res_data['items'][i]['artists'][0]['name'],
                            'album':get_songs_res_data['items'][i]['album']['name'], 
                            'date':get_songs_res_data['items'][i]['album']['release_date']
                        }
                    songs.append(song)
        elif get_songs_res.status_code == 500:
            songs = ""
        elif get_songs_res.status_code == 400:
            songs = ""
        return songs