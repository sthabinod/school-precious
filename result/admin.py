from django.contrib import admin

from result.models import Result

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass