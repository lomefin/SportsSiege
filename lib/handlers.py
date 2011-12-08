import webapp2

class LLHandler(webapp2.RequestHandler):

	def get(self):
		self.internal_get()

	def post(self):
		self.internal_post()
