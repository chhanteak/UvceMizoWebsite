from django.db import models
from ckeditor.fields import RichTextField

class Noti(models.Model):
    notify=models.CharField(max_length=500)

    def __str__(self):
        return self.notify

class Seniorno(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)

    def __str__(self):
        return self.name
class Image(models.Model):
    photo=models.FileField()

class Alumni(models.Model):

    thuziak=RichTextField(blank=True, null=True)
    name_alumni = models.CharField(max_length=700, null=True)
    desig_alumni = models.CharField(max_length=700, null=True)
    img_alumni = models.FileField(null=True)

class Homepage_intro(models.Model):
    thuziak_readmore = RichTextField(blank=True, null=True)
    homepage_thuziak=RichTextField(blank=True, null=True)

class Syllabus(models.Model):
        link=models.CharField(max_length=700)
        branch = models.CharField(max_length=50, null=True)
class Previous_Question(models.Model):
    branch=models.CharField(max_length=50)
    link2=models.CharField(max_length=700)
class Admission(models.Model):
    admission_word=RichTextField(blank=True, null=True)
    link_admission = models.CharField(max_length=700, null=True)
    notice_photo = models.FileField()
    notice_pdf = models.FileField(null=True)

class Placement(models.Model):
    placement_word=RichTextField(blank=True, null=True)

class Resume(models.Model):
    resume=models.FileField()

class Fee(models.Model):
    fee_word=RichTextField(blank=True, null=True)

class About(models.Model):
    constitution_word = RichTextField(blank=True, null=True)
    constitution_pdf = models.FileField()

class Blog(models.Model):
    thuziak_blog = RichTextField(blank=True, null=True)
    name_blog = models.CharField(max_length=700, null=True)
    year_batch = models.CharField(max_length=700, null=True)
    img_blog = models.FileField(null=True)

class Scholarship(models.Model):
    thuziak_scho= RichTextField(blank=True, null=True)

class Material(models.Model):
    link = models.CharField(max_length=700)
    branch = models.CharField(max_length=50, null=True)

class Gallery(models.Model):
    gallery_image=models.FileField(null=True)
    description = models.CharField(max_length=700, null=True)

# Create your models here.:
