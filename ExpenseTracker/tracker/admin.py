from django.contrib import admin
from tracker.models import *
admin.site.site_header = 'Expense Tracker'
admin.site.index_title = 'Expense Tracker Administration'
admin.site.site_title = 'Expense Tracker Admin'
admin.site.register(CurrentBalance)
class HistoryTrackerAdmin(admin.ModelAdmin):
    list_display = ['amount','current_balance', 'expense_type', 'description','created_at']
admin.site.register(HistoryTracker,HistoryTrackerAdmin)
    
# Register your models here.
