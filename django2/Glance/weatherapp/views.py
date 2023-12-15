from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        request2api=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=6d986e0b43db5b835dbe59d333af2dc2').read()
        json_data=json.loads(request2api) # json data
        data_In_dict={
            "country_code":str(json_data['sys']['country_code']),
            "coordinate":str(json_data['coord']['lon'])+' '+ str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'Kelvin',
            "Pressure":str(json_data['main']['pressure']),
            "Humidity":str(json_data['main']['humidity']),
        }
    else:
        city=''
        data_In_dict={}
         
    return render(request,'weatherapp/index.html',{'data_In_dict':data_In_dict,'city':city})