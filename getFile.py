import requests
import json
import os
import playsound
from gtts import gTTS


#pip3 install request
#sudo apt-get install espeak
# pip3 install gTTS
#sudo apt-get -y install mpg321
# pip3 install playsound
#sudo apt-get install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools
#speaker-test -t wav  //test rp speakers



def get_all_stations_info():
    url = "https://robotdb-a3c9.restdb.io/rest/routeinfo"

    headers = {
        'content-type': "application/json",
        'x-apikey': "5e73949509c313436a6a05ed",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)
    return response.json()

def get_station_by_barcode():
    #here will be the code to return the barcode which tell us what station we in
    return 0,"child_content"

def play_station(station):
    # The text that you want to convert to audio
    mytext = res[station[0]][station[1]]

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")

    # Playing the converted file
    # os.system('start welcome.mp3')

    playsound.playsound("welcome.mp3")



res=get_all_stations_info()
print(res)
station=get_station_by_barcode()
print(station)
play_station(station)




#######################################################















