import requests
import sys
import json
import sqlite3
from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)


@app.route("/b", methods=["GET", "POST"])
def receive_location():
    if request.method == 'POST':
        conn = sqlite3.connect('location.db')
        cur = conn.cursor()
        latitude, longitude = request.form.get("latitude"), request.form.get("longitude")
        cur.execute("INSERT INTO location (latitude, longitude) VALUES (?, ?)", (latitude, longitude))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("index.html")

# from flask import Flask, render_template, jsonify, request

# app = Flask(__name__)

# @app.route("/a", methods=["GET", "POST"])
# def receive_location():
#     if request.method == 'POST':
#         data = request.get_json()
#         latitude = data.get('latitude')
#         longitude = data.get('longitude')
#         return jsonify({'status': 'success', 'latitude': latitude, 'longitude': longitude})
#     return render_template("index.html")
