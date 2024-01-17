# OBS Studio Twitter Integration

## Overview

This script provides a simple integration between OBS Studio and Twitter, allowing users to automatically send tweets when their OBS Studio stream starts or stops. It's designed to keep your followers updated about your streaming activities directly through Twitter.

## Prerequisites

- OBS Studio installed with the `obspython` module.
- Python 3.11.4 environment set up with the `tweepy` library installed.
- Valid Twitter API credentials (Consumer Key, Consumer Secret, Access Token, and Access Token Secret).

## Installation

1. Ensure that OBS Studio and Python 3.11.4 are correctly installed on your system.
2. Install the `tweepy` library using pip:

```
pip install tweepy
```


## Configuration

1. Open the script in a text editor.
2. Replace `'YOUR_CONSUMER_KEY'`, `'YOUR_CONSUMER_SECRET'`, `'YOUR_ACCESS_TOKEN'`, and `'YOUR_ACCESS_TOKEN_SECRET'` with your actual Twitter API credentials.

## Usage

1. Load the script into OBS Studio.
2. Start or stop streaming in OBS Studio to trigger tweets automatically.
3. Check the OBS Studio logs to verify if tweets were sent successfully or if any errors occurred.

## Functionality

- `start_streaming()`: Sends a tweet when the stream starts.
- `stop_streaming()`: Sends a tweet when the stream stops.
- `on_event(event)`: Callback function that handles OBS Studio streaming events.
- `tweet(message)`: Function to send tweets.

## Logging

- The script logs its operations, providing messages about successful tweets or errors during the process in the OBS Studio log.

## License

- MIT License.

## Support

- For issues or support, create an issue in the GitHub repository or reach out to the maintainer.

Remember to replace your Twitter API keys with your actual keys and never share your keys publicly.
