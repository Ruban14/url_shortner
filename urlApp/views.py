from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
import pyshorteners as sh
import json
from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework import response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


def generate_url(request):
    long_url = request.POST.get("url", False)
    short_url = check_short_link(long_url)

    print(short_url)
    return render(request, 'output.html', {"short_url": short_url})

def index(request):
    return render(request, 'index.html')

def check_short_link(long_url):
    short_url = ''
    # reading to sample.json
    with open('sample.json', 'r') as openfile:
        json_object = json.load(openfile)
        print(json_object)

    # get the long url from user
    # ==========================

    # checking for already exists in json file

    # if exists return the created one
    if long_url in json_object:
        short_url = json_object[long_url]
        print('already present')
        
    # if not present create a new one and append to the file and then return the short url
    else:
        print('created new one')
        # after checking with json if there is no link already in json create a short url
        s = sh.Shortener()
        short_url = s.tinyurl.short(long_url)

        # after creating the url append to the file
        json_object[long_url] = short_url
        with open("sample.json", "w") as outfile:
            json.dump(json_object, outfile)
    return short_url


@api_view(['POST'])
@permission_classes((AllowAny,))
def serve_shorten_url(request):
    short_url = check_short_link(request.data['url'])
    return Response(data=short_url, status=status.HTTP_200_OK)
