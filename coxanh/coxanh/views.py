from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "<h1>Chào mừng bạn đến với Cỏ Xanh!</h1>"
        "Xin mời bạn làm <a href=\"/khaosat\">khảo sát</a> nhé."
    )
