from flask import Flask, request
from flask_restx import Resource, Namespace
from database.database import Database

user = Namespace('user')

@user.route('')
class UserManagement(Resource):
    
    def get(self):
        # GET method 구현 부분

        return {}

    def post(self):
        postBody = request.get_json()
        #이름 비밀번호 닉네임
        postId = postBody["id"]
        postPw = postBody["pw"]
        postNickname = postBody["nickname"]
        
        # POST method 구현 부분
        postDatabase  = Database()
        #INSERT INTO `{테이블의 이름}` VALUES ({열의 순서에 따른 데이터});
        postData = "INSERT INTO user VALUES ('{}', '{}', '{}');".format(postId, postPw, postNickname)
        postDatabase.execute(postData)
        postDatabase.commit()
        postDatabase.close()

        return postData



        """def post():
        param = request.get_json()
        name = param['name']
        return name
        #return jsonify(param)

        """
    def put(self):
        # PUT method 구현 부분
        return {}
    
    def delete(self):
        # DELETE method 구현 부분
        return {}