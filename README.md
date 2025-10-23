# Autonomous Cyber Incident Response Bot

This Python bot monitors system authentication logs and detects multiple failed login attempts from the same IP, triggering automated alerts and response.

## Features

- Cross-platform support (Linux & Windows)
- Real-time monitoring using file watching or Windows Event Log queries
- Configurable thresholds and time windows for detection
- Simulates IP blocking on detection

## Setup & Running

1. Create and activate Python virtual environment:
python -m venv venv

## Activate on Windows:
.\venv\Scripts\activate

## Activate on Linux/macOS:
source venv/bin/activate

2. Install dependencies:
pip install -r requirements.txt

3. Run the bot:
python incident_response_bot.py

- On Linux, you may need to run with `sudo` for log access:
sudo python incident_response_bot.py

- On Windows, run terminal with Administrator privileges.
- On Windows, the bot reads Security Event Logs for failed login events.