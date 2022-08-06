print("please wait..........")
import impProgram.abhayMainProgram as amp
# import space_game
# import server,client,EncryptAnything
from termcolor import colored
banner="""
                _                      _______                      _
             _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
            dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
            V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
                     `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
                      `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
                 __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
               ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
            _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
                        `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
                ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
              ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
             ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
             MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
             YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
              `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
                `'                  `OObNNNNNdOO'                   `'
                                      `~OOOOO~'   AbhayBasani
"""
print("[##########################################################################################################")
print("[/]Hello everyone this is our projects made by: Abhay, Raju, Suraj.")
print("[-]Tool created by Abhay, Raju, Suraj.")
# ------------------------------------Manual Area----------------------------------------------------------
icon=("""
+-+-+-+-+-+ +-+-+-+-+
|D|e|v|i|l| |N|e|s|t|
+-+-+-+-+-+ +-+-+-+-+
""")
try:
    print(colored(banner, 'red'))
    print(colored(icon,'green'))
except:
    print(banner)
    print(icon)
print("----------------------------------------------------------------------------------------------------------------------------------------")
man="[::]Select An Option You Wanna do."
manual="""
        [1]Get Info using Ph.Number.                     [7]Check internet speed.
        [2]Run Space Game(GUI).                          [8]Scan any Website Open Ports.
        [3]Convert link into QRcode image.               [9]Face Detection system. 
        [4]Text to Voice converter.                      [10]Information Gathering of any Website.
        [5]Encode your message in md5hash.               [11]Encrypt Any file using cryptography.
        [6]Convert any PDF to Voice.                     [12]Voice to Text converter.
        [13]

        [99]About                           [00]Exit
"""
try:
    print(colored(man, 'magenta'))
    print(colored(manual, 'red'))
except:
    print(man)
    print(manual)
# --------------------------------------user input info area-----------------------------------------------------------------------
user=int(input("[+]Select your Option:"))
try:
    if user == 00:
        quit()
    elif user == 1:
        amp.pInfo.getInfo()
    elif user==2:
        import space_game
        space_game
    elif user==3:
        amp.link_img.link_img()
    elif user==4:
        amp.TV.T_V()
    elif user==5:
        amp.E_hash.E_md5()
    elif user ==6:
        amp.pdftovoice.PDFtoVoice()
    elif user ==7:
        amp.inetspeed.InetSpeed()
    elif user == 8:
        amp.P_S.portscan()
    elif user == 9:
        print("please wait it will start soon.......")
        amp.FaceDect.faceDect()
    elif user == 10:
        print("please wait a moment.......")
        amp.webScrap.webscrap()
    elif user == 11:
        import impProgram.EncryptAnything
    elif user == 12:
        amp.VT.X()

    elif user == 99:
        print("{#}This program was build by Abhay , Raju , Suraj if you are facing any kind of problem please contact us.We will happy to help you")
        about={
            "Email":"basaniabhay@gmail.com",
        }
except ValueError:
    print("Please type valid input.Or please get some HELP?")
except TypeError:
    print("please type anything.")
finally:
    print("Thanks for using Us.")


