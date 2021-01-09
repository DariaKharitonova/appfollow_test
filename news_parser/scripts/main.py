from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from news_parser.news import Post
import os
from news_parser.get_news import insert_to_db
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), '../news_history.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

insert_to_db()
scheduler.add_job(insert_to_db, trigger='interval', minutes=10)
scheduler.start()


@app.route('/posts', methods=['GET'])  # to get all news
def get_news_history():
    posts = Post.query.all()
    return jsonify(Post.serialize_list(posts))
