import webapp2
import jinja2
import os

MainPageHTML = "notes.html"

class MainPage(webapp2.RequestHandler)
    def get(self):
        self.response.write(MainPageHTML)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Handler(webapp2.RequestHandler): 
    """
    Basic Handler; will be inherited by more specific path Handlers
    """
    def write(self, *a, **kw):
        "Write small strings to the website"
        self.response.out.write(*a, **kw)  

    def render_str(self, template, **params):  
        "Render jinja2 templates"
        t = JINJA_ENVIRONMENT.get_template(template)
        return t.render(params)   

    def render(self, template, **kw):
        "Write the jinja template to the website"
        self.write(self.render_str(template, **kw)) 

class NotesHandler(Handler):
    def get(self):
        self.render("notes.html")

app = webapp2.WSGIApplication([('/', MainPage),('/notes', NotesHandler)],
                              debug = True)