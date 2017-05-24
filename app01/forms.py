#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:max
from django import forms
from app01 import models
import re

from django.core.exceptions import ValidationError

class BookForm(forms.Form):
    title = forms.CharField(max_length=10)
    # publisher_id = forms.IntegerField(widget=forms.Select)
    publication_date = forms.DateField()

class BookModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        # fields = ('title','publication_date')
        exclude = {}

        widgets = {
            'title':forms.TextInput(attrs={'class':"form-control"}),
        }


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class PublishForm(forms.Form):

    user_type_choice = (
        (0, u'普通用户'),
        (1, u'高级用户'),
    )

    user_type = forms.IntegerField(widget=forms.widgets.Select(choices=user_type_choice,
                                                                  attrs={'class': "form-control"}))

    title = forms.CharField(max_length=20,
                            min_length=5,
                            error_messages={'required': u'标题不能为空',
                                            'min_length': u'标题最少为5个字符',
                                            'max_length': u'标题最多为20个字符'},
                            widget=forms.TextInput(attrs={'class': "form-control",
                                                          'placeholder': u'标题5-20个字符'}))

    memo = forms.CharField(required=False,
                           max_length=256,
                           widget=forms.widgets.Textarea(attrs={'class': "form-control no-radius", 'placeholder': u'详细描述', 'rows': 3}))

    phone = forms.CharField(validators=[mobile_validate, ],
                            error_messages={'required': u'手机不能为空'},
                            widget=forms.TextInput(attrs={'class': "form-control",
                                                          'placeholder': u'手机号码'}))

    email = forms.EmailField(required=False,
                            error_messages={'required': u'邮箱不能为空','invalid': u'邮箱格式错误'},
                            widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': u'邮箱'}))
