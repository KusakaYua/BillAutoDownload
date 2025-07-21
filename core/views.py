from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BillingSite, DownloadedBill
from .forms import BillingSiteForm

def home(request):
    """ホームページのビュー"""
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    """ユーザーのダッシュボード"""
    billing_sites = BillingSite.objects.filter(user=request.user)
    downloaded_bills = DownloadedBill.objects.filter(site__user=request.user).order_by('-download_date')
    
    context = {
        'billing_sites': billing_sites,
        'downloaded_bills': downloaded_bills,
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def add_billing_site(request):
    """新しい請求書サイトの追加"""
    if request.method == 'POST':
        form = BillingSiteForm(request.POST)
        if form.is_valid():
            billing_site = form.save(commit=False)
            billing_site.user = request.user
            billing_site.save()
            messages.success(request, '請求書サイトが正常に追加されました。')
            return redirect('dashboard')
        else:
            messages.error(request, '入力に誤りがあります。確認してください。')
    else:
        form = BillingSiteForm()
    
    return render(request, 'core/add_billing_site.html', {'form': form})

@login_required
def bill_management(request):
    """請求書管理ページ"""
    downloaded_bills = DownloadedBill.objects.filter(site__user=request.user)
    return render(request, 'core/bill_management.html', {'bills': downloaded_bills})
