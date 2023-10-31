from django.http import HttpResponse
from django.template import loader
from emailserver.models import Facility

def index(request):
    html = "<html><body>Hello, World.</body></html>"
    return HttpResponse(html)

def choose_facility(request):
    print(request)
    template = loader.get_template("choose_facility.html")
    facilities = Facility.objects.all().order_by('name')

    return HttpResponse(template.render({ 'facilities': facilities }, request))
