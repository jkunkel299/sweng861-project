# SWENG861 Project
## Music Search Tool
### Jessica Kunkel
---
Software Construction course project in Flask
Link to YouTube presentation: https://youtu.be/iznYkVZqCsg 
---
This Music Search Tool is a web application written in Python using Flask. The application utilizes the Spotify Web API to search for artists, songs, albums, and other data.
The web application supports two use cases: 
1. Search for an artist by name
2. Search for a song by name
#### Search for Artist
Enter the name of an artist and the web application will return the best-match artist for the user's input, up to five of the artist's most recent albums, and up to five of the artist's most popular songs. Information displayed about the albums includes the cover art, the name of the album, and its release date. Information displayed about the songs includes the cover art, the name of the song, the album it appears on, and the release date of the album. Where streaming rights will allow, the user can also choose to play/pause a 30-second preview of each song.
#### Search for Song
Enter the name of a song and the web application will return 10 songs whose titles best match the search term, ranked by popularity. Information displayed about the songs includes the cover art, the name of the song, the song's artist, the album the song appears on, and the release date of the album. Where streaming rights will allow, the user can also choose to play/pause a 30-second preview of each song.
