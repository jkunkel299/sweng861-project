from flask import Flask, request, render_template
from MusicSearch.music_search import *
from ConfigFile.config import getAuthToken

app = Flask(__name__)

access_token = getAuthToken()

@app.route('/')
def index():
    ''' This code renders the home page, index.html '''
    return render_template('index.html')

@app.route('/artistSearch', methods = ["GET", "POST"])
def artist_page():
    ''' This code receives the text from the HTML interface and 
        returns the artist's most recent albums and top tracks using 
        recent_albums_return() and top_songs python functions.'''
    if request.method == "POST":
        artist = request.form.get('artistToSearch')
        if artist == "":
            return render_template('artist_search.html', recent_albums="", songs="")
        else:
            artist_search = str(artist)
            search_result = find_artist_id(access_token, artist_search)
            top_artist_hit = search_result[1]
            albums_result = recent_albums_return(access_token, search_result[0])
            tracks_result = top_songs(access_token, search_result[0])
            return render_template('artist_search.html', artist_name=top_artist_hit, recent_albums=albums_result, songs=tracks_result)
    return render_template('artist_search.html')


@app.route('/songSearch', methods = ["GET", "POST"])
def song_page():
    ''' This code receives the text from the HTML interface and 
        returns the top 5 most likely tracks, their artists, and their albums, using 
        search_song() python function.'''
    if request.method == "POST":
        term = request.form.get('songToSearch')
        search_term = str(term)
        if search_term == "":
            matches_result = ""
        else:
            matches_result = get_tracks_from_search(access_token, search_term)
        
        return render_template('song_search.html', songs=matches_result)
    return render_template('song_search.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)