from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from NewsArticle.models import NewsArticle
import requests
from django.contrib.auth.decorators import login_required

User = get_user_model()


@login_required(login_url='/login')
def free_news(request):
    news_list = NewsArticle.objects.filter(premium_content=False)
    return render(request, 'dashboard/free_news.html', context={"news_list": news_list})


@login_required(login_url='/login')
def premium_news(request):
    news_list = []
    if request.user.premium_status == 2:
        news_list = NewsArticle.objects.filter(premium_content=True)
    return render(request, 'dashboard/premium_news.html', context={"news_list": news_list})


@login_required(login_url='/login')
def read_more(request, pk):
    news = NewsArticle.objects.get(id=pk)
    return render(request, 'dashboard/detailed_view.html', context={"news": news})


def payment_webhook(request):
    if request.method != 'GET':
        return

    status = request.GET.get('status')
    uuid = request.GET.get('uuid')
    headers = {'Authorization': "Bearer " + settings.API_KEY}
    response = requests.get('https://www.blockonomics.co/api/merchant_order/%s' % uuid, headers=headers)
    data = response.json()
    user = User.objects.get(email=data.get('data').get('emailid'))
    user.premium_status = int(status)
    user.save()
    return HttpResponse(200)


@login_required(login_url='/login')
def cancel_payment(request, pk):
    user = User.objects.get(id=pk)
    user.premium_status = -1
    user.save()
    return redirect('NewsArticle:premium_news')
