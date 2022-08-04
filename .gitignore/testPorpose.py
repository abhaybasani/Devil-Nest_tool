# from pyfiglet import figlet_format
# text=figlet_format("Devil Nest",font='big')
# print(text)


def InetSpeed():
	# Internet speed test program
	# pip install speedtest-cli
	import pyspeedtest
	test = pyspeedtest.SpeedTest()
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

InetSpeed()