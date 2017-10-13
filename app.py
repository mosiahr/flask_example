from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.model import BaseModelView


app = Flask(import_name=__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
# db.Column(db.)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

### ADMIN ###
from models import *
admin = Admin(app, name='Toasters', template_mode='bootstrap3')


class ToasterModelView(ModelView):
    column_exclude_list = ('site',)   # исключаем поле
    # excluded_list_columns = ('slug',)


admin.add_view(ToasterModelView(Toaster, db.session))
admin.add_view(ModelView(Tag, db.session))
