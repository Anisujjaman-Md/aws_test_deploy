from django.contrib import admin
from test_app.models import Square


class SquareAdmin(admin.ModelAdmin):
    list_display = ['side', 'area']
    readonly_fields = ['area']
    search_fields = ['side']

admin.site.register(Square, SquareAdmin)
