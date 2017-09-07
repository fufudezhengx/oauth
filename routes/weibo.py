from flask import (
    redirect,
    session,
    url_for,
    Blueprint,
    request,
    flash,
)
from config.github_config import consumer_key, consumer_secret
from models.user import User

from flask_oauth import OAuth

main = Blueprint('weibo', __name__)

oauth = OAuth()

weibo = oauth.remote_app(
    'weibo',
    base_url=None,
    request_token_url=None,
    access_token_url='https://api.weibo.com/oauth2/access_token',
    authorize_url='https://api.weibo.com/oauth2/authorize',
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
)


@main.route('/login')
def login():
    return weibo.authorize(callback=url_for('weibo.oauth_authorized',
                                            next=request.args.get('next') or request.referrer or None))


@main.route('/oauth-authorized')
@weibo.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index.phone')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['weibo_token'] = (
        resp['access_token'],
        resp['expires_in']
    )


    form = dict(
        username=resp['name'],
        uid=resp['id']
    )
    u = User.new(form=form)
    flash('You were signed in as {}'.format(u.username))

    return redirect(next_url)
