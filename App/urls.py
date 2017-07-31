# coding=utf-8
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from App import actions

urlpatterns = [
    url(r'^putdata/',actions.putdata),
    # url(r'^index/',actions.index),
    url(r'^post/', actions.post),
    url(r'^submit-form$', actions.submit_form),
    url(r'^submit$', actions.submit),
]

#可以由客户端来决定返回的格式
# urlpatterns = format_suffix_patterns(urlpatterns)