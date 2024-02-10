import unittest

from MusicSearch.music_search import *
from ConfigFile.config import getAuthToken

access_token = getAuthToken()

class TestMusicSearch(unittest.TestCase):
    def test_find_artist_id(self):
        ARTIST_1 = "Taylor Swift"
        ARTIST_2 = "Noah Kahan"
        ARTIST_3 = "Lizzy McAlpine"
        ARTIST_4 = "Hozier"
        ARTIST_5 = ""

        RESULT_1 = find_artist_id(access_token, ARTIST_1)
        RESULT_2 = find_artist_id(access_token, ARTIST_2)
        RESULT_3 = find_artist_id(access_token, ARTIST_3)
        RESULT_4 = find_artist_id(access_token, ARTIST_4)
        RESULT_5 = find_artist_id(access_token, ARTIST_5)

        ID_1 = RESULT_1[0]
        ID_2 = RESULT_2[0]
        ID_3 = RESULT_3[0]
        ID_4 = RESULT_4[0]
        ID_5 = RESULT_5[0]

        self.assertEqual(ID_1, "06HL4z0CvFAxyc27GXpf02")
        self.assertEqual(ID_2, "2RQXRUsr4IW1f3mKyKsy4B")
        self.assertEqual(ID_3, "1GmsPCcpKgF9OhlNXjOsbS")
        self.assertEqual(ID_4, "2FXC3k01G6Gw61bmprjgqS")
        self.assertEqual(ID_5, "")

    def test_recent_albums_return(self):
        ARTIST_1 = "Taylor Swift"
        ARTIST_2 = "Noah Kahan"
        ARTIST_3 = "Lizzy McAlpine"
        ARTIST_4 = "Hozier"
        ARTIST_5 = ""

        RESULT_1 = recent_albums_return(access_token, ARTIST_1)
        RESULT_2 = recent_albums_return(access_token, ARTIST_2)
        RESULT_3 = recent_albums_return(access_token, ARTIST_3)
        RESULT_4 = recent_albums_return(access_token, ARTIST_4)
        RESULT_5 = recent_albums_return(access_token, ARTIST_5)

        EXPECTED_1 = [{'cover':'', 'name': "1989 (Taylor's Version) [Deluxe]", 'date': '2023-10-27'}, 
                      {'cover':'', 'name': "1989 (Taylor's Version)", 'date': '2023-10-26'}, 
                      {'cover':'', 'name': "Speak Now (Taylor's Version)", 'date': '2023-07-07'}, 
                      {'cover':'', 'name': 'Midnights (The Til Dawn Edition)', 'date': '2023-05-26'}, 
                      {'cover':'', 'name': 'Midnights (3am Edition)', 'date': '2022-10-22'}]
        EXPECTED_2 = [{'cover':'', 'name': "Stick Season (We'll All Be Here Forever)", 'date': '2023-06-09'}, 
                      {'cover':'', 'name': "Stick Season", 'date': '2022-10-14'}, 
                      {'cover':'', 'name': "I Was / I Am", 'date': '2021-09-17'}, 
                      {'cover':'', 'name': "Busyhead", 'date': '2019-06-14'}]
        EXPECTED_3 = [{'cover':'', 'name': "five seconds flat", 'date': '2022-04-08'}, 
                      {'cover':'', 'name': "Give Me A Minute", 'date': '2020-08-13'}]
        EXPECTED_4 = [{'cover':'', 'name': "Unreal Unearth", 'date': '2023-08-18'}, 
                      {'cover':'', 'name': "Wasteland, Baby!", 'date': '2019-03-01'}, 
                      {'cover':'', 'name': "Hozier", 'date': '2014-10-07'}, 
                      {'cover':'', 'name': "Hozier (Expanded Edition)", 'date': '2014-09-19'}]
        EXPECTED_5 = ""
        
        self.assertEqual(RESULT_1, EXPECTED_1)
        self.assertEqual(RESULT_2, EXPECTED_2)
        self.assertEqual(RESULT_3, EXPECTED_3)
        self.assertEqual(RESULT_4, EXPECTED_4)
        self.assertEqual(RESULT_5, EXPECTED_5)
        
    def test_top_songs(self):
        ARTIST_1 = "Taylor Swift"
        ARTIST_2 = "Noah Kahan"
        ARTIST_3 = "Lizzy McAlpine"
        ARTIST_4 = "Hozier"
        ARTIST_5 = ""

        RESULT_1 = top_songs(access_token, ARTIST_1)
        RESULT_2 = top_songs(access_token, ARTIST_2)
        RESULT_3 = top_songs(access_token, ARTIST_3)
        RESULT_4 = top_songs(access_token, ARTIST_4)
        RESULT_5 = top_songs(access_token, ARTIST_5)

        EXPECTED_1 = [{'cover':'', 'name':"Cruel Summer", 'preview':'', 'album':"Lover", 'date':'2019-08-23'},
                      {'cover':'', 'name':"Is It Over Now? (Taylor's Version) (From The Vault)", 'preview':'', 'album':"1989 (Taylor's Version)", 'date':'2023-10-26'},
                      {'cover':'', 'name':"Lover", 'preview':'', 'album':"Lover", 'date':'2019-08-23'},
                      {'cover':'', 'name':"Anti-Hero", 'preview':'', 'album':"Midnights", 'date':'2022-10-21'},
                      {'cover':'', 'name':"cardigan", 'preview':'', 'album':"folklore", 'date':'2020-07-24'}]
        EXPECTED_2 = [{'cover':'', 'name':"Stick Season", 'preview':'', 'album':"Stick Season", 'date':'2022-10-14'},
                      {'cover':'', 'name':"Dial Drunk (with Post Malone)", 'preview':'', 'album':"Dial Drunk (with Post Malone)", 'date':'2023-07-18'},
                      {'cover':'', 'name':"Northern Attitude (with Hozier)", 'preview':'', 'album':"Northern Attitude (with Hozier)", 'date':'2023-11-10'},
                      {'cover':'', 'name':"You’re Gonna Go Far", 'preview':'', 'album':"Stick Season (We'll All Be Here Forever)", 'date':'2023-06-09'},
                      {'cover':'', 'name':"All My Love", 'preview':'', 'album':"Stick Season", 'date':'2022-10-14'}]
        EXPECTED_3 = [{'cover':'', 'name':"ceilings", 'preview':'', 'album':"five seconds flat", 'date':'2022-04-08'},
                      {'cover':'', 'name':"Call Your Mom (with Lizzy McAlpine)", 'preview':'', 'album':"Call Your Mom (with Lizzy McAlpine)", 'date':'2023-09-15'},
                      {'cover':'', 'name':"doomsday", 'preview':'', 'album':"five seconds flat", 'date':'2022-04-08'},
                      {'cover':'', 'name':"hate to be lame", 'preview':'', 'album':"five seconds flat", 'date':'2022-04-08'},
                      {'cover':'', 'name':"You Could Start A Cult (with Lizzy McAlpine)", 'preview':'', 'album':"The Show: The Encore", 'date':'2023-11-03'}]
        EXPECTED_4 = [{'cover':'', 'name':"Take Me to Church", 'preview':'', 'album':"Hozier (Expanded Edition)", 'date':'2014-09-19'},
                      {'cover':'', 'name':"Work Song", 'preview':'', 'album':"Hozier (Expanded Edition)", 'date':'2014-09-19'},
                      {'cover':'', 'name':"Northern Attitude (with Hozier)", 'preview':'', 'album':"Northern Attitude (with Hozier)", 'date':'2023-11-10'},
                      {'cover':'', 'name':"Would That I", 'preview':'', 'album':"Wasteland, Baby!", 'date':'2019-03-01'},
                      {'cover':'', 'name':"Someone New", 'preview':'', 'album':"Hozier (Expanded Edition)", 'date':'2014-09-19'}]
        EXPECTED_5 = ""
        
        self.assertEqual(RESULT_1, EXPECTED_1)
        self.assertEqual(RESULT_2, EXPECTED_2)
        self.assertEqual(RESULT_3, EXPECTED_3)
        self.assertEqual(RESULT_4, EXPECTED_4)
        self.assertEqual(RESULT_5, EXPECTED_5)

    def get_tracks_from_search(self):
        TERM_1 = "lover"
        TERM_2 = "jaded"
        TERM_3 = ""

        RESULT_1 = get_tracks_from_search(access_token, TERM_1)
        RESULT_2 = get_tracks_from_search(access_token, TERM_2)
        RESULT_3 = get_tracks_from_search(access_token, TERM_3)

        EXPECTED_1 = [{'cover':'', 'name':"Lover", 'preview':'', 'artist':"Taylor Swift", 'album':"Lover",'date':'2019-08-23'},
                      {'cover':'', 'name':"Lover, You Should've Come Over", 'preview':'', 'artist':"Jeff Buckley", 'album':"Grace",'date':'1994'},
                      {'cover':'', 'name':"Miss Americana & The Heartbreak Prince", 'preview':'', 'artist':"Taylor Swift", 'album':"Lover",'date':'2019-08-23'},
                      {'cover':'', 'name':"False God", 'preview':'', 'artist':"Taylor Swift", 'album':"Lover",'date':'2019-08-23'},
                      {'cover':'', 'name':"Lovers Rock", 'preview':'', 'artist':"TV Girl", 'album':"French Exit",'date':'2014-06-05'},
                      {'cover':'', 'name':"Stick Season", 'preview':'', 'artist':"Noah Kahan", 'album':"Stick Season",'date':'2022-10-14'},
                      {'cover':'', 'name':"Daylight", 'preview':'', 'artist':"Taylor Swift", 'album':"Lover",'date':'2019-08-23'},
                      {'cover':'', 'name':"Lover Is a Day", 'preview':'', 'artist':"Cuco", 'album':"wannabewithu",'date':'2016-07-09'},
                      {'cover':'', 'name':"Lovers And Friends", 'preview':'', 'artist':"Lil Jon & The East Side Boyz", 'album':"Crunk Juice",'date':'2004-11-16'},
                      {'cover':'', 'name':"Lovers on the Sun", 'preview':'', 'artist':"Various Artists", 'album':"Surtido Rico Vol. 1",'date':'2024-02-03'}]
        EXPECTED_2 = [{'cover':'', 'name':"Jaded", 'preview':'', 'artist':"Miley Cyrus", 'album':"Endless Summer Vacation",'date':'2023-08-18'},
                      {'cover':'', 'name':"Jaded", 'preview':'', 'artist':"Various Artists", 'album':"NOW That's What I Call Music! Vol. 88",'date':'2023-10-27'},
                      {'cover':'', 'name':"Used To Be Young", 'preview':'', 'artist':"Miley Cyrus", 'album':"Endless Summer Vacation",'date':'2023-08-18'},
                      {'cover':'', 'name':"Jaded", 'preview':'', 'artist':"Spiritbox", 'album':"Jaded",'date':'2023-08-25'},
                      {'cover':'', 'name':"Cruel Summer", 'preview':'', 'artist':"Taylor Swift", 'album':"Lover",'date':'2019-08-23'},
                      {'cover':'', 'name':"Rose Colored Lenses", 'preview':'', 'artist':"Miley Cyrus", 'album':"Endless Summer Vacation",'date':'2023-08-18'},
                      {'cover':'', 'name':"Jaded", 'preview':'', 'artist':"Aerosmith", 'album':"Just Push Play",'date':'2001-03-05'},
                      {'cover':'', 'name':"Stick Season", 'preview':'', 'artist':"Noah Kahan", 'album':"Stick Season",'date':'2022-10-14'},
                      {'cover':'', 'name':"Jaded", 'preview':'', 'artist':"Drake", 'album':"Scorpion",'date':'2018-06-29'},
                      {'cover':'', 'name':"jaded", 'preview':'', 'artist':"sadeyes", 'album':"jaded",'date':'2018-12-03'}]
        EXPECTED_3 = ""

        self.assertEqual(RESULT_1, EXPECTED_1)
        self.assertEqual(RESULT_2, EXPECTED_2)
        self.assertEqual(RESULT_3, EXPECTED_3)

    

if (__name__ == "__main__"):
    unittest.main()