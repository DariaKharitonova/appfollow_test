from sqlalchemy import desc, asc
from flask import jsonify, Blueprint
from news_parser.news import Post
from webargs import fields
from webargs.flaskparser import use_args
from marshmallow import validate
from news_parser.settings import app


@app.route('/posts', methods=['GET'])  # to get all news
@use_args({
    "offset": fields.Int(missing=0, validate=lambda n: n >= 0),
    "limit": fields.Int(missing=5, validate=lambda n: n >= 0),
    "order": fields.String(missing="id", validate=validate.OneOf(['id', 'title', 'link', 'post_id', 'created_at'])),
    'sort': fields.String(missing='asc', validate=validate.OneOf(['asc', 'desc']))
    },
    location="query")
def get_news_history(args):
    offset = args.get('offset')
    limit = args.get('limit')
    order = args.get('order')
    sort = asc if args.get('sort') == 'asc' else desc

    posts = Post.query.order_by(sort(order)).offset(offset).limit(limit).all()
    return jsonify(Post.serialize_list(posts))
