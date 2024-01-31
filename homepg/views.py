from django.shortcuts import render,get_object_or_404
from homepg.models import Noti, Seniorno, Image, Alumni, Homepage_intro
from homepg.models import Syllabus, Previous_Question, Admission, Placement, Resume
from homepg.models import Fee, Blog, Scholarship, Material, Gallery, About
def index(request):
    all_noti=Noti.objects.all()
    all_seniorno = Seniorno.objects.all()
    image_instance = Image.objects.all()
    thuziak_var = Homepage_intro.objects.first()
    context={
        'noti_html':all_noti,
        'seniorno_html':all_seniorno,
        'photo_html':image_instance,
        'homepg_thuziak':thuziak_var,
    }
    return render(request,'homepg/index.html',context)

def blog(request):
    blog_var = Blog.objects.all()
    return render(request, 'homepg/Blog.html', {'blog_html': blog_var})

def syllabus(request):
    syllabus_var =Syllabus.objects.all()
    return render(request, 'homepg/Syllabus.html', {'all_syllabus': syllabus_var})

def question(request):
    qp_var=Previous_Question.objects.all()
    return render(request,'homepg/questionpaper.html',{'all_qp':qp_var})
def material(request):
    material_var=Material.objects.all()
    return render(request,'homepg/material.html',{'all_material':material_var})
def admission(request):
    admission_var=Admission.objects.all()
    return render(request,'homepg/admission.html',{'all_admission':admission_var})
def fee(request):
    fee_var=Fee.objects.all()
    return render(request,'homepg/fee.html',{'all_fee':fee_var})
def scho(request):
    scho_var=Scholarship.objects.all()
    return render(request,'homepg/scho.html',{'all_scho':scho_var})

def alumni(request):
    thuziak_var=Alumni.objects.all()
    return render(request,'homepg/alumni.html',{'thuziak_html':thuziak_var})
def gallery(request):
    images = Gallery.objects.all()
    return render(request,'homepg/gallery.html',{'images':images})
def about(request):
    const_var = About.objects.all()
    return render(request, 'homepg/about.html', {'all_constitution': const_var})


def placement(request):
    placement=Placement.objects.all()
    resume_var=Resume.objects.all()
    context={
                'all_placement':placement,
                'all_resume':resume_var

            }
    return render(request,'homepg/placement.html',context)
# Create your views here.
