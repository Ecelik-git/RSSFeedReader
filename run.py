from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

@app.route("/")

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/data/", methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        feed_url = request.form['feed_url']
        entries = []
        feed = feedparser.parse(feed_url)
        entries.extend(feed.entries)
        return render_template('data.html', entries=entries)

app.run(debug=True)
