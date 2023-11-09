from django.http import HttpResponse, HttpRequest
from django.template import loader
from emailserver.models import Facility, Tour

def index(request):
    html = "<html><body>Hello, World.</body></html>"
    return HttpResponse(html)

def monitor_tour(request: HttpRequest):
    facilities = Facility.objects.all().order_by('name')
    template = loader.get_template("monitor_tour.html")
    base_page = template.render({ 'facilities': facilities }, request)
    
    if (request.method == 'POST'):
        facility = None
        if 'facility' in request.POST:
            print(f"facility = {request.POST['facility']}")
            facility_id = request.POST['facility']
            facility = Facility.objects.get(pk=facility_id)

        if facility is None:
            return HttpResponse(base_page)
        
        print(f"facility name = {facility.name}")
        tours = facility.tour_set.all()
        
        tour = None
        if 'tour' in request.POST:
            tour_id = request.POST['tour']
            tour = Tour.objects.get(pk=tour_id)
        
        start_date = request.POST.get('start-date')

        end_date = request.POST.get('end-date')

        return HttpResponse(template.render({ 'facilities': facilities, 'selected_facility': facility, 'tours': tours, 'selected_tour': tour, 'start_date': start_date, 'end_date': end_date }, request))


    return HttpResponse(base_page)
