## Setup

1. Run Python Script

## Securing IG, Twitter/X, BlueSky, Threads Tokens/Credentials


To securely post the script on GitHub without exposing tokens, follow these steps:

1. **Use Environment Variables**: Store sensitive tokens in environment variables instead of hardcoding them in your script.

   Update your script to read tokens from environment variables:
   ```python
   import os
   
   twitter_bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
   instagram_access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
   bluesky_access_token = os.getenv('BLUESKY_ACCESS_TOKEN')
   ```

2. **Create a `.env` File**: Create a `.env` file to store your environment variables locally. This file should not be committed to GitHub.

   Example `.env` file:
   ```
   TWITTER_BEARER_TOKEN=your_twitter_token
   INSTAGRAM_ACCESS_TOKEN=your_instagram_token
   BLUESKY_ACCESS_TOKEN=your_bluesky_token
   ```

3. **Use a Library to Load Environment Variables**: Use a library like `python-dotenv` to load environment variables from the `.env` file.

   Install `python-dotenv`:
   ```sh
   pip install python-dotenv
   ```

   Update your script to load the `.env` file:
   ```python
   from dotenv import load_dotenv

   load_dotenv()

   twitter_bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
   instagram_access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
   bluesky_access_token = os.getenv('BLUESKY_ACCESS_TOKEN')
   ```

4. **Add `.env` to `.gitignore`**: Add the `.env` file to `.gitignore` to prevent it from being committed to the repository.

   Add the following line to your `.gitignore` file:
   ```
   .env
   ```

5. **Create a Sample Environment File**: Create a sample environment file (`.env.example`) without the actual tokens. This file can be committed to GitHub to show others how to set up their environment variables.

   Example `.env.example` file:
   ```
   TWITTER_BEARER_TOKEN=your_twitter_token
   INSTAGRAM_ACCESS_TOKEN=your_instagram_token
   BLUESKY_ACCESS_TOKEN=your_bluesky_token
   ```

Following these steps will help you securely post your script on GitHub without exposing sensitive tokens.
