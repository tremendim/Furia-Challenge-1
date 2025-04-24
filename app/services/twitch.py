import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")



def get_twitch_token():

    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()['access_token']

def get_live_streamers(streamers, token):
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {token}'
    }
    params = [('user_login', streamer) for streamer in streamers]
    response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
    response.raise_for_status()
    return response.json().get('data', [])
