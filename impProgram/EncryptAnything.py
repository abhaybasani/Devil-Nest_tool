class X:
    # fernet =it help to genrate secret key
    from cryptography.fernet import Fernet
    # --------------------------------------------------genrate the key for encryption and decryption-------------------------------
    global fernet, key
    key=Fernet.generate_key()
    # print("[*]your key is:> ",key)
    # encryption
    fernet=Fernet(key)

    #-----------------------------[writing the key] it create a file which contain file=key.key, wb=write-------------------
    with open('key.key', 'wb') as filekey:
        filekey.write(key)
    #[reading the key]
    with open ('key.key', 'rb') as filekey:
        key=filekey.read()
    def encrypt(self):
        print("[*]your encryption key is:> ", key)
        try:
            # --------------------- {read the file} you want to encrypt [any file audio img video txt file] laser.wav=audio file---------------------------------
            select_file=input("[+]Enter file name which locatate on your folder: ")
            with open(f'{select_file}', 'rb') as file:
                orignal_file = file.read()
            # ---------------------------------------------------encrypt that file you read----------------------------------
            encrypted = fernet.encrypt(orignal_file)
            # save that encrypted file so it show on folder
            enc_file=input("[+]New name of encrypted file:> ")
            with open(f'{enc_file}', 'wb') as file:
                file.write(encrypted)
                print("---Your file was encrypted check your folder---")
        except FileNotFoundError:
            print("[/]Please choose that file which already store on your folder")
        except:
            print("please get some help!!")

    def decprypt(self):
        from cryptography.fernet import Fernet
        # ------------------------------------------decryption------------------------------------------------------------
        # decrypting the file
        # fernet=Fernet(here you send the key you genrated to reciver so they can decrypt file.
        fernet = Fernet(key)
        # read encrypted file
        efile=input("[+]Enter file name for decrypt:>")
        with open(efile, 'rb') as file:
            encrypted_file = file.read()
        # decypted file
        decrypted = fernet.decrypt(encrypted_file)
        print(2)
        # create decrypt file
        dname=input("[+]New decryption name:>")
        with open(dname, 'wb') as file:
            file.write(decrypted)
            print("---Your file was decrypted check your folder---")

x=X()
x.encrypt()
x.decprypt()