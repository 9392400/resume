from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.models import resume
from django.template import loader
import pdfkit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required
def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        summary=request.POST.get("summary")
        degree=request.POST.get("degree")
        university=request.POST.get("university")
        pervious=request.POST.get("pervious")
        skills=request.POST.get("skills")
        profile=resume(name=name,email=email,phone=phone,summary=summary,degree=degree,university=university,pervious=pervious,skills=skills)
        profile.save()
    return render(request,'app/add.html')
def adds(request,id):
    form=resume.objects.get(id=id)
    template=loader.get_template('app/get.html')
    html=template.render({'form':form})
    options={
       'page-size' :'A4',
       'encoding'  :'UTF-8',
    }
    pdf=pdfkit.from_string(html,False,options=options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment;filename="resume.pdf"'
    return response

def register(request):
    if request.method=='POST':
        boy=UserCreationForm(request.POST)
        if boy.is_valid():
            boy.save()
            return redirect('login')
            
    boy=UserCreationForm()
    return render(request,'app/register.html',{'boy':boy})

