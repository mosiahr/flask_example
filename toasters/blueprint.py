#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template

from models import Toaster, Tag





toasters = Blueprint('toasters', import_name=__name__, template_folder='templates')


#http://localhost/toasters/
@toasters.route('/')
def index():
    toasters = Toaster.query.all()
    return render_template('toasters/index.html', toasters=toasters)


#http://localhost/toasters/id
@toasters.route('/<id>')
def toaster_detail(id):
    toaster = Toaster.query.get(id)
    tags = toaster.tags
    return render_template('toasters/toaster_detail.html', toaster=toaster, tags=tags)


#http://localhost/toasters/tag/slug
@toasters.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    toasters = tag.toasters.all()
    return render_template('toasters/tag_detail.html', tag=tag, toasters=toasters)