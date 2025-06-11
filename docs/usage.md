# Usage

Install the required packages:

```bash
pip install -r requirements.txt
```

Set the following environment variables before starting the bot:

- `DISCORD_TOKEN` &mdash; Discord bot token used for authentication.
- `OFAC_API_KEY` &mdash; API key for submitting reports to OFAC.

Run the bot with:

```bash
python -m buster.discord_bot
```

The bot uses Python 3.11 or newer and requires internet access to file reports.
