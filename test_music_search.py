import unittest

from MusicSearch.music_search import (
    find_artist_id,
    recent_albums_return,
    top_songs,
    get_tracks_from_search,
)
from ConfigFile.config import getAuthToken

# get access_token for use in functions imported from MusicSearch module
access_token = getAuthToken()


class TestMusicSearch(unittest.TestCase):
    def test_find_artist_id(self):
        """
        Testing functionality of find_artist_id python function by comparing
        resultant artist_id and artist_name to the expected output from the
        Spotify Web API
        """
        # Set artist inputs, including blank and invalid entries
        # Testing ability to extract best-match information based on partial artist entry
        ARTIST_1 = "Taylor"
        ARTIST_2 = "Lizzy McAlpine"
        ARTIST_3 = "Hozier"
        # blank entry
        ARTIST_4 = ""
        # invalid entry Returns Status 200 with blank items array
        ARTIST_5 = "6570-90=\\"
        # Invalid entry Returns Status 400 error from Spotify Web API
        ARTIST_6 = "                       "

        # Set expected values for artist_id
        EXP_ID_1 = "06HL4z0CvFAxyc27GXpf02"
        EXP_ID_2 = "1GmsPCcpKgF9OhlNXjOsbS"
        EXP_ID_3 = "2FXC3k01G6Gw61bmprjgqS"
        EXP_ID_4 = ""
        EXP_ID_5 = ""
        EXP_ID_6 = ""

        # Set expected values for artist_name
        EXP_ARTIST_NAME_1 = "Taylor Swift"
        EXP_ARTIST_NAME_2 = "Lizzy McAlpine"
        EXP_ARTIST_NAME_3 = "Hozier"
        EXP_ARTIST_NAME_4 = ""
        EXP_ARTIST_NAME_5 = ""
        EXP_ARTIST_NAME_6 = ""

        # Result array - call the function find_artist_id for each artist name input
        RESULT_1 = find_artist_id(access_token, ARTIST_1)
        RESULT_2 = find_artist_id(access_token, ARTIST_2)
        RESULT_3 = find_artist_id(access_token, ARTIST_3)
        RESULT_4 = find_artist_id(access_token, ARTIST_4)
        RESULT_5 = find_artist_id(access_token, ARTIST_5)
        RESULT_6 = find_artist_id(access_token, ARTIST_6)

        # extract values for artist_id from result arrays
        RES_ID_1 = RESULT_1[0]
        RES_ID_2 = RESULT_2[0]
        RES_ID_3 = RESULT_3[0]
        RES_ID_4 = RESULT_4[0]
        RES_ID_5 = RESULT_5[0]
        RES_ID_6 = RESULT_6[0]

        # extract values for artist_name from result arrays
        RES_ARTIST_NAME_1 = RESULT_1[1]
        RES_ARTIST_NAME_2 = RESULT_2[1]
        RES_ARTIST_NAME_3 = RESULT_3[1]
        RES_ARTIST_NAME_4 = RESULT_4[1]
        RES_ARTIST_NAME_5 = RESULT_5[1]
        RES_ARTIST_NAME_6 = RESULT_6[1]

        # compare artist_id extracted from result of find_artist_id to the expected result given by the Spotify Web API
        self.assertEqual(RES_ID_1, EXP_ID_1)
        self.assertEqual(RES_ID_2, EXP_ID_2)
        self.assertEqual(RES_ID_3, EXP_ID_3)
        self.assertEqual(RES_ID_4, EXP_ID_4)
        self.assertEqual(RES_ID_5, EXP_ID_5)
        self.assertEqual(RES_ID_6, EXP_ID_6)

        # compare artist_name extracted from result of find_artist_id to the expected result given by the Spotify Web API
        self.assertEqual(RES_ARTIST_NAME_1, EXP_ARTIST_NAME_1)
        self.assertEqual(RES_ARTIST_NAME_2, EXP_ARTIST_NAME_2)
        self.assertEqual(RES_ARTIST_NAME_3, EXP_ARTIST_NAME_3)
        self.assertEqual(RES_ARTIST_NAME_4, EXP_ARTIST_NAME_4)
        self.assertEqual(RES_ARTIST_NAME_5, EXP_ARTIST_NAME_5)
        self.assertEqual(RES_ARTIST_NAME_6, EXP_ARTIST_NAME_6)

    def test_recent_albums_return(self):
        """
        Testing functionality of recent_albums_return python function by comparing
        resultant array of recent_albums to the expected output from the
        Spotify Web API
        """
        # Set artist IDs
        # Artist: Taylor Swift
        ARTIST_1 = "06HL4z0CvFAxyc27GXpf02"
        # Artist: Lizzy McAlpine
        # Testing ability to handle artist with <5 albums
        ARTIST_2 = "1GmsPCcpKgF9OhlNXjOsbS"
        # Artist: Hozier
        # Testing ability to handle artist with <5 albums
        ARTIST_3 = "2FXC3k01G6Gw61bmprjgqS"
        # Result of any invalid user input:
        # Blank, invalid term with Status 200, invalid term with Status 400
        ARTIST_4 = ""

        # Result array - call the function recent_albums_return for each artist_id input
        RESULT_1 = recent_albums_return(access_token, ARTIST_1)
        RESULT_2 = recent_albums_return(access_token, ARTIST_2)
        RESULT_3 = recent_albums_return(access_token, ARTIST_3)
        RESULT_4 = recent_albums_return(access_token, ARTIST_4)

        # Set expected values for results arrays
        EXPECTED_1 = [
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851dc2bacae1dca83d26e2b1949",
                "name": "1989 (Taylor's Version) [Deluxe]",
                "date": "2023-10-27",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851904445d70d04eb24d6bb79ac",
                "name": "1989 (Taylor's Version)",
                "date": "2023-10-26",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d000048510b04da4f224b51ff86e0a481",
                "name": "Speak Now (Taylor's Version)",
                "date": "2023-07-07",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851fa747621a53c8e2cc436dee0",
                "name": "Midnights (The Til Dawn Edition)",
                "date": "2023-05-26",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851e0b60c608586d88252b8fbc0",
                "name": "Midnights (3am Edition)",
                "date": "2022-10-22",
            },
        ]
        EXPECTED_2 = [
            {
                "cover": "https://i.scdn.co/image/ab67616d000048511e7c02b74d1beefca663be04",
                "name": "five seconds flat",
                "date": "2022-04-08",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d000048516c1ff9424f275a8af7c72551",
                "name": "Give Me A Minute",
                "date": "2020-08-13",
            },
        ]
        EXPECTED_3 = [
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851a63bdfd4a6e9b3c9f4f2e91d",
                "name": "Unreal Unearth",
                "date": "2023-08-18",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d000048515795e01c151ba5a8ce4bd295",
                "name": "Wasteland, Baby!",
                "date": "2019-03-01",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d000048510359731f8f8240580be3a9ee",
                "name": "Hozier",
                "date": "2014-10-07",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d000048514ca68d59a4a29c856a4a39c2",
                "name": "Hozier (Expanded Edition)",
                "date": "2014-09-19",
            },
        ]
        EXPECTED_4 = ""

        # compare result array extracted from result of recent_albums_return to the expected result given by the Spotify Web API
        self.assertEqual(RESULT_1, EXPECTED_1)
        self.assertEqual(RESULT_2, EXPECTED_2)
        self.assertEqual(RESULT_3, EXPECTED_3)
        self.assertEqual(RESULT_4, EXPECTED_4)

    def test_top_songs(self):
        """
        Testing functionality of top_songs python function by comparing
        the resultant array of songs to the expected output from the
        Spotify Web API
        """
        # Set artist IDs
        # Artist: Taylor Swift
        ARTIST_1 = "06HL4z0CvFAxyc27GXpf02"
        # Artist: Lizzy McAlpine
        ARTIST_2 = "1GmsPCcpKgF9OhlNXjOsbS"
        # Artist: Hozier
        ARTIST_3 = "2FXC3k01G6Gw61bmprjgqS"
        # Result of any invalid user input:
        # Blank, invalid term with Status 200, invalid term with Status 400
        ARTIST_4 = ""

        # Result array - call the function top_songs for each artist_id input
        RESULT_1 = top_songs(access_token, ARTIST_1)
        RESULT_2 = top_songs(access_token, ARTIST_2)
        RESULT_3 = top_songs(access_token, ARTIST_3)
        RESULT_4 = top_songs(access_token, ARTIST_4)

        # Set expected values for results arrays
        EXPECTED_1 = [
            {
                "id": "1BxfuPKGuaTgP7aM0Bbdwr",
                "cover": "https://i.scdn.co/image/ab67616d00004851e787cffec20aa2a396a61647",
                "name": "Cruel Summer",
                "preview": None,
                "album": "Lover",
                "date": "2019-08-23",
            },
            {
                "id": "1Iq8oo9XkmmvCQiGOfORiz",
                "cover": "https://i.scdn.co/image/ab67616d00004851904445d70d04eb24d6bb79ac",
                "name": "Is It Over Now? (Taylor's Version) (From The Vault)",
                "preview": None,
                "album": "1989 (Taylor's Version)",
                "date": "2023-10-26",
            },
            {
                "id": "0V3wPSX9ygBnCm8psDIegu",
                "cover": "https://i.scdn.co/image/ab67616d00004851bb54dde68cd23e2a268ae0f5",
                "name": "Anti-Hero",
                "preview": None,
                "album": "Midnights",
                "date": "2022-10-21",
            },
            {
                "id": "1dGr1c8CrMLDpV6mPbImSI",
                "cover": "https://i.scdn.co/image/ab67616d00004851e787cffec20aa2a396a61647",
                "name": "Lover",
                "preview": None,
                "album": "Lover",
                "date": "2019-08-23",
            },
            {
                "id": "4R2kfaDFhslZEMJqAFNpdd",
                "cover": "https://i.scdn.co/image/ab67616d0000485195f754318336a07e85ec59bc",
                "name": "cardigan",
                "preview": None,
                "album": "folklore",
                "date": "2020-07-24",
            },
        ]
        EXPECTED_2 = [
            {
                "id": "2L9N0zZnd37dwF0clgxMGI",
                "cover": "https://i.scdn.co/image/ab67616d00004851d370fdc4dbc47778b9b667c3",
                "name": "ceilings",
                "preview": "https://p.scdn.co/mp3-preview/580782ffb17d468fe5d000bdf86cc07926ff9a5a?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "album": "five seconds flat",
                "date": "2022-04-08",
            },
            {
                "id": "3fKpSA5w8iqLe9sNdIDESW",
                "cover": "https://i.scdn.co/image/ab67616d00004851f0b007441dc1a09cbbfd77f6",
                "name": "Call Your Mom (with Lizzy McAlpine)",
                "preview": None,
                "album": "Call Your Mom (with Lizzy McAlpine)",
                "date": "2023-09-15",
            },
            {
                "id": "4WjxtORnwPavm5PDsAWJEc",
                "cover": "https://i.scdn.co/image/ab67616d00004851d370fdc4dbc47778b9b667c3",
                "name": "doomsday",
                "preview": "https://p.scdn.co/mp3-preview/03ca8dbd3728d022dca17f7873478503dbc7a8b7?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "album": "five seconds flat",
                "date": "2022-04-08",
            },
            {
                "id": "26MJjeJ0NSOQDKeZzrEFMl",
                "cover": "https://i.scdn.co/image/ab67616d00004851d370fdc4dbc47778b9b667c3",
                "name": "hate to be lame",
                "preview": "https://p.scdn.co/mp3-preview/1dbb4d772cbf42643f43513d17be5cdca64d9857?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "album": "five seconds flat",
                "date": "2022-04-08",
            },
            {
                "id": "1VsciQwDYOAyDw2FX6D062",
                "cover": "https://i.scdn.co/image/ab67616d000048514256f53c0c1dd46da47802d5",
                "name": "You Could Start A Cult (with Lizzy McAlpine)",
                "preview": None,
                "album": "The Show: The Encore",
                "date": "2023-11-03",
            },
        ]
        EXPECTED_3 = [
            {
                "id": "1CS7Sd1u5tWkstBhpssyjP",
                "cover": "https://i.scdn.co/image/ab67616d000048514ca68d59a4a29c856a4a39c2",
                "name": "Take Me to Church",
                "preview": "https://p.scdn.co/mp3-preview/d6170162e349338277c97d2fab42c386701a4089?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "album": "Hozier (Expanded Edition)",
                "date": "2014-09-19",
            },
            {
                "id": "5TgEJ62DOzBpGxZ7WRsrqb",
                "cover": "https://i.scdn.co/image/ab67616d000048514ca68d59a4a29c856a4a39c2",
                "name": "Work Song",
                "preview": "https://p.scdn.co/mp3-preview/4645ce3b1f238810c2e61a57a4b4ed4c2e78bd62?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "album": "Hozier (Expanded Edition)",
                "date": "2014-09-19",
            },
            {
                "id": "4oEf84vBYVftf6KmZexhVo",
                "cover": "https://i.scdn.co/image/ab67616d00004851030dc4208e26478832531bd4",
                "name": "Northern Attitude (with Hozier)",
                "preview": None,
                "album": "Northern Attitude (with Hozier)",
                "date": "2023-11-10",
            },
            {
                "id": "37zuIvk4KBkAxxLJsxJaHq",
                "cover": "https://i.scdn.co/image/ab67616d000048515795e01c151ba5a8ce4bd295",
                "name": "Would That I",
                "preview": "https://p.scdn.co/mp3-preview/268399c1c6c5c367f58b14e09164ea9c8924ea1e?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "album": "Wasteland, Baby!",
                "date": "2019-03-01",
            },
            {
                "id": "2DNXgvkyv35vTWvdgjs7qn",
                "cover": "https://i.scdn.co/image/ab67616d000048514ca68d59a4a29c856a4a39c2",
                "name": "Someone New",
                "preview": "https://p.scdn.co/mp3-preview/02e87019d26c818328a91c33c10509224b880916?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "album": "Hozier (Expanded Edition)",
                "date": "2014-09-19",
            },
        ]
        EXPECTED_4 = ""

        # compare result array extracted from result of top_songs to the expected result given by the Spotify Web API
        self.assertEqual(RESULT_1, EXPECTED_1)
        self.assertEqual(RESULT_2, EXPECTED_2)
        self.assertEqual(RESULT_3, EXPECTED_3)
        self.assertEqual(RESULT_4, EXPECTED_4)

    def test_get_tracks_from_search(self):
        """
        Testing functionality of get_tracks_from_search python function by
        comparing the resultant array of songs to the expected output from the
        Spotify Web API
        """
        # Set search terms
        TERM_1 = "lover"
        TERM_2 = "jaded"
        # blank search bar
        TERM_3 = ""
        # Invalid search term Returns Status code 200 with Blank items array
        TERM_4 = "6570-90=\\"
        # Invalid search term Returns Status code 400 error message from Spotify Web API
        TERM_5 = "                       "

        # Result array - call the function get_tracks_from_search for each search_term input
        RESULT_1 = get_tracks_from_search(access_token, TERM_1)
        RESULT_2 = get_tracks_from_search(access_token, TERM_2)
        RESULT_3 = get_tracks_from_search(access_token, TERM_3)
        RESULT_4 = get_tracks_from_search(access_token, TERM_4)
        RESULT_5 = get_tracks_from_search(access_token, TERM_5)

        # Set expected values for results arrays
        EXPECTED_1 = [
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851e787cffec20aa2a396a61647",
                "name": "Lover",
                "preview": None,
                "artist": "Taylor Swift",
                "album": "Lover",
                "date": "2019-08-23",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851e1bc1af856b42dd7fdba9f84",
                "name": "Lovers Rock",
                "preview": "https://p.scdn.co/mp3-preview/922a42db5aa8f8d335725697b7d7a12af6808f3a?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "TV Girl",
                "album": "French Exit",
                "date": "2014-06-05",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d000048516a760642a56847027428cb61",
                "name": "Lover, You Should've Come Over",
                "preview": "https://p.scdn.co/mp3-preview/a846c60d4880f6b3901df7c7b3f6d156f4807f8c?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "Jeff Buckley",
                "album": "Grace",
                "date": "1994",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d000048514ab521cf16202a5bc5f72cfe",
                "name": "Lovers And Friends",
                "preview": "https://p.scdn.co/mp3-preview/02770b9d1930f1f8bd22b20b2fd65857a8b04dd3?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "Lil Jon & The East Side Boyz",
                "album": "Crunk Juice",
                "date": "2004-11-16",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851b1c091e32aad5310ebbdd558",
                "name": "Lover Is a Day",
                "preview": "https://p.scdn.co/mp3-preview/fbef3cdacb1636624f4a3bbc2050b008414dd1d7?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "Cuco",
                "album": "wannabewithu",
                "date": "2016-07-09",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d0000485159457bdb1edb5c6417f3baa2",
                "name": "Lover (Remix) [feat. Shawn Mendes]",
                "preview": None,
                "artist": "Taylor Swift",
                "album": "Lover (Remix) [feat. Shawn Mendes]",
                "date": "2019-11-13",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851642f3d8e8208bd784d377b0d",
                "name": "Loverboy",
                "preview": "https://p.scdn.co/mp3-preview/31722612c1d7563f1d24f4b242982553f49582e8?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "A-Wall",
                "album": "Helios",
                "date": "2019-08-04",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851ee52821d214e70851ac26702",
                "name": "Lovers",
                "preview": "https://p.scdn.co/mp3-preview/b78142d33132b001ccda9a6db8087c35f20bc491?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "Anna of the North",
                "album": "Lovers",
                "date": "2017-09-08",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851d9296492f954b9e422cd79f5",
                "name": "Loverboy",
                "preview": "https://p.scdn.co/mp3-preview/31722612c1d7563f1d24f4b242982553f49582e8?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "A-Wall",
                "album": "Loverboy",
                "date": "2019-06-28",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d0000485100540a663c95a4c2ec8a8c0c",
                "name": "Lover/Friend",
                "preview": "https://p.scdn.co/mp3-preview/11c0c5531312a990260ce56a60b6248370e087d9?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "KAYTRANADA",
                "album": "Lover/Friend",
                "date": "2023-11-30",
            },
        ]
        EXPECTED_2 = [
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851cd222052a2594be29a6616b5",
                "name": "Jaded",
                "preview": "https://p.scdn.co/mp3-preview/b70d6946222644d6d88d5b88fe0c8446c6240bd0?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "Miley Cyrus",
                "album": "Endless Summer Vacation",
                "date": "2023-08-18",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851f907de96b9a4fbc04accc0d5",
                "name": "Jaded",
                "preview": None,
                "artist": "Drake",
                "album": "Scorpion",
                "date": "2018-06-29",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d000048518515be38589bf130a2f535e1",
                "name": "Jaded",
                "preview": "https://p.scdn.co/mp3-preview/eeb5e4b1c1cc24c6c0c2609095ff717aa0c27150?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "Spiritbox",
                "album": "Jaded",
                "date": "2023-08-25",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d0000485136051875634a4833119cb4b8",
                "name": "Jaded",
                "preview": None,
                "artist": "Aerosmith",
                "album": "Just Push Play",
                "date": "2001-03-05",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851ac9a652335cf34de9a65292a",
                "name": "Jaded",
                "preview": "https://p.scdn.co/mp3-preview/10d2a276bddb0fe1498bdd09cde03262957c2f73?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "Green Day",
                "album": "Insomniac",
                "date": "1995-10-10",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d000048518bd9e4c6bd1e33dc9b1e9771",
                "name": "Jaded",
                "preview": None,
                "artist": "Miley Cyrus",
                "album": "NOW That's What I Call Music! Vol. 88",
                "date": "2023-10-27",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851ded71e819c335a966aca6ae7",
                "name": "jaded",
                "preview": "https://p.scdn.co/mp3-preview/b42678946c3f01b5a830ccbfb3f483ddeb3e3361?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "sadeyes",
                "album": "jaded",
                "date": "2018-12-03",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d000048512726fa0e66447dc4b20b5ed8",
                "name": "jaded",
                "preview": "https://p.scdn.co/mp3-preview/4c804a9dc048aad89d15dfef5cac424012a5d571?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "Yot Club",
                "album": "aquarium",
                "date": "2019-01-13",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851c185e37be2a06b5c6f2dc704",
                "name": "Jaded",
                "preview": None,
                "artist": "Drake",
                "album": "Scorpion",
                "date": "2018-06-29",
            },
            {
                "cover": "https://i.scdn.co/image/ab67616d00004851cf550c9160838d10ee4ded2a",
                "name": "Jaded",
                "preview": "https://p.scdn.co/mp3-preview/90e12e7242334af254f8f41c9856a591fb4e7f2d?cid=51548009223c4ba0b2f5b33c5aaf1d96",
                "artist": "Betcha",
                "album": "Placebo",
                "date": "2023-08-25",
            },
        ]
        EXPECTED_3 = ""
        EXPECTED_4 = ""
        EXPECTED_5 = ""

        # compare result array extracted from result of get_tracks_from_search to the expected result given by the Spotify Web API
        self.assertEqual(RESULT_1, EXPECTED_1)
        self.assertEqual(RESULT_2, EXPECTED_2)
        self.assertEqual(RESULT_3, EXPECTED_3)
        self.assertEqual(RESULT_4, EXPECTED_4)
        self.assertEqual(RESULT_5, EXPECTED_5)


if __name__ == "__main__":
    unittest.main()
