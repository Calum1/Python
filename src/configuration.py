import ConfigParser
import logging

from logging.handlers import RotatingFileHandler

from flask import Flask

app = Flask(__name__)

def init(app):
    config = configParser.ConfigParser()
    try:
        config_location="Python/src/etc/defaults.cfg"
        config.read(config_location)

        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")
    except:
        print "Could not read configs from: ", config_location

def logs(app):
    log_pathname = app.config['log_location'] + app.config['log_file']
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024* 1024 * 10,
    backupCount=1024)
    file_handler.setLevel( app.config['log_level'] )
    formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName)s | %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel( app.config['log_level'])
    app.logger.addHandler(file_handler)


