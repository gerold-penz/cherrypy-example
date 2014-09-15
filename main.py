#!/usr/bin/env python
# coding: utf-8

import cherrypy

# HTTP-root package
import http_root


def main():

    config = {
        "global": {
            # Server settings
            "server.socket_host": "0.0.0.0",
            "server.socket_port": 8080,
        },
        # "/": {
        #     #...
        # }
    }

    # Create, configure and start application
    app = cherrypy.Application(http_root, config = config)
    cherrypy.quickstart(app, config = config)


if __name__ == "__main__":
    main()

