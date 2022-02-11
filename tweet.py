import random
import credentials
import schedule
import time
import tweepy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth = tweepy.OAuthHandler(
                      credentials.TWEEPY_API_KEY, 
                      credentials.TWEEPY_API_SECRET_KEY)
auth.set_access_token(
                  credentials.TWEEPY_ACCESS_TOKEN,
                  credentials.TWEEPY_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

sp = spotipy.Spotify(
              auth_manager=SpotifyClientCredentials(
              client_id=credentials.SPOTIPY_CLIENT_ID, 
              client_secret=credentials.SPOTIPY_CLIENT_SECRET))

def getRandomSearch():
  characters = 'abcdefghijklmnopqrstuvwxyz'
  randomSearch = ''

  for i in range (0, 2):
    randomCharacter = random.choice(characters)
    randomSearch += randomCharacter

  return randomSearch

def getRandomNumber():
  return random.randint(1, 15)

def setTweetMessage():
  randomSearch = getRandomSearch()
  randomOffset = getRandomNumber()
  randomNumber = getRandomNumber()
  print(randomSearch)
  print(randomOffset)
  message = ''
  
  results = sp.search(q=randomSearch, offset=randomOffset)
  for idx, track in enumerate(results['tracks']['items']):
    if idx == randomNumber:
      name = track['name']
      url = track['external_urls']['spotify']
      message = name + "\n" + url
      print(message)
      # api.update_status(message)

setTweetMessage()