from django.db import models
from django.contrib.auth.models import User

class BillingSite(models.Model):
    """請求書サイトの設定モデル"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100)
    login_url = models.URLField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    download_frequency = models.CharField(max_length=50, default='monthly')
    last_downloaded = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.site_name}"

class DownloadedBill(models.Model):
    """ダウンロードした請求書の情報"""
    site = models.ForeignKey(BillingSite, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    download_date = models.DateTimeField(auto_now_add=True)
    file_path = models.FilePathField()
    bill_date = models.DateField()

    def __str__(self):
        return f"{self.site.site_name} - {self.file_name}"
