from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from preston import preston


# Main Flask app
app = Flask(__name__)
app.config.from_pyfile('config.cfg')

# ESI API connection
ESI = preston.Preston(
    user_agent='pyFlux EVE test',
    client_id=app.config['EVE_OAUTH_CLIENT_ID'],
    client_secret=app.config['EVE_OAUTH_SECRET'],
    callback_url=app.config['EVE_OAUTH_CALLBACK']
)

# # DB connection
# db.app = app
# db.init_app(app)

# User management
login_manager = LoginManager(app)
login_manager.login_message = ''
login_manager.login_view = 'login'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(ssl_context=(app.config['SSL_CERT'], app.config['SSL_KEY']))
