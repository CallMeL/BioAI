# BMTools with Spotify tool

## How to run

after install all the packages using `pip install -r requirements.txt`, open two termial windows under the root folder of this project

* For the service:

```
export OPENAI_API_KEY= 'Your key'
export SPOTIPY_CLIENT_ID='Your client ID'
export SPOTIPY_CLIENT_SECRET='Your secret'
export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'
./myenv/bin/python host_local_tools.py
```

* For tools

```
export OPENAI_API_KEY= 'Your key'
export SPOTIPY_CLIENT_ID='Your client ID'
export SPOTIPY_CLIENT_SECRET='Your secret'
export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'
./myenv/bin/python web_demo.py
```

