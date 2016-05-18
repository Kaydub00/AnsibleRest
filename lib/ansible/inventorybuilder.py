#!/usr/bin/python

import jinja2
from tempfile import NamedTemporaryFile

class inventorybuilder:

  inventory = """[activegroup]
{% for item in locations -%}
{{ item }}
{% endfor %}
"""

  def __init__(self, hostlist):
    self.hostlist = hostlist

  def getInventory(self):
    inventory_template = jinja2.Template(self.inventory)
    rendered = inventory_template.render({'locations': self.hostlist})
    return rendered

  def getInventoryFile(self):
    hosts = NamedTemporaryFile(delete=False)
    hosts.write(self.getInventory())
    hosts.close
    return hosts

