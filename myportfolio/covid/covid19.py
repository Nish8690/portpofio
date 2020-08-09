import requests
import json

# res = requests.get('https://api.covid19api.com/summary')
res = requests.get('https://www.trackcorona.live/api/countries')

r_dict = res.text[:]
text_json= json.loads(r_dict)
print(text_json)


list=[]

for country in text_json['data']:
    print(country)
#     for key, value in country.items():
#         temp=[key,value]
#         list.append(temp)
# print(list[0][1])
#
# res = json.loads(glob,unicode="UTF-8")
#
# for glob in text_json['Global']:
#     # res = json.loads(glob)
# #     print(res)
#     print(glob)
#     for key,value in glob.keys():
#         temp=[key,value]

        # list.append(key)
# print(list)


    # print(country)
#     print('Date : ',counry['Date'],'\t',
#           'Contry Name : ',counry['Country'],'\t',
#           'TotalConfirmed : ',counry['TotalConfirmed'],'\t',
#           'NewConfirmed : ',counry['NewConfirmed'],'\t',
#           'NewDeaths : ',counry['NewDeaths'],'\t',
#           'TotalDeath : ',counry['TotalDeaths'],'\t',
#           'NewRecovered : ',counry['NewRecovered'],'\t',
#           'TotalRecovered : ',counry['TotalRecovered'])
