from django.shortcuts import render
import urllib.request as rq
import json
# Create your views here.
def index(request):
    content = {}
    url = "http://api.icndb.com/jokes/random?firstName=Rajnikanth&amp&lastName="
    if request.method == 'GET':
        with rq.urlopen(url) as res:
            joke_json = json.loads(res.read())
            joke = joke_json['value']['joke']
            content = {"joke": joke}
        return render(request, 'search/index.html', content)


