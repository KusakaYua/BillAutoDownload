from django import forms
from .models import BillingSite

class BillingSiteForm(forms.ModelForm):
    """請求書サイト追加フォーム"""
    class Meta:
        model = BillingSite
        fields = ['site_name', 'login_url', 'username', 'password', 'download_frequency']
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例: 電力会社'}),
            'login_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com/login'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ログインユーザー名'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'download_frequency': forms.Select(
                attrs={'class': 'form-select'},
                choices=[
                    ('monthly', '月1回'),
                    ('weekly', '週1回'),
                    ('daily', '毎日'),
                ]
            )
        }
        labels = {
            'site_name': '請求書サイト名',
            'login_url': 'ログインURL',
            'username': 'ユーザー名',
            'password': 'パスワード',
            'download_frequency': 'ダウンロード頻度',
        }

    def clean_password(self):
        """パスワードの簡易的な検証"""
        password = self.cleaned_data.get('password')
        if len(password) < 4:
            raise forms.ValidationError('パスワードは4文字以上である必要があります。')
        return password
