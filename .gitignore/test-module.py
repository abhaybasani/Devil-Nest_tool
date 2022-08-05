import os
x=os.system('cmd /k "netsh wlan show profile"')
print(x)
user=input("Enter wifi name:>")
y=os.system(f'cmd/k "netsh wlan show profile name={user} key=clear"')
print(y)