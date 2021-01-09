from news_parser.news import *
from flask import jsonify, request, Response


@app.route('/news_history', methods=['GET'])  # to get all news
def get_news_history():
    return jsonify({'news': News.get_all_news()})


@app.route('/news_history', methods=['POST'])  # route to add new news
def add_news():
    request_data = request.get_json_output()
    News.add_news(request_data["heading"], request_data["link"],
                  request_data["date"])
    response = Response("News added", 201, mimetype='application/json')
    return response
