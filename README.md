# Sniper Discord Bot

A simple self-bot Discord bot designed to load commands dynamically and run tasks on a loop.

## Features

- Loads commands from the `cmds` folder dynamically.
- Executes periodic tasks with a customizable interval.
- Simple and lightweight configuration using `yaml`.

## Requirements

- Python 3.8+
- `discord.py-self` library
- `pyyaml` library

## Installation

⚠️ Make sure all requirements are installed correctly.

### Clone the repository

```bash
git clone https://github.com/quarterwire/sniper.git
cd sniper
py main.py
```

### Configure config.yml

Edit the config.yml file with your own details:

```yaml
token: "your_discord_bot_token"
message: "your message"
channels: [0, 1] # An lists of channels to send the same message. Make sure it is an integer
interval: 60 # Time interval for the message loop (in seconds)
```

### License

```sql Copyright (c) [2024] [Sniper]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
