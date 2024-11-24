from django.contrib import admin
from django.utils.html import format_html
from cloudinary import CloudinaryImage

# Register your models here.
from.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin ):
    list_display= ["title", "status", "access"]
    list_filter= ["status", "access"]
    fields= [
        "title",
        "description",
        "status",
        "image",
        "access",
        "display_image", # not a natural field
    ]
    readonly_fields= ['display_image']


    def display_image(self, 
                      obj:Course,
                      *args, 
                      **kwargs):
        url= obj.image_admin_url
        html= f'<img src={url}>'
        return format_html(html)
    
    display_image.short_description= "Current Image"

# admin.site.register(Course, CourseAdmin) # same as the decorator