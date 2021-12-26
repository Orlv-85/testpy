import requests

class Get_webtest:
    
     def get_users (self,a,b):
         resp=requests.get('http://127.0.0.1:5000/users', {a:b})
         return resp
