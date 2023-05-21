import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        dept = "Information Technology"
        seat_no = "T190058718"
        responseString = ""
        i=10

        while i>0:
            responseString = responseString + "<br><h1>Dept : {}, Seat_No : {}</h1>".format(dept,seat_no)
            i=i-1
        self.response.out.write(responseString)

app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
        


# import webapp2

# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         i=10
#         while i>0:
#             self.response.write("Megha<br>")
#             i = i-1 

# app = webapp2.WSGIApplication([('/',MainPage)],debug=True)