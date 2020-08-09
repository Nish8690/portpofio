from django.db import models
import requests
import json

# res = requests.get('https://api.covid19api.com/summary')
#
# r_dict = res.text[:]
# text_json= json.loads(r_dict)
#
# for counry in text_json['Countries']:
#     print('Date : ',counry['Date'],'\t',
#           'Contry_Name : ',counry['Country'],'\t',
#           'TotalConfirmed : ',counry['TotalConfirmed'],'\t',
#           'NewConfirmed : ',counry['NewConfirmed'],'\t',
#           'NewDeaths : ',counry['NewDeaths'],'\t',
#           'TotalDeath : ',counry['TotalDeaths'],'\t',
#           'NewRecovered : ',counry['NewRecovered'],'\t',
#           'TotalRecovered : ',counry['TotalRecovered'])
#
#
# # Create your models here.
# class Covid(models.Model):
#     Date : counry['Date']
#     Contry_Name :counry['Country']
#     TotalConfirmed :counry['TotalConfirmed']
#     NewConfirmed :counry['NewConfirmed']
#     NewDeaths :counry['NewDeaths']
#     TotalDeath :counry['TotalDeaths']
#     NewRecovered :counry['NewRecovered']
#     TotalRecovered :counry['TotalRecovered']
#
#
#     Contry_Name = models.CharField(max_length=200)
#     TotalConfirmed = models.CharField(max_length=200)
#     NewConfirmed = models.CharField(max_length=50,default= "")
#     NewDeaths = models.CharField(max_length=300)
#     proj_image=models.ImageField(default="")
#     TotalDeath=models.FileField(default=None,upload_to='pf/images')
#     NewRecovered = models.DateField(max_length=200,default=None)
#     TotalRecovered = models.URLField(default=None, max_length=200)
#
#
#
#     # objects = ProjectManager()
#
#     def __str__(self):
#         return self.proj_name
