from django.db import models
from  mongoengine import Document, EmbeddedDocument, fields
# from django.contrib.auth import get_user_model
# from django.db.models.loading import cache as model_cache
# if not model_cache.loaded:
#     model_cache.get_models()

# class Projdescription(EmbeddedDocument):
#     name = fields.StringField(max_length=400)
#
#     def __str__(self):
#         return self.name

# class ProjectManager(models.Manager):
#     pass


# Create your models here.
class Project(models.Model):
    proj_id = models.IntegerField()
    proj_name = models.CharField(max_length=200)
    # file=fields.FileField()
    # proj_desc = fields.EmbeddedDocumentField(Projdescription)
    comments = models.CharField(max_length=400)


    # objects = ProjectManager()

    def __str__(self):
        return self.proj_name

# class Designation(EmbeddedDocument):
#     name = fields.StringField(required=True, max_length=250)
#
#     def __str__(self):
#         return self.name


# class Employee(Document):
#     name = fields.StringField(required=True, max_length=250)
#     username = fields.StringField(max_length=250)
#     email = fields.EmailField()
#     emp_id = fields.IntField()
#     designation = fields.EmbeddedDocumentField(Designation)
#     file = fields.FileField()
#
#     def __str__(self):
#         return self.name
#
#     # meta = {
#     #     'abstract': True
#     # }
#
#
# class Department(Document):
#     name = fields.StringField(required=True, max_length=250)
#     file = fields.FileField()
#
#     def __str__(self):
#         return self.name
#
#     # meta = {
#     #     'abstract': True
#     # }
