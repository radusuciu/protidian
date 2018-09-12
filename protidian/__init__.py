from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config.config as config

app = Flask(__name__)
app.config.from_object(config.config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register blueprints
from protidian.views import home, api_blueprint
app.register_blueprint(home)
app.register_blueprint(api_blueprint, url_prefix='/api')
