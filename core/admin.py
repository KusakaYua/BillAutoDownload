from django.contrib import admin
from .models import BillingSite, DownloadedBill

@admin.register(BillingSite)
class BillingSiteAdmin(admin.ModelAdmin):
    """請求書サイト設定の管理画面"""
    list_display = ('user', 'site_name', 'login_url', 'download_frequency', 'last_downloaded')
    list_filter = ('user', 'download_frequency')
    search_fields = ('site_name', 'user__username')

@admin.register(DownloadedBill)
class DownloadedBillAdmin(admin.ModelAdmin):
    """ダウンロードした請求書の管理画面"""
    list_display = ('site', 'file_name', 'download_date', 'bill_date')
    list_filter = ('site__user', 'download_date')
    search_fields = ('file_name', 'site__site_name')
