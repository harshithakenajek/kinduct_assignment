from flask import Flask
from kinduct.routes.message_route import message_route

def root_app(app,prefix):
    app.register_blueprint(
            message_route,url_prefix="/{prefix}/api/v1".format(prefix=prefix))
    