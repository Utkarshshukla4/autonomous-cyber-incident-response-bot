## Contact

**Utkarsh Shukla**

Email- utqrshkumar07@gmail.com

GitHub- https://github.com/Utkarshshukla4


##  Overview

This bot automates the cyber incident response process — from detection to containment — using Python and predefined playbooks.  
It mimics enterprise SOC automation behavior for training or simulation.

##  Features

- Cross-platform support (Linux & Windows)
- Real-time monitoring using file watching or Windows Event Log queries
- Configurable thresholds and time windows for detection
- Simulates IP blocking on detection


##  Architecture

[Network / System Event]
      ↓
[Threat Detection Engine]
      ↓
[Response Playbook]
      ↓
[Mitigation Action]
      ↓
[Report Generation]


## Project Structure

cir-bot/
├── src/
├── playbooks/
├── logs/
├── docs/
│   └── architecture.png
├── requirements.txt
├── README.md
└── .gitignore


##  Installation

git clone https://github.com/Utkarshshukla4/autonomous_cyber_incident_response_bot.git

cd autonomous_cyber_incident_response_bot

pip install -r requirements.txt  {WINDOWS}

python3 -m pip install -r requirements.txt  {LINUX}


## Setup & Running

1. Create and activate Python virtual environment:

_Windows:_

python -m venv venv

venv\Scripts\activate

_Linux/macOS:_

source venv/bin/activate


2. Run the bot:
   
_Windows:_

python incident_response_bot.py

_Linux:_

python3 incident_response_bot.py

## Summary

This bot automates detection and mitigation of common cyber threats, reducing manual intervention.
