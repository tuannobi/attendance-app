import requests
import ast

class ClassService:
    def getClassByTeacherUsername(self,token,username):
        uri="http://localhost:8080/api/classes/teacher/"+username
        headers={'Authorization':token}
        response = requests.get(uri,headers=headers)
        # print(list(response.text))
        return ast.literal_eval(response.text)