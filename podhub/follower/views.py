from app import app
from feed import Feed
from flask import jsonify, request


@app.route('/')
def index():
    return jsonify()


@app.route('/audio')
def feed(feed_id, index):
    url = request.args.get('feed_url')
    index = request.args.get('index')

    feed = Feed(url=url)

    try:
        entry = feed.lookup.get(index)
    except TypeError:
        return jsonify(error_message='index must be an integer.'), 400
    except IndexError:
        return jsonify(error_message='episode {} not found'.format(index)), 400

    return jsonify(feed_url=entry.audio)
