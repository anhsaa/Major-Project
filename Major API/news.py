from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import api
from datetime import datetime
from dbConnection import conn
from utilizies.jsonconverter import databaseJsonConverter
from authen import token_required


news=api.model('News', {
    'image': fields.String(required=True, description='The task details'),
    'title': fields.String(required=True,description='The task details'),
    'date': fields.Date(required=True,description='The task details'),
    'description': fields.String(required=True,description='The task details'),

    })

name_space=api.namespace('News','all about news ')
@cross_origin
@name_space.route("/CRUD",methods=['POST'])
@name_space.route('/CRUD/<int:news_id>',methods=['PUT','GET','DELETE'])
class newsCRUD(Resource):
    @api.expect(news)
    @token_required
    @api.doc(params={'image':'As string','title':'As integer','date':'As integer','description':'As integer'})
    
    def post(self):
        dbconn=conn()
        cur = dbconn.cursor()
        try:
            image=request.json['image']
            title=request.json['title']
            date=request.json['date']
            description=request.json['description']
            cur.execute("INSERT INTO news (image, title, date, description) VALUES (%s, %s, %s, %s)",(image, title, date, description,))
            dbconn.commit()
            if cur.rowcount > 0:
                return json.dumps({'msg':'Successfully','status_code':'200'})
            else:
                return json.dumps({'msg':'Already','status_code':'400'})
        except Exception as e:
            raise e
        finally:
            cur.close()
            dbconn.close()

    @token_required
    @api.expect(news)
    @api.doc(params={'image':'As string','title':'As integer','date':'As integer','description':'As integer'})
    def put(self,news_id=0):
        dbconn=conn()
        cur1 = dbconn.cursor()
        try:
            image=request.json['image']
            title=request.json['title']
            date=request.json['date']
            description=request.json['description']
            cur1.execute("UPDATE news SET image=%s, title=%s, date=%s, description=%s WHERE news_id=%s",(image,title,date,description,news_id,))
            dbconn.commit()
            return json.dumps({'msg':'update Successfully','status_code':'200'})
        
        except Exception as ex:
            raise ex
        finally:
            cur1.close()
            dbconn.close()
        
    @token_required
    def delete(self, news_id=0):
        dbconn=conn()
        cur8 = dbconn.cursor()
        try:
            cur8.execute("DELETE FROM news WHERE news_id = %s", (news_id,))
            dbconn.commit()
            return json.dumps({'msg': 'Delete successful', 'status_code': 200})
        except Exception as ex:
            raise ex
        finally:
            cur8.close()
            dbconn.close()
        
        
        

newsdate_model = api.model('Date', {
'datefrom': fields.Date(required=True, description='News date'),

})
name_space3=api.namespace('Getnews','all about news of fustsal')
@cross_origin
@name_space3.route('/get_news',methods=['POST'])
class dateCRUD(Resource):
    @token_required
    @api.expect(newsdate_model)
    @api.doc(params={'datefrom': 'As date',})
    
    def post(self):
        dbconn=conn()
        cur5 = dbconn.cursor()
        try:
            datefrom = request.json['datefrom']
            cur5.execute("SELECT * FROM news WHERE date >= %s", (datefrom,))
            data1 = databaseJsonConverter(cur5)

            if data1:
                return ({'msg': data1, 'status_code': 200})
            else:
                return ({'msg': 'No found', 'status_code':400})

        except Exception as ex1:
            raise ex1

        finally:
            cur5.close()
            dbconn.close()

 

