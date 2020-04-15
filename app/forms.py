#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:42:32 2020

@author: ashleigh
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('select','Select Gender'), ('Male', 'Male'), ('Female', 'Female')])
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "e.g jdoe@example.com"})
    location = StringField('Location', validators=[DataRequired()], render_kw={"placeholder": "e.g Kingston, Jamaica"})
    biography = TextAreaField('Biography', validators=[DataRequired()])
    image = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'JPG'], 'Images only!')
    ], id='image')

