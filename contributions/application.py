from flask import Flask, flash, redirect, render_template, request, \
    session, url_for, jsonify
from flask_session import Session

from render_html import *
from dateutils import *


app = Flask(__name__)

if app.config['DEBUG']:

    @app.after_request
    def after_request(response):
        response.headers['Cache-Control'] = \
            'no-cache, no-store, must-revalidate'
        response.headers['Expires'] = 0
        response.headers['Pragma'] = 'no-cache'
        return response


app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route("/", methods=["GET"])
def index():

    # set jinja2 filters
    app.jinja_env.filters["tooltip"] = tooltip_text
    app.jinja_env.filters["display_date"] = dateutils.display_date
    app.jinja_env.filters['elapsed_time'] = dateutils.elapsed_time

    # to do; allow this to be changed without changing code!
    a = create_graph(['static/records/Mandarin (Minutes)', 'static/records/French (Minutes)'])

    return render_template('index.html',
                                        graphs=a[0],
                                        today=a[1],
                                        start=a[2],
                                        weekdays=a[3],
                                        month=a[4])