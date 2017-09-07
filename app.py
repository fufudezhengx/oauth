from flask import Flask

from config.config import secret_key

from routes.index import main as index_routes
from routes.github import main as github_routes
from routes.weixin import main as weixin_routes
from routes.weibo import main as weibo_routes


def configured_app():
    app = Flask(__name__)

    app.secret_key = secret_key

    app.register_blueprint(index_routes)
    app.register_blueprint(github_routes, url_prefix='/github')
    app.register_blueprint(weixin_routes, url_prefix='/weixin')
    app.register_blueprint(weibo_routes, url_prefix='/weibo')

    return app


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
        threaded=True,
    )
    app = configured_app()
    app.run(**config)
