from django.contrib import admin
from .models import Order, Finish, Start, Kolichestvo


class OrderAdmin(admin.ModelAdmin):
    list_display = ('otkuda', 'kuda', 'data')
    list_filter = ['data']


admin.site.register(Order, OrderAdmin)
admin.site.register(Start)
admin.site.register(Finish)
admin.site.register(Kolichestvo)
