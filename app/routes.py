from app import app, login

from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, BigArtist, SmallArtist

from flask import redirect, url_for, flash, request, jsonify

from app.forms import RegistrationForm, LoginForm
from app import db

from app import spotify_support


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    user = request.get_json()
    username = user['username']
    password = user['password']

    if username and password:
        new_user = User(username=username, spotify_access='x')
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return {'user': username}, 200
    else:
        return {'errors': 'ah shit something happened with registration'}, 400

@app.route('/spot-login', methods=['POST'])
def spot_login():
    user = request.get_json()
    username = user['value']
    if username:
        auth_url = spotify_support.login_spotify(username)
        print(auth_url)
        if auth_url['auth']:
            print("AUTH URL:", auth_url)
            return {'response': auth_url['value']}
        else:
            return {'response': 'logged'}
    else:
        return {'error':'Please enter your username.'}


@app.route('/logged', methods=['POST'])
def logged():
    print("VALUE OF LOGGED",request.get_json()['value'])
    spotify_support.auth_handler(request.get_json()['value'])
    return {'logged': True}

@app.route('/login', methods=['GET', 'POST'])
def login():

    user_query = request.get_json()
    username = user_query['username']
    password = user_query['password']

    print("THINGS", username, password)

    if username and password:
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            login_user(user, False)
            return {'response': '/'}, 200
        return jsonify({'errors': {'Forbidden:': "INVALID CREDENTIALS"}}), 403
    else:
        return {'errors': "ah shit you couldn't log in"}, 400

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return {"success": 200}

@app.route('/search', methods = ['POST'])
def search():
    artist = request.get_json()
    name = artist['value']
    try:
        artist_obj = BigArtist.query.filter_by(name=name).first()
        print(artist_obj)
        if artist_obj:
            genres = [artist_obj.genre1, artist_obj.genre2, artist_obj.genre3]
            new_artists = spotify_support.recommend_artists(name, genres)
            new_images = []
            for i in new_artists:
                new_images.append([i, spotify_support.get_image(i), spotify_support.get_url(i)])
            playlist = spotify_support.make_playlist(name, new_artists, genres)
            artist_view = {
                'playlist': playlist[0],
                'new_artists': new_images,
                'playlist_name': playlist[1]
            }
            return artist_view
        else:
            return {'error':'Artist Unavailable, please check spelling or try another artist.'}


    except:
        return {'error':'There was an issue with something or other'}
