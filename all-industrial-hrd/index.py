#!/usr/bin/env python

import os
import webapp2
import sys
import cgi
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
  def get(self):
    path = self.request.path

    if path == '/':
        temp = os.path.join(os.path.dirname(__file__),'templates/index.html')
    else:
		temp = os.path.join(os.path.dirname(__file__),'templates/%s' % path)
		if not os.path.isfile(temp):
			temp = os.path.join(os.path.dirname(__file__),'templates/404.html')
			self.response.set_status(404)
		  

    outstr = template.render(temp, {'path': path})
    self.response.out.write(outstr)


	  
application = webapp2.WSGIApplication([('/.*', MainHandler)],
							   debug=True)	  
	  
	  
