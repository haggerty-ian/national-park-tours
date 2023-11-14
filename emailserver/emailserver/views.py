from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.core.exceptions import ValidationError
from emailserver.models import Facility, Tour, MonitorWindow

def index(request):
    html = "<html><body>Hello, World.</body></html>"
    return HttpResponse(html)

def monitor_tour(request: HttpRequest):
    facilities = Facility.objects.all().order_by('name')
    template = loader.get_template("monitor_tour.html")
    base_page = template.render({ 'facilities': facilities }, request)
    
    if (request.method == 'POST'):
        facility = get_facility(request)
        
        if facility is None:
            return HttpResponse(base_page)
        
        print(f"facility name = {facility.name}")
        tours = facility.tour_set.all()
        
        tour = get_tour(request)

        return HttpResponse(template.render({ 'facilities': facilities, 'selected_facility': facility, 'tours': tours, 'selected_tour': tour }, request))

    return HttpResponse(base_page)

def submit_monitor(request: HttpRequest):
    template = loader.get_template("submit_monitor.html")

    facility = get_facility(request)
    tour = get_tour(request)

    start_date = request.POST.get('start-date')
    end_date = request.POST.get('end-date')

    if start_date is not None and len(start_date) == 0:
        start_date = None
    
    if end_date is not None and len(end_date) == 0:
        end_date = None
    
    email = request.POST.get('email')

    print(f'start_date = {start_date}')
    print(f'end_date = {end_date}')

    if not facility or not tour or not email:
        result_message = "failed to submit all fields"
    else:
        try:
            monitor_window = MonitorWindow(email=email, start_date=start_date, end_date=end_date, facility=facility, tour=tour)
            monitor_window.save()
            result_message = 'successfully saved monitor window'
        except ValidationError as e:
            result_message = e.message

    return HttpResponse(template.render({ 'result_message': result_message }))

def get_tour(request: HttpRequest):
    tour = request.POST.get('tour')
    if tour is not None and tour.isdecimal():
        tour_id = request.POST['tour']
        tour = Tour.objects.get(pk=tour_id)
    else:
        tour = None

    return tour
        
    
def get_facility(request: HttpRequest):
    facility = request.POST.get('facility')
    if facility is not None and facility.isdecimal():
        print(f"facility = {request.POST['facility']}")
        facility_id = request.POST['facility']
        facility = Facility.objects.get(pk=facility_id)
    else:
        facility = None

    return facility