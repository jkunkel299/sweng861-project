import requests


def find_artist_id(access_token, artist_search):
    """
    A function that takes in the access_token and artist_search parameters.
    The access_token is used in the header of the GET request to the Spotify
    Web API for authentication and authorization. The artist_search term is
    passed to the Spotify Web API as the query within the URL for the Search
    endpoint.
    The Spotify Web API response is scraped for the artist_id and artist_name.
    The artist_id is required for subsequent artist-related searches.
    The artist_name is the most-likely artist match based on the search term
    entered by the user.
    find_artist_id returns the tuple (artist_id, artist_name).
    """

    if artist_search == "":
        # if statement for error-handling blank entries
        # set artist_id and artist_name to empty strings for future error handling
        artist_id = ""
        artist_name = ""
    else:
        # URL to be used as Search endpoint with Spotify Web API
        # includes filter type=artist to limit search results to artists
        get_id_url = (
            "https://api.spotify.com/v1/search?q=" + artist_search + "&type=artist"
        )
        # Set headers, using access_token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        # GET request to Spotify Web API using established URL and headers
        get_id_res = requests.get(url=get_id_url, headers=headers)
        if get_id_res.status_code == 200:
            # if the response status is 200 (Good)
            # set new dictionary to the 'artists' object within the JSON response from Spotify Web API
            get_id_res_data = get_id_res.json()["artists"]
            if not get_id_res_data["items"]:
                # if the response status was good, but Spotify Web API returned no results
                # set artist_id and artist_name to empty strings for future error handling
                artist_id = ""
                artist_name = ""
            else:
                # extract artist_id and artist_name from 'items' array of artist object
                # using the first artist object (best match to search term)
                artist_id = get_id_res_data["items"][0]["id"]
                artist_name = get_id_res_data["items"][0]["name"]
        elif get_id_res.status_code == 500:
            # if the response status was 500 (Server error)
            # set artist_id and artist_name to blank strings for future error handling
            artist_id = ""
            artist_name = ""
        elif get_id_res.status_code == 400:
            # if the response status was 400 (Client error)
            # set artist_id and artist_name to blank strings for future error handling
            artist_id = ""
            artist_name = ""
    # return tuple containing artist_id and artist_name
    return artist_id, artist_name


def recent_albums_return(access_token, artist_id):
    """
    A function that takes in the access_token and artist_id parameters.
    The access_token is used in the header of the GET request to the Spotify
    Web API for authentication and authorization.
    The artist_id is gained from calling the function find_artist_id
    and is passed to the Spotify Web API as the query within the URL for the
    Get Artist's Albums endpoint.
    The Spotify Web API is scraped for the album cover image, name, and release date
    for up to 5 of the artist's most recent albums.
    recent_albums_return returns an array of recent_albums to be presented on
    the artist_search HTML webpage.
    """
    if artist_id == "":
        # if statement for error-handling results of previously-called find_artist_id function
        # set recent_albums to blank string for future error handling
        recent_albums = ""
    else:
        # URL to be used as Get Artist's Albums endpoint with Spotify Web API
        # includes filter include_groups=album to limit search results to albums
        # includes filter market=US to limit search results to those in the US Market
        # includes filter limit=5 for API to return maximum of 5 albums
        get_recent_albums_url = (
            "https://api.spotify.com/v1/artists/"
            + artist_id
            + "/albums?include_groups=album&market=US&limit=5"
        )
        # Set headers, using access_token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        # GET request to Spotify Web API using established URL and headers
        get_recent_albums_res = requests.get(url=get_recent_albums_url, headers=headers)
        if get_recent_albums_res.status_code == 200:
            # if the response status is 200 (Good)
            # set get_recent_albums_res_data to the 'items' array within the JSON response from Spotify Web API
            get_recent_albums_res_data = get_recent_albums_res.json()["items"]
            # initialize blank list of recent_albums
            recent_albums = []
            for i in range(len(get_recent_albums_res_data)):
                try:
                    # for each album in the 'items' array, extract album cover, album name, and release date
                    album = {
                        "cover": get_recent_albums_res_data[i]["images"][2]["url"],
                        "name": get_recent_albums_res_data[i]["name"],
                        "date": get_recent_albums_res_data[i]["release_date"],
                    }
                    # append the album to the end of the recent_albums list
                    recent_albums.append(album)
                except IndexError:
                    # catch for IndexError
                    recent_albums = ""
        elif get_recent_albums_res.status_code == 500:
            # if the response status was 500 (Server error)
            # set recent_albums to blank string for future error handling
            recent_albums = ""
        elif get_recent_albums_res.status_code == 400:
            # if the response status was 400 (Client error)
            # set recent_albums to blank string for future error handling
            recent_albums = ""
    # return recent_albums list
    return recent_albums


