#!/usr/bin/env python
# coding: utf-8

import cherrypy


@cherrypy.expose
def index(*args, **kwargs):
    return u"aaa/index"


