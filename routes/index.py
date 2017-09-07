from flask import (
    render_template,
    Blueprint,
    request,
    redirect,
    url_for,
)

from models import current_user

main = Blueprint('index', __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/phone")
def phone():
    return render_template("phone.html")


@main.route("/phone/add", method=["POST"])
def phone_add():
    form = request.form
    phone = form.get('phone', None)

    u = current_user()
    if phone is not None:
        u.phone = phone
        u.save()
        return render_template('profile.html', u=u)
    else:
        return redirect(url_for('index.phone'))
