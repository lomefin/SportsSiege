import webapp2
import logging
logging.getLogger().setLevel(logging.DEBUG)

class DefaultRouter(webapp2.RequestHandler):
    def get(self):
    	logging.info( "Default router")
        self.response.headers['Content-Type'] = 'text/plain'
        from jinja2 import Template
        template = Template('Hello {{name}}!')
        out = template.render(name='World')
        self.response.out.write(out)


class NotFoundHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info( "Not found handler")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('Not Found!')
        self.response.set_status(404)


not_found = webapp2.WSGIApplication([('/.*', NotFoundHandler)])
default = webapp2.WSGIApplication([('/*', DefaultRouter)])

def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! I could swear this page was here!')
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A server error occurred!')
    response.set_status(500)


default.error_handlers[404] = handle_404
default.error_handlers[500] = handle_500