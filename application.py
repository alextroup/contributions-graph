from flask import Flask, flash, redirect, render_template, request, \
    session, url_for, jsonify
from flask_session import Session
import os

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

    # get text / record files (must be in this folder)
    file_list = []
    for file in os.listdir("static/records"):
        file_list.append('static/records/' + file)
    file_list = sorted(file_list)

    graph_data = create_graph(file_list)

    return render_template('index.html',
                                        graphs=graph_data[0],
                                        today=graph_data[1],
                                        start=graph_data[2],
                                        weekdays=graph_data[3],
                                        month=graph_data[4])