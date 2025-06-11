# Usage
To run the Buster prototype you need Python 3.11 or newer.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your Discord bot token and other settings as environment variables.
Buster requires a few environment variables to run:

- `DISCORD_TOKEN` – Discord bot token used to connect to the API.
- `DISCORD_APP_ID` – Application ID for slash command registration.
- `BUSTER_LOG_LEVEL` – Optional log level (default is `INFO`).

3. Start the bot (this repository does not yet include the implementation).
Install dependencies and run the bot:

    ```bash
    python -m buster.discord_bot
    ```

The [architecture documentation](architecture.md) provides more details on how the components fit together.
