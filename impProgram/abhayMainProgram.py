print("working")
class Install_req:
    def install(self):
        import os
        os.system('cmd')

# print(1)
class HM_Calc:
    def calc(self):
        try:
            while (1):
                print("calculator peramiterize")

                def cal(num1, opr, num2):
                    print("Ques: ", num1, opr, num2)

                num1 = int(input("enter your first number: "))
                opr = input("enter your operation b/w= ( + , - , * , / ) for exit=0:")
                num2 = int(input("enter your second number: "))
                if opr and num1 == 0:
                    exit()
                if opr == '+':
                    print("Result: ", num1 + num2)
                elif opr == '-':
                    print("Result: ", num1 - num2)
                elif opr == '*':
                    print("Result: ", num1 * num2)
                elif opr == '/':
                    print("Result: ", num1 / num2)
                else:
                    print("Invaild")
                cal(num1, opr, num2)
        except ValueError:
            print("##please enter int type value! next time")
        except KeyboardInterrupt:
            print("program is finish. Thanks you.")
# print(2)
class Discount:
    def dis(self):
        try:
            # ------------------give user a discount program--------------
            price = int(input("enter price of product"))
            discount = int(input("enter how much you won't discount"))
            a = price * discount / 100
            tp = price - a
            print("your discount is:", a)
            print("after discount price is:", tp)
        except ValueError:
            print("##please enter int type value! next time")
        except KeyboardInterrupt:
            print("program is finish. Thanks you.")
# print(3)
class Phoneinfo:
    def getInfo(self):
        while True:
            try:
                from phonenumbers import timezone, geocoder, carrier, parse
                print("__________________________________________________")
                print("Example: 917856421458")
                number = input("[+]Enter your num with country code +__:")
                phone = parse("+" + number)
                # for know timezone of victem
                time = timezone.time_zones_for_number(phone)
                # known ISP
                simdetails = carrier.name_for_number(phone, "en")
                # known country by geo location
                country = geocoder.description_for_number(phone, "en")
                print("Time:>",time)
                print("Phone:>",phone)
                print("Sim details:>",simdetails)
                print("Country:>",country)
                # for longitude and latitude
                from opencage.geocoder import OpenCageGeocode
                geocoder = OpenCageGeocode('1a0e423f30a943f1be940684fe4c0d56')
                query = str(country)
                result = geocoder.geocode(query)
                latitude = result[0]['geometry']['lat']
                longitude = result[0]['geometry']['lng']
                print(f"Latitude:>{latitude}\nLongitude:>{longitude}")
                # ===========================================================================
                # for get .html page for gui map location
                # import folium
                # mymap=folium.Map(Location=[latitude,longitude],zoom_start=9)
                # folium.Marker([latitude,longitude],popup=country).add_to(mymap)
                # # save map in html file
                # mymap.save('victimLocation.html')
                # ====================================================================
            except ValueError:
                print("##please enter int type value! next time")
            except KeyboardInterrupt:
                print("program is finish. Thanks you.")
            except None:
                pass
# print(4)
class Encode_md5:
    def E_md5(self):
        while True:
            try:
                import hashlib
                text = input("[+]Enter your text you want to Convert md5hash:> ")
                hash = hashlib.md5(text.encode())
                md5_hash = hash.hexdigest()
                print("Your md5 hash is:> ", md5_hash)
            except:
                print("please get some help!!")
# print(5)
class Decode_md5():
    def Dcode(self):
        pass
class N_speed:
    def InetSpeed(self):
        # Internet speed test program
        # pip install speedtest-cli
        import speedtest
        test = speedtest.Speedtest()
        print("Loading server List......")
        test.get_servers()  # get list of servers
        print("Choosing best server........")
        print("Please wait it take some Time..........")
        best = test.get_best_server()  # choose best server
        print(f"found Host: {best['host']} \nLocated in: {best['country']}")
        print("Downloading speed test.....")
        download_result = test.download()
        print(
            f"Ur Downloading speed:{download_result / 1024 / 1024 :.2f} mbps")  # /1024=for kbps, /1024 /1024=for mbps, :.2f=for only 2 float number
        print("Upload speed test........")
        upload_result = test.download()
        print(f"Ur Upload speed:{upload_result / 1024 / 1024 :.2f} mbps")
        print("ping speed test......")
        ping = test.results.ping
        print(f"Ping Speed: {download_result:.2f} ms")
