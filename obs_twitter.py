import obspython as obs
import tweepy
import time

# Twitter API credentials (replace with your own)
client = tweepy.Client(
    consumer_key='YOUR_CONSUMER_KEY',
    consumer_secret='YOUR_CONSUMER_SECRET',
    access_token='YOUR_ACCESS_TOKEN',
    access_token_secret='YOUR_ACCESS_TOKEN_SECRET'
)

def tweet(message):
    try:
        client.create_tweet(text=message)
        obs.script_log(obs.LOG_INFO, f"Tweeted: {message}")
    except Exception as e:
        obs.script_log(obs.LOG_WARNING, f"Error tweeting: {e}")

def start_streaming():
    unix_time = int(time.time())
    tweet(f"I have started streaming!\nCome and watch.\n{unix_time}")

def stop_streaming():
    unix_time = int(time.time())
    tweet(f"I have stopped streaming.\nThanks for watching!\n{unix_time}")

def on_event(event):
    if event == obs.OBS_FRONTEND_EVENT_STREAMING_STARTED:
        obs.script_log(obs.LOG_INFO, "Stream started, sending tweet...")
        start_streaming()
    elif event == obs.OBS_FRONTEND_EVENT_STREAMING_STOPPED:
        obs.script_log(obs.LOG_INFO, "Stream stopped, sending tweet...")
        stop_streaming()

def script_load(settings):
    obs.script_log(obs.LOG_INFO, "Script loaded, waiting for streaming events...")
    obs.obs_frontend_add_event_callback(on_event)

