from django.http import HttpResponse, HttpRequest
from django.template import loader
from emailserver.models import Facility, Tour

def index(request):
    html = "<html><body>Hello, World.</body></html>"
    return HttpResponse(html)

def choose_facility(request: HttpRequest):
    print(request)
    template = loader.get_template("choose_facility.html")
    
    facilities = Facility.objects.all().order_by('name')
    if (request.method == 'POST'):
        print(f"facility = {request.POST['facility']}")
        facility_index = request.POST['facility']
        facilty = Facility.objects.get(pk=facility_index)
        tours = facilty.tour_set.all()
        print(f'tours len = {len(tours)}')
        print(f"facility name = {facilty.name}")
        return HttpResponse(template.render({ 'facilities': facilities, 'selected_facility': facilty, 'tours': tours }, request))


    return HttpResponse(template.render({ 'facilities': facilities }, request))
