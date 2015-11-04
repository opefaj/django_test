from __future__ import with_statement
from fabric.api import *

def prepare_deploy():
	local("./manage.py test my app")
	local("git add -p && git commit")
	local("git push")