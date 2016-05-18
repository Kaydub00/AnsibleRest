#!/usr/bin/python

import ansible.runner
import ansible.playbook
import sys
import json
import yaml
from ansible import callbacks
from ansible import utils

class playbookrunner:

  def __init__(self, inventoryfile, playbookfile):
    self.inventoryfile = inventoryfile
    self.playbookfile = playbookfile

  def execute(self):
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=1)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=1)
    pb = ansible.playbook.PlayBook(
        playbook=self.playbookfile,
        host_list=self.inventoryfile,
        stats=stats,
        callbacks=playbook_cb,
        runner_callbacks=runner_cb
    )
    ret = pb.run()
    return ret









