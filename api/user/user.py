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
        is_success = False
        Body = request.get_json()
        #이름 비밀번호 닉네임
        id = Body["id"]
        pw = Body["pw"]
        nickname = Body["nickname"]
        # POST method 구현 부분
        database  = Database()
        """
        SELECT 필드이름
        FROM 테이블이름
        [WHERE 조건]"""
        #데이터 확인
        #select EXISTS (select id from 테이블이름 where 컬럼=찾는 값 limit 1) as success;
        is_success = database.execute_one("SELECT EXISTS(SELECT * FROM user WHERE id = '{}')as success".format(id) )
        bool_success = is_success['success']
        if(1-bool_success):
            #데이터 삽입
            #INSERT INTO `{테이블의 이름}` VALUES ({열의 순서에 따른 데이터});
            postData = "INSERT INTO user VALUES ('{}', '{}', '{}');".format(id, pw, nickname)
            database.execute(postData)
            database.commit()
            database.close()
            return {
            "is_success": 'true',
            "message" : "유저 생성 성공"
            },200
        else:
            database.commit()
            database.close()
            return{
                "is_success": 'false',
                "message" : "이미 있는 유저"
            },400
        


        """def post():
        param = request.get_json()
        name = param['name']
        return name
        #return jsonify(param)

        """
    def put(self):        
        # PUT method 구현 부분
        Body = request.get_json()
        #이름 비밀번호 닉네임
        id = Body["id"]
        pw = Body["pw"]
        nickname = Body["nickname"]
        # POST method 구현 부분
        database  = Database()
        """
        SELECT 필드이름
        FROM 테이블이름
        [WHERE 조건]"""
        #데이터 확인
        #select EXISTS (select id from 테이블이름 where 컬럼=찾는 값 limit 1) as success;
        isId = database.execute_one("SELECT EXISTS(SELECT * FROM user WHERE id = '{}')as success".format(id) )
        boolId = isId['success']
        
        isPw = database.execute_one("SELECT EXISTS(SELECT * FROM user WHERE pw = '{}')as success".format(pw) )
        boolPw = isPw['success']
        
        isNickname = database.execute_one("SELECT EXISTS(SELECT * FROM user WHERE nickname = '{}')as success".format(nickname) )
        boolNickname = isNickname['success']
        
        if(boolNickname):
            database.commit()
            database.close()
            return{
                "is_success": 'false',
                "message" : "현재 닉네임과 같음"
            },400
        
        
        if(boolId and boolPw):
            #데이터 업데이트
            #update 테이블 set 컬럼 = '값' where 컬럼 = '값';
            postData = "update user set nickname = '{}' where id = '{}';".format(nickname, id)
            database.execute(postData)
            database.commit()
            database.close()
            return {
            "is_success": 'true',
            "message" : "유저 닉네임 변경 성공"
            },200
        else:
            database.commit()
            database.close()
            return{
                "is_success": 'false',
                "message" : "아이디나 비밀번호 불일치"
            },400


    
    def delete(self):
        # DELETE method 구현 부분
        Body = request.get_json()
        #이름 비밀번호 닉네임
        id = Body["id"]
        pw = Body["pw"]
        nickname = Body["nickname"]
        # POST method 구현 부분
        database  = Database()
        """
        SELECT 필드이름
        FROM 테이블이름
        [WHERE 조건]"""
        #데이터 확인
        #select EXISTS (select id from 테이블이름 where 컬럼=찾는 값 limit 1) as success;
        isId = database.execute_one("SELECT EXISTS(SELECT * FROM user WHERE id = '{}')as success".format(id) )
        boolId = isId['success']
        
        isPw = database.execute_one("SELECT EXISTS(SELECT * FROM user WHERE pw = '{}')as success".format(pw) )
        boolPw = isPw['success']
        
        if(boolId and boolPw):
            #데이터 삭제
            #DELETE FROM 테이블 WHERE 컬럼 = '값';
            postData = "DELETE FROM user WHERE id = '{}';".format(id)
            database.execute(postData)
            database.commit()
            database.close()
            return {
            "is_success": 'true',
            "message" : "유저 삭제 성공"
            },200
        else:
            database.commit()
            database.close()
            return{
                "is_success": 'false',
                "message" : "아이디나 비밀번호 불일치"
            },400