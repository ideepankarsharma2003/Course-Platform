import helpers
from django.db import models
from cloudinary.models import CloudinaryField


helpers.cloudinary_init()
# Create your models here.
"""
- Courses:
    - Title
    - Description
    - Thumbnail/Image
    - Access:
        - Anyone
        - Email Required
        - Purchase required
        - User required (n/a)
    - Status
        - Published
        - Coming Soon
        - Draft
"""

class PublishStatus(models.TextChoices):
    PUBLISHED= "pub", "Published"
    COMING_SOON= "soon", "Coming Soon"
    DRAFT= "draft", "Draft"

class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"


def handle_upload(instance, filename):
    return f"{filename}"

class Course(models.Model):
    title= models.CharField(max_length=20)
    description= models.TextField(blank=True, null=True)
    # image= models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image= CloudinaryField("image", null=True)
    access= models.CharField(
        max_length=10,
        choices=AccessRequirement.choices,
        default=AccessRequirement.ANYONE
    )
    status= models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
    )

    @property
    def is_published(self):
        return self.status== PublishStatus.PUBLISHED
    
    @property
    def image_admin_url(self):
        if not self.image:
            return ""
        
        image_options= {
            "width":200,
        }
        url= self.image.build_url(**image_options)
        return url
    
    
    def get_image_thumbnail(self, as_html=False, width=500):
        if not self.image:
            return ""
        
        image_options= {
            "width":width,
        }
        if as_html:
            #  CloudinaryImage(cloudinary_id).image(**image_options)
            return self.image.image(**image_options)
        #  CloudinaryImage(cloudinary_id).build_url(**image_options)
        url= self.image.build_url(**image_options)
        return url
    
    def get_image_detail(self, as_html=False, width=750):
        if not self.image:
            return ""
        
        image_options= {
            "width":width,
        }
        if as_html:
            #  CloudinaryImage(cloudinary_id).image(**image_options)
            return self.image.image(**image_options)
        #  CloudinaryImage(cloudinary_id).build_url(**image_options)
        url= self.image.build_url(**image_options)
        return url




"""
- Lessons
    - Title
    - Description
    - Video
    - Status Published, Coming Soon, Draft
"""


# Lesson.objects.all() # lesson queryset -> all rows
# Lesson.objects.first()
# course_obj = Course.objects.first()
# course_qs = Course.objects.filter(id=course_obj.id)
# Lesson.objects.filter(course__id=course_obj.id)
# course_obj.lesson_set.all()
# lesson_obj = Lesson.objects.first()
# ne_course_obj = lesson_obj.course
# ne_course_lessons = ne_course_obj.lesson_set.all()
# lesson_obj.course_id
# course_obj.lesson_set.all().order_by("-title")


class Lesson(models.Model):
    course= models.ForeignKey(Course, on_delete=models.CASCADE)
    title= models.CharField(max_length=20)
    description= models.TextField(blank=True, null=True)
