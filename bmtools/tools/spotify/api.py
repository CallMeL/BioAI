import os
import traceback
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import json
from ..tool import Tool
import os
from bmtools import get_logger
logger = get_logger(__name__)

class SpotifyAPIWrapper:
    def __init__(self, client_id, client_secret, redirect_uri) -> None:
        self.client_id = '0d3011b0444d4f12854e74e696bc1b61'
        self.client_secret = '53bdbbe9d7004f1196048c5686c3bd77'
        self.redirect_uri = 'http://localhost'

        scope = ['playlist-modify-public', 'user-modify-playback-state']
        # self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        #     client_id=self.client_id,
        #     client_secret=self.client_secret,
        #     redirect_uri=self.redirect_uri,
        #     scope=scope
        # ))
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def show_related_artist(self,artist_name: str):
        result = self.sp.search(q='artist:' + artist_name, type='artist')
        uri = result['artists']['items'][0]['uri']
        related = self.sp.artist_related_artists(uri)
        output = "Artists related to artist_name : \n"
        for artist in related['artists']:
            output += " " + artist['name']
        return output
    def find_song_by_name(self, song_name: str):
        results = self.sp.search(q=song_name, type='track')
        logger.debug(song_name)
        logger.debug(results)
        # print('results for searching: \n')
        # print(results)
        if (results):
            song_uri = results['tracks']['items'][0]['uri']
            new_url = song_uri.replace("spotify:track:", "https://open.spotify.com/track/")
            print(new_url)
            return new_url
        else:
            return "No albums found for the specified singer."

    def recommendations_for_artist(self,artist_name: str):
        artists = self.sp.search(q='artist:'+artist_name, type='artist')
        items = artists['artists']['items']
        artist = items[0]
        logger.info(artist)
        response = self.sp.recommendations(seed_artists=[artist['id']])
        output = "Recommendation: \n"
        for track in response['tracks']:
            output += " " + track['name'] + "\n"

        return (output)


def build_tool(config) -> Tool:
    tool = Tool(
        "spotify",
        "Interact with the Spotify API",
        name_for_model="spotify",
        description_for_model=(
            "A tool to interact with Spotify. Use for search songs, managing playlists, controlling playback, and more."
        ),
        logo_url="https://your-app-url.com/.well-known/logo.png",
        contact_email="hello@contact.com",
        legal_info_url="hello@legal.com"
    )

    spotify_wrapper = SpotifyAPIWrapper(
        config["client_id"],
        config["client_secret"],
        config["redirect_uri"]
    )

    @tool.get('/show_related_artist')
    def show_related_artist(artist_name:str):
        """Get the related artists by artist's name"""
        return str(spotify_wrapper.show_related_artist(artist_name))

    @tool.get("/find_song_by_name")
    def find_song_by_name(song_name: str):
        """Get the url by song's name"""
        return str(spotify_wrapper.find_song_by_name(song_name))

    @tool.get("/recommend_for_artist")
    def recommendations_for_artist(artist_name:str):
        """Get the recommendations for similar songs by artist's name"""
        return str(spotify_wrapper.recommendations_for_artist(artist_name))

    return tool
