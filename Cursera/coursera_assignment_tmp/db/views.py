from django.shortcuts import render
from django.http import HttpResponse
from .query import *
from django.db.models import Q, Count, Avg
from .models import User, Blog, Topic

# Create your views here.
def test_create(request):
    # unsubscribe_u2_from_blogs()
    # unsubscribe_u2_from_blogs()
    # get_topic_created_grated()
    # get_user_with_limit()
    get_topic_count()
    return HttpResponse(content='')