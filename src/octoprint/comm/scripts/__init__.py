# coding=utf-8
from __future__ import absolute_import, unicode_literals

__license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'
__copyright__ = "Copyright (C) 2018 The OctoPrint Project - Released under terms of the AGPLv3 License"


class Script(object):

	def __init__(self, name, renderer, context=None):
		if context is None:
			context = dict()

		self.name = name
		self.renderer = renderer
		self.context = context

	def render(self, context=None):
		if context is None:
			context = dict()

		render_context = dict(self.context)
		render_context.update(context)

		return self.renderer(render_context).split("\n")