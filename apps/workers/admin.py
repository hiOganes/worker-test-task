from django.contrib import admin
from apps.workers.models import Worker

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'position', 'is_active', 'hired_date')
    list_filter = ('is_active', 'position', 'hired_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_editable = ('is_active',)