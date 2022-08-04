print("working")
class Install_req:
    def install(self):
        import os
        os.system('cmd')

print(1)
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
print(2)
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
print(3)
class Phoneinfo:
    def getInfo(self):
        try:
            from phonenumbers import timezone, geocoder, carrier, parse
            number = input("Enter your num +__:")
            phone = parse("+" + number)
            # for know timezone of victem
            time = timezone.time_zones_for_number(phone)
            # known ISP
            simdetails = carrier.name_for_number(phone, "en")
            # known country by geo location
            country = geocoder.description_for_number(phone, "en")
            print(time)
            print(phone)
            print(simdetails)
            print(country)
            # for longitude and latitude
            from opencage.geocoder import OpenCageGeocode
            geocoder = OpenCageGeocode('1a0e423f30a943f1be940684fe4c0d56')
            query = str(country)
            result = geocoder.geocode(query)
            latitude = result[0]['geometry']['lat']
            longitude = result[0]['geometry']['lng']
            print(latitude, longitude)
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
print(4)
class Encode_md5:
    def E_md5(self):
        import hashlib
        text = input("enter your text you want to convert md5hash: ")
        hash = hashlib.md5(text.encode())
        md5_hash = hash.hexdigest()
        print("Your md5 hash is: ", md5_hash)
print(5)
class Decode_md5:
    def D_md5(self):
        import hashlib
        flag = 0
        print("===it only encode md5 hash value====")
        pass_hash = input("enter md5hash value here: ")
        wordlist=''
        wordlist = input("location of your wordlist if you don't Enter: ")
        try:
            pass_file = open(wordlist, 'r')
        except:
            print("File not found!")
            quit()
        for i in pass_file:
            enc_word = i.encode("utf-8")
            # convert hash to md5
            digest = hashlib.md5(enc_word.strip()).hexdigest()
            # compare our hash to wordlist
            if digest == pass_hash:
                print("password found!!")
                print("pwd is:", i)
                flag = 1
                break
            elif flag == 0:
                print("passwd not found!@")

print(7)
class N_speed:
    def InetSpeed(self):
        # Internet speed test program
        # pip install speedtest-cli
        import speedtest
        test = speedtest.Speedtest()
        print("Loading server List......")
        test.get_servers()  # get list of servers
        print("Choosing best server........")
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
print(8)
class LinkImg:
    def link_img(self):
        import qrcode
        link=input("[+]enter your link you want to convert:> ")
        img=qrcode.make(link)
        img.save("qrcode.jpg")
        print("Your img was create and store in folder please check.")
print(9)
class TextToVoice:
    def T_V(self):
        while(1):
            try:
                from gtts import gTTS
                import os
                # forFile=open("text.txt","r")
                # forFileText=forFile.read().replace("\n"," ")
                myText = input("enter your text: ")
                language = 'en'
                output = gTTS(text=myText, lang=language, slow=False)
                output.save("output.mp3")
                os.system("start output.mp3")
            except:
                print("sorry for your interption can you say it again")
toolpad=HM_Calc()
disc=Discount()
pInfo=Phoneinfo()
D_hash=Decode_md5()
E_hash=Encode_md5()
TV=TextToVoice()
inetspeed=N_speed()
link_img=LinkImg()
print("finish program")
