from news_parser.settings import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    post_id = db.Column(db.String(255), nullable=False, unique=True, sqlite_on_conflict_unique='IGNORE')
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'created_at': self.created_at
        }

    @staticmethod
    def serialize_list(posts):
        return [post.serialize() for post in posts]

# TODO: test
def add_news(_title, _url, _post_id):
    new_post = Post(title=_title, url=_url, post_id=_post_id)
    db.session.add(new_post)
    db.session.commit()
