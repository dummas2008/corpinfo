from django.shortcuts import render
import urllib
from .common import *
from django.http import JsonResponse


def company_list(request):
    searchkeys = request.GET.get('q', '')
    DOUBAN_APIKEY = "0ec6fa203a4756fd2c54ee60aed604f7"  # 这里需要填写你自己在豆瓣上申请的应用的APIKEY
    url = 'http://api.douban.com/v2/movie/search?q={}&apikey={}'.format(urllib.parse.quote(searchkeys), DOUBAN_APIKEY)  
    r = get_content(url, decoded=False)
    info=json.loads(str(r,"utf-8"))
    url = 'http://api.douban.com/v2/movie/subject/{}?apikey={}'.format(info["subjects"][0]["id"], DOUBAN_APIKEY)
    r = get_content(url, decoded=False)
    descs=json.loads(str(r,"utf-8"))
    return JsonResponse(descs)