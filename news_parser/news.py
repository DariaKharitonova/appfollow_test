from news_parser.settings import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    post_id = db.Column(db.String(255), nullable=False, unique=True, sqlite_on_conflict_unique='IGNORE')
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    #
    # def __repr__(self):
    #     return "<Post(title='%s', link='%s', created='%s')>" % (
    #                             self.title, self.link, self.created_at)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.link,
            'created': self.created_at
        }

    @staticmethod
    def serialize_list(posts):
        return [post.serialize() for post in posts]


def add_news(_heading, _link, _post_id):
    new_news = Post(title=_heading, link=_link, post_id=_post_id)
    db.session.add(new_news)
    db.session.commit()