def top_songs(access_token, artist_id):
    """
    A function that takes in the access_token and artist_id parameters.
    The access_token is used in the header of the GET request to the Spotify
    Web API for authentication and authorization.
    The artist_id is gained from calling the function find_artist_id
    and is passed to the Spotify Web API as the query within the URL for the
    Get Artist's Top Tracks endpoint.
    The Spotify Web API is scraped for the song id, album cover image, song name, preview URL,
    album name, and release date for up to 5 of the artist's most popular songs.
    top_songs returns an array of songs to be presented on the artist_search
    HTML webpage.
    """
    if artist_id == "":
        # if statement for error-handling results of previously-called find_artist_id function
        # set songs to blank string for future error handling
        songs = ""
    else:
        # URL to be used as Get Artist's Albums endpoint with Spotify Web API
        # includes filter market=US to limit search results to those in the US Market
        get_top_songs_url = (
            "https://api.spotify.com/v1/artists/" + artist_id + "/top-tracks?market=US"
        )
        # Set headers, using access_token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        # GET request to Spotify Web API using established URL and headers
        get_top_songs_res = requests.get(url=get_top_songs_url, headers=headers)
        if get_top_songs_res.status_code == 200:
            # if the response status is 200 (Good)
            # set get_top_songs_res_data to the 'tracks' array within the JSON response from Spotify Web API
            get_top_songs_res_data = get_top_songs_res.json()["tracks"]
            # initialize blank list of songs
            songs = []
            for i in range(5):
                try:
                    # for the first 5 elements in the 'tracks' array, extract song id, album cover,
                    # song name, song preview URL, album name, and release date
                    song = {
                        "id": get_top_songs_res_data[i]["id"],
                        "cover": get_top_songs_res_data[i]["album"]["images"][2]["url"],
                        "name": get_top_songs_res_data[i]["name"],
                        "preview": get_top_songs_res_data[i]["preview_url"],
                        "album": get_top_songs_res_data[i]["album"]["name"],
                        "date": get_top_songs_res_data[i]["album"]["release_date"],
                    }
                    # append the song to the end of the songs list
                    songs.append(song)
                except IndexError:
                    # catch for IndexError
                    songs = ""
        elif get_top_songs_res.status_code == 500:
            # if the response status was 500 (Server error)
            # set songs to blank string for future error handling
            songs = ""
        elif get_top_songs_res.status_code == 400:
            # if the response status was 400 (Client error)
            # set songs to blank string for future error handling
            songs = ""
    # return songs list
    return songs


def get_tracks_from_search(access_token, search_term):
    """
    A function that takes in the access_token and search_term parameters.
    The access_token is used in the header of the GET request to the Spotify
    Web API for authentication and authorization.
    The search_term is gained from user input and is passed to the Spotify Web API
    as the query within the URL for the Search endpoint.
    The Spotify Web API is scraped for the album cover image, song name, preview URL,
    artist name, album name, and release date for up to 10 of the best song matches
    for the search term.
    get_tracks_from_search returns an array of songs to be presented on the song_search
    HTML webpage.
    """
    if search_term == "":
        songs = ""
    else:
        # URL to be used as Search endpoint with Spotify Web API
        # includes a filter type=track to limit search results to songs
        # includes filter market=US to limit search results to those in the US Market
        # includes filter limit=10 for API to return maximum of 10 songs
        get_songs_url = (
            "https://api.spotify.com/v1/search?q="
            + search_term
            + "&type=track&market=US&limit=10"
        )
        # Set headers, using access_token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        # GET request to Spotify Web API using established URL and headers
        get_songs_res = requests.get(url=get_songs_url, headers=headers)
        if get_songs_res.status_code == 200:
            # if the response status is 200 (Good)
            # set get_songs_res_data to the 'tracks' array within the JSON response from Spotify Web API
            get_songs_res_data = get_songs_res.json()["tracks"]
            if not get_songs_res_data["items"]:
                # if the response status was good, but Spotify Web API returned no results
                # set songs to empty string for future error handling
                songs = ""
            else:
                # initialize blank list of songs
                songs = []
                for i in range(10):
                    try:
                        # for the first 10 elements in the 'tracks' array, extract album cover,
                        # song name, song preview URL, artist name, album name, and release date
                        song = {
                            "cover": get_songs_res_data["items"][i]["album"]["images"][2][
                                "url"
                            ],
                            "name": get_songs_res_data["items"][i]["name"],
                            "preview": get_songs_res_data["items"][i]["preview_url"],
                            "artist": get_songs_res_data["items"][i]["artists"][0]["name"],
                            "album": get_songs_res_data["items"][i]["album"]["name"],
                            "date": get_songs_res_data["items"][i]["album"]["release_date"],
                        }
                        # append the song to the end of the songs list
                        songs.append(song)
                    except IndexError:
                        # catch for IndexError
                        songs = ""
        elif get_songs_res.status_code == 500:
            # if the response status was 500 (Server error)
            # set songs to blank string for future error handling
            songs = ""
        elif get_songs_res.status_code == 400:
            # if the response status was 400 (Client error)
            # set songs to blank string for future error handling
            songs = ""
    # return songs list
    return songs
