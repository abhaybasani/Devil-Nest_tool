print("please wait..........")
import bankAtm
# import space_game
# import server,client,EncryptAnything
import abhayMainProgram as amp
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
print()
# ------------------------------------Manual Area----------------------------------------------------------
from pyfiglet import figlet_format
icon=figlet_format("Devil Nest",font='Digital') # Colossal,big,Banner3,Digital,
print(banner)
print(icon)
print("----------------------------------------------------------------------------------------------------------------------------------------")
print("[::]Select An Option You Wanna do.")
print("""
[1]Get Info using Ph.Number.                    [7]check internet speed.
[2]Run Space Game(gui).                         [8]convert link into image.
[3]Voice to Text converter.                     [9]Open bind connection server and client. 
[4]Text to Voice converter.                     [10]Encrypt Any file using cryptography.
[5]Encode your message in md5hash.              [11]
[6]Decode md5hash code.

[99]About                           [00]Exit
""")
# --------------------------------------user input info area-----------------------------------------------------------------------
user=int(input("[+]Select your Option:"))
try:
    if user == 00:
        quit()
    elif user == 1:
        amp.pInfo.getInfo()
    elif user==2:
        import space_game
    elif user==3:
        amp.VT.X()
    elif user==4:
        amp.TV.T_V()
    elif user==5:
        amp.E_hash.E_md5()
    elif user ==6:
        amp.D_hash.D_md5()
    elif user ==7:
        amp.inetspeed.InetSpeed()
except ValueError:
    print("Please type valid input.Or please get some HELP?")
except TypeError:
    print("please type anything.")
finally:
    print("Thanks for using Us.")


