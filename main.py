import speedtest

#Create a Speedtest object
test = speedtest.Speedtest()

#Measure download and upload speeds
download = test.download()
upload = test.upload()

#Convert the speeds from bits per second to megabits per second
download_mbps = download / 1_000_000
upload_mbps = upload / 1_000_000

#Print the results in megabits per second
print(f"Download speed: {download_mbps:.2f} Mbps")
print(f"Upload speed: {upload_mbps:.2f} Mbps")