from flask import Flask, render_template
from flask_restx import Resource, Api, fields
from flask import request, jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection, api


news = api.model('News', {
    'image': fields.String(required=True, description='The task details'),
    'title': fields.String(required=True, description='The task details'),
    'date': fields.Date(required=True, description='The task details'),
    'description': fields.String(required=True, description='The task details'),

})

name_space = api.namespace('News', 'all about news ')


@cross_origin
@name_space.route("/CRUD", methods=['GET', 'POST', 'PUT', 'DELETE'])
@name_space.route('/CRUD/<int:news_id>', methods=['POST'])
class newsCRUD(Resource):
    @api.expect(news)
    @api.doc(params={'image': 'As string', 'title': 'As string', 'date': 'As integer', 'description': 'As string'})
    def post(self):
        image = request.json['image']
        title = request.json['title']
        date = request.json['date']
        description = request.json['description']
        cur = dbconnection.cursor()
        cur.execute("INSERT INTO news (image, title, date, description) VALUES (%s, %s, %s, %s)",
                    (image, title, date, description,))
        dbconnection.commit()
        if cur.rowcount > 0:
            return json.dumps({'msg': 'Successfully', 'status_code': '200'})
        else:
            return json.dumps({'msg': 'Already', 'status_code': '400'})

    def put(self, news_id=0):
        image = request.json['image']
        title = request.json['title']
        date = request.json['date']
        description = request.json['description']
        cur1 = dbconnection.cursor()
        cur1.execute("UPDATE news SET image=%s, title=%s, date=%s, description=%s WHERE news_id=%s",
                     (image, title, date, description, news_id,))

        dbconnection.commit()
        update_news_id = cur1.lastrowid
        if update_news_id:
            return json.dumps({'msg': 'update Successfully', 'status_code': '200'})
        else:
            return json.dumps({'msg': 'Failed to update', 'status_code': '400'})

    def delete(self, news_id):
        cur8 = dbconnection.cursor()
        cur8.execute("DELETE FROM news WHERE news_id = %s", (news_id,))
        dbconnection.commit()

        if cur8.rowcount > 0:
            return json.dumps({'msg': 'Delete successful', 'status_code': 200})
        else:
            return json.dumps({'msg': 'Already deleted or no data found', 'status_code': 400})

    def get(self):
        cur9 = dbconnection.cursor()
        cur9.execute("select * from news")
        dat9 = cur9.fetchall()
        dbconnection.commit()
        results = []
        for row in dat9:
            dat9_datetime = row[2]  # Assuming datetime is at index 2
            if dat9_datetime is not None:
                dat9_str = dat9_datetime.strftime("%Y-%m-%d %H:%M:%S")
                results.append(dat9_str)
        if len(results) > 0:
            return json.dumps({'msg': results, 'status_code': '200'})
        else:
            return json.dumps({'msg': 'No valid datetime values found or no data available', 'status_code': '400'})
