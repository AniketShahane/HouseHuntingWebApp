from django.contrib import admin
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('is_mvp',)
    list_perpage = 25

    def get_ordering(self, request):
        return ['id']

admin.site.register(Realtor, RealtorAdmin)
