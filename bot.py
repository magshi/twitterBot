from flask import Flask, render_template, request, redirect, session, url_for, flash
import tweet
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def tweet_data():
    body = request.json
    data = body['data']
    columns = body['columns']
    text_inserts = body['text_inserts']
    tweet.tweet(data, columns, text_inserts)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
