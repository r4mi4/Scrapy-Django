from django.shortcuts import render
from scp.scp.spiders.news import IrnaNewsSpider, FillFormSpider
from scp.scp.run_spider import run_spider
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required(login_url='/')
def start_crawl(request):
    result = run_spider(IrnaNewsSpider)
    context = {
        'data': result
    }
    return render(request, 'posts/search.html', context)


@staff_member_required(login_url='/')
def filladminform(request):
    url = request.GET.get('url_news')
    result = run_spider(FillFormSpider, url)
    return JsonResponse(result, safe=False)
