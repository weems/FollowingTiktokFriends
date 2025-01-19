import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# Load TikTok usernames from a JSON file
with open('tiktok_usernames.json', 'r') as file:
    usernames = json.load(file)

# Twitter authentication and follow
def authenticate_twitter():
    twitter_bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
    return {'Authorization': f'Bearer {twitter_bearer_token}'}

def follow_on_twitter(username, headers):
    url = f'https://api.twitter.com/2/users/by/username/{username}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_id = response.json()['data']['id']
        follow_url = f'https://api.twitter.com/2/users/{user_id}/follow'
        requests.post(follow_url, headers=headers)

# Instagram/Threads authentication and follow
def authenticate_instagram():
    instagram_access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
    return {'Authorization': f'Bearer {instagram_access_token}'}

def follow_on_instagram(username, headers):
    url = f'https://graph.instagram.com/v10.0/{username}?access_token={headers["Authorization"]}'
    response = requests.get(url)
    if response.status_code == 200:
        user_id = response.json()['id']
        follow_url = f'https://graph.instagram.com/{user_id}/follow'
        requests.post(follow_url, headers=headers)

# Bluesky authentication and follow
def authenticate_bluesky():
    bluesky_access_token = os.getenv('BLUESKY_ACCESS_TOKEN')
    return {'Authorization': f'Bearer {bluesky_access_token}'}

def follow_on_bluesky(username, headers):
    url = f'https://api.bluesky.com/v1/users/{username}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_id = response.json()['id']
        follow_url = f'https://api.bluesky.com/v1/users/{user_id}/follow'
        requests.post(follow_url, headers=headers)

# Mastodon authentication and follow
def authenticate_mastodon():
    mastodon_access_token = os.getenv('MASTODON_ACCESS_TOKEN')
    mastodon_instance = os.getenv('MASTODON_INSTANCE')
    return {'Authorization': f'Bearer {mastodon_access_token}', 'instance': mastodon_instance}

def follow_on_mastodon(username, headers):
    mastodon_instance = headers.pop('instance')
    url = f'https://{mastodon_instance}/api/v1/accounts/search?q={username}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200 and response.json():
        user_id = response.json()[0]['id']
        follow_url = f'https://{mastodon_instance}/api/v1/accounts/{user_id}/follow'
        requests.post(follow_url, headers=headers)

# Main function to follow users on all platforms
def follow_users(usernames):
    twitter_headers = authenticate_twitter()
    instagram_headers = authenticate_instagram()
    bluesky_headers = authenticate_bluesky()
    mastodon_headers = authenticate_mastodon()

    for username in usernames:
        follow_on_twitter(username, twitter_headers)
        follow_on_instagram(username, instagram_headers)
        follow_on_bluesky(username, bluesky_headers)
        follow_on_mastodon(username, mastodon_headers)

# Execute the function
follow_users(usernames)
print("Process completed.")
