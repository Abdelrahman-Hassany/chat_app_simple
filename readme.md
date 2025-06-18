# Django Channels Simple Chat App

This is a minimal real-time chat application built using Django Channels. It demonstrates how to implement WebSocket-based communication in Django using asynchronous consumers and Redis as the channel layer backend.

## Features

- One-to-many group chat (room-based)
- Real-time messaging using WebSockets
- Simple frontend with HTML, CSS, and vanilla JavaScript
- Redis as the channel layer, running inside WSL on Windows

## Tech Stack

- Django
- Django Channels
- Channels Redis
- Redis (via WSL)
- HTML/CSS/JavaScript (no frontend frameworks)

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/yourusername/django-chat-app.git
cd django_chat_app
```

# Set up the virtual environment

```
pipenv install django channels channels_redis
pipenv shell

```

# Configure the Django project

Make sure settings.py includes:

```
INSTALLED_APPS = [
    ...
    'channels',
    'chat_app',
]

ASGI_APPLICATION = 'chat_project.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}


```

# Enable Redis using WSL

```
sudo apt update
sudo apt install redis-server
sudo service redis-server start

```
## to test redis if it work 

```
redis-cli >> will open (127.0.0.1:6379>)

127.0.0.1:6379> ping 

```
should return: PONG

# Run migrations

```
python manage.py migrate

```

# Start the ASGI server using Uvicorn

```
uvicorn chat_project.asgi:application --reload

```

# Open the chat in your browser

Visit: http://127.0.0.1:8000/chat/

Open in two tabs or windows to test real-time messaging.

# project structure

django_chat_app/
├── chat_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py        # ASGI entry point
│   └── wsgi.py
├── chat_app/
│   ├── __init__.py
│   ├── models.py      # Message model
│   ├── views.py       # chat_view
│   ├── consumers.py   # WebSocket consumer
│   ├── routing.py     # WebSocket URL patterns
│   ├── urls.py
│   └── templates/
│       └── chat_template.html


## Database Usage & Suggestions

Although this demo uses a database (SQLite by default), it currently does **not** store chat messages. All messages are exchanged in real-time using WebSockets, and once the page is refreshed, previous messages are lost.

If you want to extend this project to support message history and more realistic chat behavior, consider the following enhancements:

### Suggested Improvements

1. **Persist Messages in Database**  
   Save each incoming message to the database in `ChatConsumer.receive()` using Django's ORM. This will allow chat history to be displayed when a user reopens the chat.

2. **Load Previous Messages on Page Load**  
   Use a regular Django view to fetch previous messages from the database and render them in the chat template when the page loads.

3. **User Authentication**  
   Integrate Django's built-in authentication system to allow users to log in and identify who sent each message.

4. **Private 1-to-1 Chat**  
   Extend the app to allow direct messaging between users by creating unique WebSocket rooms per user-pair.

5. **Message Read/Delivery Status**  
   Add status indicators for whether messages have been delivered or read.

6. **Responsive UI**  
   Improve the frontend design using Bootstrap or Tailwind CSS to make the chat interface more visually appealing and mobile-friendly.

7. **Notifications**  
   Add real-time browser or in-app notifications when a new message is received and the user is not focused on the tab.

---

You can pick any of these features to build a more complete real-time messaging app and showcase your skills in Django, WebSockets, and asynchronous programming.
