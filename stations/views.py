from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

CONTENT = list()
with open("data-398-2018-08-30.csv", encoding='utf-8') as r_file:
    reader = csv.reader(r_file, delimiter=",")
    tmp = list()
    for row in reader:
        tmp.append(row)
headers = tmp.pop(0)
for row in tmp:
    tmp_dict = dict()
    for num, value in enumerate(row):
        tmp_dict[headers[num]] = value
    CONTENT.append(tmp_dict)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'stations/index.html', context)
