import obspython as obs
import tweepy

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
    tweet("I have started streaming!\nCome and watch.")

def stop_streaming():
    tweet("I have stopped streaming.\nThanks for watching!")

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

