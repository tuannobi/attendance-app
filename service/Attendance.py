import requests
import json

class Attedance:
    def takeAttendace(self,token,class_id,student_id):
        uri="http://localhost:8080/api/attendances"
        headers={'Authorization':token}
        payload={}
        clazz={}
        student={}
        clazz["id"]=class_id
        student["id"]=student_id
        payload["student"]=student
        payload["clazz"]=clazz
        response=requests.post(uri,headers=headers,json=payload)
        if(response.status_code != 201):
            return False
        return True;