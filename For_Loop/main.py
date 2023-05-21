import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        name = "Soham"
        seat_no = "T190058718"
        dept = "Information Technology"
        responseString = ""

        for _ in range(5):
            responseString=responseString+ "<br><h1>Name : {},Seat : {},Department: {}</h1>".format(name,seat_no,dept)

        self.response.out.write(responseString)

app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
