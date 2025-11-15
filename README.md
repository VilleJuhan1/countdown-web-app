# Countdown app Development version

This repository is specifically created for testing out a containerized development environment. It starts a very lightweight countdown web app for pre-Christmas party. Just modify the /templates/index.html file if you want to use it for some other purpose.

The countdown target is formatted using a .env file in the project root folder, ie. "TARGET_DATE=December 13, 2025 12:00:00".

## How to develop the app further using Docker Compose

Go to project directory and spin up the container environment

```bash
docker compose up
```

The app should now be running in http://localhost:5001. Every change you make to the following files and folders will prompt a reload:

_.py
_.env
./static/_
./templates/_

However you have to reload the browser session for the changes to be visible.
