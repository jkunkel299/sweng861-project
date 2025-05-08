# import Flask
from flask import Flask, request, render_template

# import functions from MusicSearch module
from MusicSearch.music_search import (
    find_artist_id,
    recent_albums_return,
    top_songs,
    get_tracks_from_search,
)

# import getAuthToken function from ConfigFile module
from ConfigFile.config import getAuthToken

# Instantiate Flask application
app = Flask(__name__)

# get access_token for use in functions imported from MusicSearch module
access_token = getAuthToken()


@app.route("/")
def index():
    """
    This code renders the home page, index.html
    """
    return render_template("index.html")


@app.route("/artistSearch", methods=["GET", "POST"])
def artist_page():
    """
    This code receives the user input text from the HTML interface and
    returns the artist's most recent albums and top tracks using
    recent_albums_return() and top_songs() python functions.
    """
    # if request.method is POST
    # (i.e., when the user submits the form within the artist_search webpage)
    if request.method == "POST":
        # get user input from form in artist_search.html, input id="artistToSearch"
        artist = request.form.get("artistToSearch")
        if artist == "":
            # if the form is blank, set the page context as empty strings
            top_artist_hit = ""
            albums_result = ""
            tracks_result = ""
        else:
            # convert user input to string
            artist_search = str(artist)
            # call find_artist_id function, where artist_search is the
            # user's input from the artistToSearch form
            search_result = find_artist_id(access_token, artist_search)
            # extract the most-likely value for the artist's name from the search results tuple
            top_artist_hit = search_result[1]
            # call recent_albums_return function, where the artist_id is extracted
            # from the search results tuple
            albums_result = recent_albums_return(access_token, search_result[0])
            # call top_songs function, where the artist_id is extracted from the search results tuple
            tracks_result = top_songs(access_token, search_result[0])
        # render the artist_search template with the context resulting from each function call above, or blank context
        # artist_name is the most-likely name of the artist, top_artist_hit, or empty string if invalid user input
        # recent_albums list is the list returned from recent_albums_return(), albums_result, or empty string if invalid user input
        # songs list is the list returned from top_songs, tracks_result, or empty string if invalid user input
        return render_template(
            "artist_search.html",
            artist_name=top_artist_hit,
            recent_albums=albums_result,
            songs=tracks_result,
        )
    # if request.method is GET, render artist_search HTML page without additional context
    return render_template("artist_search.html")


@app.route("/songSearch", methods=["GET", "POST"])
def song_page():
    """
    This code receives the user input text from the HTML interface and
    returns the top 10 bst-matching tracks, their artists, and their albums, using
    get_tracks_from_search() python function.
    """
    # if request.method is POST
    # (i.e., when the user submits the form within the song_search webpage)
    if request.method == "POST":
        term = request.form.get("songToSearch")
        print(f'term: {term}')
        if term == "":
            # if the form is blank, set the page context to an empty string
            matches_result = ""
            print("in if term = \"\"")
        else:
            # convert user input to string
            search_term = str(term)
            print(f'search_term: {search_term}')
            # call top_songs function, where the search_term is the user's input
            matches_result = get_tracks_from_search(access_token, search_term)
            print(matches_result)
        # render the song_search template with the context resulting from the function call above, or blank context
        # songs list is the list returned from get_tracks_from_search, matches_result, or empty string if invalid user input
        return render_template("song_search.html", songs=matches_result)
    # if request.method is GET, render song_search HTML page without additional context
    return render_template("song_search.html")

@app.errorhandler(500)
def internal_server_error(e):
    """
    This code handles routing for internal server errors, allowing the user
    to return to the homepage.
    """
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500

# run Flask application
if __name__ == "__main__":
    app.run()
