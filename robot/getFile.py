import requests
import json
import os
import playsound
from gtts import gTTS


# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
    


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
    return (0,"child_content")




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

    #playsound.playsound("welcome.mp3")
    os.system("mpg321 -q welcome.mp3")




    
def barcode_scan():
        # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
        help="path to output CSV file containing barcodes")
    args = vars(ap.parse_args())
    
    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    # vs = VideoStream(src=0).start()
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)
    
    # open the output CSV file for writing and initialize the set of
    # barcodes found thus far
    csv = open(args["output"], "w")
    found = set()
    
    # loop over the frames from the video stream
    while True:
        # grab the frame from the threaded video stream and resize it to
        # have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        # find the barcodes in the frame and decode each of the barcodes
        barcodes = pyzbar.decode(frame)
        
    # loop over the detected barcodes
        for barcode in barcodes:
            # extract the bounding box location of the barcode and draw
            # the bounding box surrounding the barcode on the image
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # the barcode data is a bytes object so if we want to draw it
            # on our output image we need to convert it to a string first
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            # draw the barcode data and barcode type on the image
            text = "{} ({})".format(barcodeData, barcodeType)
            ourBarcode = barcodeData
            cv2.putText(frame, text, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
            # if the barcode text is currently not in our CSV file, write
            # the timestamp + barcode to disk and update the set
            if barcodeData not in found:
                csv.write("{},{}\n".format(datetime.datetime.now(),
                    barcodeData))
                csv.close()
                cv2.destroyAllWindows()
                vs.stop()
                return barcodeData
            
                csv.flush()
                found.add(barcodeData)

#     print(ourBarcode)
    # show the output frame
        cv2.imshow("Barcode Scanner", frame)
        key = cv2.waitKey(1) & 0xFF
 
    # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    # close the output CSV file do a bit of cleanup
    print("[INFO] cleaning up...")
    csv.close()
    cv2.destroyAllWindows()
    vs.stop()
    






# main
res=get_all_stations_info()
print(res)
# print()
# station=get_station_by_barcode()
#station=eval(barcode_scan())
#print(station)
#play_station(station)




#######################################################















