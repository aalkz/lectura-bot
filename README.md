# Lectura Bot

The purpose of this Discord bot is to help organize activities within the [Spanish-English Learning Server](https://discord.gg/spanish-english). Specifically to help manage the Lectura queue.

<img src="https://img.shields.io/badge/python-%3E%3D%20v3.11-blue" alt="Python 3.11 or above required">


## Commands

Add oneself to the reading queue

```
/leer
```


# Instructions for preparing dev environment

## Discord setup

- [Create or use an existing bot application](https://discord.com/developers/applications)
- Turn ON server members intent

## Python setup

Create virtual environment

```
python -m venv venv
```

```
.\venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt -U
```

Make an `.env` file and configure the discord token y and the IDs of the channels where the bot will operate

```
# .env
DISCORD_TOKEN=
SERVER_ID=
LECTURA_TEXT_CHANNEL=
LECTURA_VC_CHANNEL=
TEST_TEXT_CHANNEL=
TEST_VC=
```

## Run
 
```
python bot.py
```
 
