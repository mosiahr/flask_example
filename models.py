
from app import db
from datetime import datetime
import re

from transliterate import translit, get_available_language_codes


def slugify(text, delim=u'-'):
    pattern = r'[^\w+]'  # любой символ кроме любая цифра или буква
    return re.sub(pattern, delim, translit(str(text).lower(), 'ru', reversed=True))


# ManyToMany
toaster_tags = db.Table('toaster_tags',
                     db.Column('toaster_id', db.Integer, db.ForeignKey('toaster.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                )


class Toaster(db.Model):
    __tablename__ = 'toaster'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    address = db.Column(db.String(140))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    site = db.Column(db.String(120))
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    tags = db.relationship('Tag', secondary=toaster_tags, backref=db.backref('toasters', lazy='dynamic'))


    def __repr__(self):
        return '<Toaster id: {}, Name: {}>'.format(self.id, self.name)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return self.name