import os
import webapp2
import sys
import cgi
import logging
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import mail

class MainHandler(webapp2.RequestHandler):

    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.htm')
        self.response.out.write(template.render(path, template_values))

class ContactHandler(webapp2.RequestHandler):

    def post(self):
        name = self.request.get("name")
        name = name.strip()
        company = self.request.get("company")
        company = company.strip()
        phone = self.request.get("phone")
        phone = phone.strip()
        email = self.request.get("email")
        email = email.strip()
        content = self.request.get("message")
        content = content.strip()

        errors = ''
        if not name:
            template_values = {'name': 'Y'}
            errors = 'Y'
        if not company:
            template_values = {'company': 'Y'}
            errors = 'Y'
        if not phone:
            template_values = {'phone': 'Y'}
            errors = 'Y'
        if not email:
            template_values = {'email': 'Y'}
            errors = 'Y'
        if not content:
            template_values = {'content': 'Y'}
            errors = 'Y'
        
        if not errors:
            message = mail.EmailMessage(sender='tye@allindustrialsupply.com', reply_to=email, subject="Contact page inquiry form submission")
            message.to = "AIES <contactus@allindustrialsupply.com>"
            message.body = """
Name: %s
Company: %s
Phone: %s
Email: %s
Message: %s
            """ %(name,company,phone,email,content)
            message.send()
            template_values = {'sented': 'Y'}
        else:
            template_values = {'sender': 'Y'}
      
        path = os.path.join(os.path.dirname(__file__), 'templates/contactus.html')
        self.response.out.write(template.render(path, template_values))

application = webapp2.WSGIApplication([('/', MainHandler), ('/contact', ContactHandler)], debug=True)
