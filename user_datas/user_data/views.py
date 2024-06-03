from django.shortcuts import render, redirect
from .models import Detail


# Create your views here.
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        website = request.POST.get('website')
        email_id = request.POST.get('email')
        email_id_2 = request.POST.get('email_2')
        tel_no = request.POST.get('tel')
        address = request.POST.get('address')
        address2 = request.POST.get('address_2')
        city = request.POST.get('city')
        town = request.POST.get('town')
        country = request.POST.get('country')
        technology = request.POST.get('technology')
        technology_2 = request.POST.get('technology_2')
        technology_3 = request.POST.get('technology_3')
        contact_person = request.POST.get('contact_person')

        contact_details=Detail(name=name,website=website,email_id=email_id,email_id_2=email_id_2,tel_no=tel_no,address=address,
                                       address2=address2,city=city,town=town,country=country,technology=technology,technology_2=technology_2,
                                       technology_3=technology_3,contact_person=contact_person)
        contact_details.save()
        return redirect('thank_you')

    return render(request,'contact.html')

def data_list(request):
    all_data=Detail.objects.all()
    context={
        'all_data':all_data
    }
    return render(request,'data_list.html',context)

def filter_by_country(request):
    country = request.GET.get('country', None)
    if country:
        contacts = Detail.objects.filter(country=country)
    else:
        contacts = Detail.objects.all()
    return render(request, '/filter_by_country.html', {'contacts': contacts, 'country': country})

def thank_you_view(request):

    return render(request, 'thank.html')

def search_by_country(request):
    query = request.GET.get('q', '')
    if query:
        contacts = Detail.objects.filter(country__icontains=query)
    else:
        contacts = Detail.objects.all()
    return render(request, 'search.html', {'contacts': contacts, 'query': query})