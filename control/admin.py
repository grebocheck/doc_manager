from django.contrib import admin
from .models import Status, RequestDocument, RequestEvent

# Register your models here.

admin.site.register([Status, RequestDocument, RequestEvent])
