#!/usr/bin/env python
from setuptools import setup

setup(
	name=u'celerity',
	version=u'0.0.1',
	author=u'Justin Duke',
	license=u'...',
	description=u'A self-contained Hastebin CLI.',
	scripts=['celerity.py'],
	entry_points={
		'console_scripts':['celerity = celerity:main']
	},
)