class X:
    # fernet =it help to genrate secret key
    from cryptography.fernet import Fernet
    # --------------------------------------------------genrate the key for encryption and decryption-------------------------------
    global key, fernet
    key=Fernet.generate_key()
    # print("[*]your key is:> ",key)
    # encryption
    fernet=Fernet(key)

    #-----------------------------[writing the key] it create a file which contain file=key.key, wb=write-------------------
    with open('key.key','wb') as filekey:
        filekey.write(key)
    #[reading the key]
    with open ('key.key','rb') as filekey:
        key=filekey.read()
    def encrypt(self):
        print("[*]your key is:> ", key)
        try:
            # --------------------- {read the file} you want to encrypt [any file audio img video txt file] laser.wav=audio file---------------------------------
            select_file=input("[+]Enter file name which locatate on your folder: ")
            with open(f'{select_file}', 'rb') as file:
                orignal_file = file.read()
            # ---------------------------------------------------encrypt that file you read----------------------------------
            encrypted = fernet.encrypt(orignal_file)
            # save that encrypted file so it show on folder
            enc_file=input("enter encripted file name with extention: ")
            with open(f'{enc_file}', 'wb') as file:
                file.write(encrypted)
                print("---Your file was encrypted check your folder---")
        except FileNotFoundError:
            print("[/]Please choose that file which already store on your folder")
        except:
            print("please get some help!!")

    def decprypt(self):
        print("[*]your key is:> ", key)
        from cryptography.fernet import Fernet
        # ------------------------------------------decryption------------------------------------------------------------
        # decrypting the file
        # fernet=Fernet(here you send the key you genrated to reciver so they can decrypt file)
        fernet = Fernet(key)
        # read encrypted file
        with open('encrypted laser.wav', 'rb') as file:
            encrypted_file = file.read()

        # decypted file
        decrypted = fernet.decrypt(encrypted_file)

        # create decrypt file
        with open('decrypted laser.wav', 'wb') as file:
            file.write(decrypted)
            print("---Your file was encrypted check your folder---")

x=X()
