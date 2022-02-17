import random
import tweepy
import spotipy
import schedule
import time
from os import environ

TWEEPY_API_KEY = environ['TWEEPY_API_KEY']
TWEEPY_API_SECRET_KEY = environ['TWEEPY_API_SECRET_KEY']
TWEEPY_ACCESS_TOKEN = environ['TWEEPY_ACCESS_TOKEN']
TWEEPY_ACCESS_TOKEN_SECRET = environ['TWEEPY_ACCESS_TOKEN_SECRET']
SPOTIPY_CLIENT_ID = environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = environ['SPOTIPY_CLIENT_SECRET']

auth = tweepy.OAuthHandler(
                      TWEEPY_API_KEY, 
                      TWEEPY_API_SECRET_KEY)
auth.set_access_token(
                  TWEEPY_ACCESS_TOKEN,
                  TWEEPY_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

sp = spotipy.Spotify(
              auth_manager=spotipy.oauth2.SpotifyClientCredentials(
              client_id=SPOTIPY_CLIENT_ID, 
              client_secret=SPOTIPY_CLIENT_SECRET))

def getRandomSearch():
  characters = 'abcdefghijklmnopqrstuvwxyz'
  randomSearch = ''

  for i in range (0, 2):
    randomCharacter = random.choice(characters)
    randomSearch += randomCharacter

  return randomSearch

def getRandomNumber():
  return random.randint(1, 9)

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
      api.update_status(message)

def scheduleTweetMessage():
  schedule.every().day.do(setTweetMessage)

  while 1:
    schedule.run_pending()
    time.sleep(1)

scheduleTweetMessage()