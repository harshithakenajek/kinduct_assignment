from flask import Flask
from kinduct.routes.message_route import message_route

def root_app(app):
        # from clinical_portal.utils.config import DevelopmentConfig

        # app.config.from_object(DevelopmentConfig)

    # print("prefix",prefix,app)
    app.register_blueprint(
            message_route)
    