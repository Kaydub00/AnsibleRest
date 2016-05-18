#!/usr/bin/python

import cherrypy
from cherrypy.lib import auth_basic
import pwd, os;
from lib.ansible import inventorybuilder
from lib.ansible import playbookrunner
from lib.foreman import foreman
import json
from lib.data.entity.playbooklocation import PlaybookLocation
from datetime import date
import datetime

class RestSpinUpService(object):
        exposed = True

        def POST(self, hostname=None):
		# Get the user and log
		#user = cherrypy.request.login
		#cherrypy.log(You can audit log here)
		if not isinstance(hostname, list):
			hostname = [hostname]
		x = inventorybuilder.inventorybuilder(hostname)
		invfile = x.getInventoryFile()
		invfile = invfile.name
		# Use DB to store playbooks and retrieve from DB
		playbook = "/location/of/playbook"
		pb = playbookrunner.playbookrunner(invfile,playbook)
		results = pb.execute()
		os.remove(invfile)
		# This directly returns Ansible results JSON
		return results