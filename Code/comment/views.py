from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Comment

@login_required
@require_POST
def create_comment(request):
    pass
# Create your views here.
