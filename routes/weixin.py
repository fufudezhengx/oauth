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

main = Blueprint('weixin', __name__)

oauth = OAuth()

weixin = oauth.remote_app(
    'weixin',
    base_url=None,
    request_token_url='https://api.weixin.qq.com//sns/userinfo',
    access_token_url='https://api.weixin.qq.com/sns/oauth2/access_token',
    authorize_url='https://open.weixin.qq.com/connect/qrconnect',
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
)


@main.route('/login')
def login():
    return weixin.authorize(callback=url_for('weixin.oauth_authorized',
                                             next=request.args.get('next') or request.referrer or None))


@main.route('/oauth-authorized')
@weixin.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index.phone')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['weixin_token'] = (
        resp['access_token'],
        resp['expires_in']
    )


    form = dict(
        username=resp['nickname'],
        uid=resp['openid']
    )
    u = User.new(form=form)
    flash('You were signed in as {}'.format(u.username))

    return redirect(next_url)
