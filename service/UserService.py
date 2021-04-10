import requests
class UserService:
    def getTokenString(self,user):
        auth_uri="http://localhost:8080/api/auth"
        info =  {}
        info["username"] = user.username
        info["password"] = user.password
        response=requests.post(auth_uri,json=info)
        if (response.status_code != 200):
            return 0
        response_json=response.json()
        return response_json["type"]+" "+response_json["token"]