# print(8)
class LinkImg:
    def link_img(self):
        import qrcode
        link=input("[+]enter your link you want to convert:> ")
        img=qrcode.make(link)
        img.save("qrcode.jpg")
        print("Your img was create and store in folder please check.")
# print(9)
# ----------------------------------------text to voice------------------------------------
class TextToVoice:
    def T_V(self):
        while(1):
            try:
                from gtts import gTTS
                import os
                # forFile=open("text.txt","r")
                # forFileText=forFile.read().replace("\n"," ")
                myText = input("[+]enter your text: ")
                language = 'en-in'
                output = gTTS(text=myText, lang=language, slow=False)
                output.save("output.mp3")
                os.system("start output.mp3")
            except:
                print("sorry for your interption can you say it again")

# ================================Web Scraping===========================================
class webInfo:
        def webscrap(self):
                try:
                    while True:
                        import requests
                        from bs4 import BeautifulSoup
                        url=input("enter your url:>")
                        print("""
                        1 ->website all anchors tag.
                        2 ->whole website html format.
                        3 ->Get all paragraph and title of website.
                        """)
                        info=int(input("[+]Enter what you want to geather:> "))
                        r = requests.get(url)
                        htmlContent = r.content
                        soup = BeautifulSoup(htmlContent, 'html.parser')
                        anchors = soup.find_all('a')
                        all_links = set()
                        if info==1:
                            print("Please wait a sec..............")
                            # Get all the links on the page:
                            for link in anchors:
                                if (link.get('href') != '#'):
                                    linkText = url + link.get('href')
                                    all_links.add(link)
                                    print(linkText)

                            navbarSupportedContent = soup.find(id='navbarSupportedContent')
                        elif info == 2:
                            print(soup)
                        elif info == 3:
                            # get title of website
                            title = soup.title
                            # Get all the paragraphs from the page
                            para = soup.find_all('p')
                            print(para)
                            print(title)

                except:
                    print("got some error")

#-----------------------------------------------Face Dectection--------------------------------------------------------
class FaceDect:
    def faceDect(self):
        import cv2
        import pathlib
        cascade_path=pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
        # print(cascade_path)
        clf=cv2.CascadeClassifier(str(cascade_path))
        camera=cv2.VideoCapture(0)
        # videocapture=cv2.VideoCapture("file.mp4")
        while True:
            _, frame=camera.read()
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=clf.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30,30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            for (x,y,width,height) in faces:
                cv2.rectangle(frame,(x,y),(x+width,y+height),(255,255,0),2)

            cv2.imshow("Faces",frame)
            if cv2.waitKey(1) == ord("q"):
                break
        camera.release()
        cv2.destroyAllWindows()
#--------------------------------------------Voice to Text-----------------------------------------
class VoiceText:
    def X(self):
        import speech_recognition
        import pyttsx3
        import pyaudio

        while True:
            recognizer=speech_recognition.Recognizer()
            try:
                with speech_recognition.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(mic,duration=0.1)
                    print("Speak.....!")

                    audio=recognizer.listen(mic)
                    print("Convert voice to text.......")
                    text=recognizer.recognize_google(audio)
                    print()
                    text=text.lower()
                    print(f"Recognized:> {text}")
            except speech_recognition.UnknownValueError:
                recognizer=speech_recognition.Recognizer()
                continue
            except TypeError:
                print("type error")
            except:
                print("program is finished")
VT=VoiceText()
TV=TextToVoice()
toolpad=HM_Calc()
disc=Discount()
pInfo=Phoneinfo()
E_hash=Encode_md5()
inetspeed=N_speed()
link_img=LinkImg()
webScrap=webInfo()
FaceDect=FaceDect()      #through cmd
print("finish program")
