from django.contrib import admin

from .models import Choice
# Register your models here.
from .models import Question

admin.site.register(Question)
admin.site.register(Choice)
