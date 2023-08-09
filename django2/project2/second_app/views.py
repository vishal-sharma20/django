from django.shortcuts import render
from django.http import HttpResponse

def main(req):
    return render(req, 'home.html')


def day(request, day):
    dic = {
        "Monday" : "सोमवार",
        "Tuesday" : "मंगलवार",
        "Wednesday" : "बुधवार",
        "Thurday" : "गुरुवार",
        "Friday" : "शुक्रवार",
        "Saturday" : "शनिवार",
        "Sunday" : "रविवार"
    }
    context = {
    'english': day,
    'hindi': dic[day],
    }
    return render(request, "mon.html", context)
    
