from flask import (
    redirect,
    session,
    url_for,
    request,
    Blueprint,
    flash)
from flask_oauth import OAuth

from config.github_config import consumer_key, consumer_secret
from models.user import User

main = Blueprint('github', __name__)

oauth = OAuth()

github = oauth.remote_app(
    'github',
    base_url='https://api.github.com/',
    request_token_url='https://api.github.com/user',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='GET http://github.com/login/oauth/authorize',
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
)


@main.route('/login')
def login():
    return github.authorize(callback=url_for('github.oauth_authorized',
                                             next=request.args.get('next') or request.referrer or None))


@main.route('/oauth-authorized')
@github.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index.phone')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['github_token'] = (
        resp['access_token'],
        resp['expires_in']
    )


    form = dict(
        username=resp['login'],
        uid=resp['id']
    )
    u = User.new(form=form)
    flash('You were signed in as {}'.format(u.username))

    return redirect(next_url)
