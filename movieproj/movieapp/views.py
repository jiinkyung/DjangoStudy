from django.shortcuts import render
import requests
import json
from my_id import my_id


def home(request):
    url = 'https://api.themoviedb.org/3/trending/movie/week?api_key='+my_id
    response = requests.get(url)
    resdata = response.text
    obj = json.loads(resdata)
    obj = obj['results']

    return render(request, 'index.html', {'obj':obj})

def detail(request, movie_id):
    # https://api.themoviedb.org/3/movie/300?api_key=f2a8424e40bf3e57b995e2c750a52465&language=en-US
    url = 'https://api.themoviedb.org/3/movie/' + movie_id +'?api_key=' + my_id
  
    response = requests.get(url)
    resdata = response.text
    return render(request, 'detail.html', {"resdata":resdata})
