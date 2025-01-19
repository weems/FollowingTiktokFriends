
# Following TikTok Friends

This project allows you to follow your TikTok friends on other social media platforms such as Twitter, Instagram, Threads, and Bluesky after the TikTok shutdown due to the Ban in the United States.

## Features

- Authenticate and follow users on Twitter, Instagram, Threads, and Bluesky.
- Securely manage API credentials and tokens.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- `python-dotenv` library (`pip install python-dotenv`)

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/weems/FollowingTiktokFriends.git
cd FollowingTiktokFriends
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Secure Your Credentials

Create a `.env` file in the root directory to store your API credentials. This file should not be committed to version control.

```sh
touch .env
```

Add your credentials to the `.env` file:

```env
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
INSTAGRAM_ACCESS_TOKEN=your_instagram_access_token
BLUESKY_ACCESS_TOKEN=your_bluesky_access_token
```

### 4. Update the Script

Ensure your script reads the credentials from the `.env` file. Example:

```python
from dotenv import load_dotenv
import os
import requests

load_dotenv()

twitter_bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
instagram_access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
bluesky_access_token = os.getenv('BLUESKY_ACCESS_TOKEN')

# Your script logic here...
```

### 5. Run the Script

Ensure you have a JSON file with TikTok usernames (e.g., `tiktok_usernames.json`).

```json
[
    "username1",
    "username2",
    "username3"
]
```

Run the script:

```sh
python script.py
```

## Securing Your Credentials

### Use Environment Variables

Storing credentials in environment variables helps prevent accidental exposure. Use the `python-dotenv` library to load these variables from a `.env` file.

### Add `.env` to `.gitignore`

Ensure your `.env` file is added to `.gitignore` to prevent it from being committed to your repository:

```sh
echo ".env" >> .gitignore
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
```

You can adjust the instructions and details based on your specific implementation and script logic.
