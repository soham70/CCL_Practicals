import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__),'templates/index.html')
        self.response.out.write(template.render(path,template_values))
    def post(self):
        pin = self.request.get('pin')
        url = "https://api.postalpincode.in/pincode/"+str(pin)
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        
        
        if len(data)>0:
            post_offices = []
            for office in data[0]['PostOffice']:
                post_offices.append(office['Name'])
        else:
            post_offices = [] 
        template_values = {
            "post_offices":post_offices
        }
        path = os.path.join(os.path.dirname(__file__),'templates/results.html')
        self.response.out.write(template.render(path,template_values))
app=webapp2.WSGIApplication([("/",MainPage)],debug=True)