#!/usr/bin/env python
# coding: utf-8

import cherrypy

# Namespace imports
import aaa
import bbb
import ccc


@cherrypy.expose
def index(*args, **kwargs):
    return u"/index"

