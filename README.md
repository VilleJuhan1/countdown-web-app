# Countdown app Development version

This repository is specifically created for testing out a containerized development environment. It starts a very lightweight countdown web app for pre-Christmas party. Just modify the /templates/index.html file if you want to use it for some other purpose.

The countdown target is formatted using a .env file in the project root folder, ie. "TARGET_DATE=December 13, 2025 12:00:00".

## How to test locally

```bash
# Go to the project folder
cd CountdownApp

# Create and activate a Python virtual environment for the project
python3 -m venv venv
source venv/bin/activate  # use "venv\Scripts\activate" on Windows

# Install dependencies from the requirements.txt file
pip install -r requirements.txt

# Run the web app
python3 app.py
```

The App should be running in http://localhost:5001.

## How to deploy on Render

- Fork the project to your own repository.
- Go to https://render.com.
- Create a New Web Service
- From a Repository → choose your repo.
- Deploy!
