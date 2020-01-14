from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

websites, pages, articles = [],[],[]

class website(Resource):
    def get(self, name):
        for site in websites:
            if site['name']==name:
                return site
        
    def post(self,name,author):
        import datetime
        date=datetime.datetime.today().strftime('%D')
        site = {'name':name,'author':author,'date posted':date}
        websites.append(site)
        return 'website posted',200
                
    
class page(Resource):
    def get(self, name):
        for p in pages:
            if p['name']==name:
                return p
        
    def post(self,name,author):
        import datetime
        date=datetime.datetime.today().strftime('%D')
        p = {'name':name,'author':author,'date posted':date}
        pages.append(p)
        return 'page posted',200
    
class article(Resource):
    def get(self, name):
        for a in articles:
            if a['name']==name:
                return a
        
    def post(self,name,author):
        import datetime
        date=datetime.datetime.today().strftime('%D')
        a = {'name':name,'author':author,'date posted':date}
        articles.append(a)
        return 'article posted',200

api.add_resource(website,'/website/<string:name>')
api.add_resource(page,'/page/<string:name>')
api.add_resource(article,'/article/<string:title>')

app.run(port=5000)
