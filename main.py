import speedtest

test = speedtest.Speedtest()

download = test.download()
upload = test.upload()

download_mbps = download / 1_000_000
upload_mbps = upload / 1_000_000

print(f"Download speed: {download_mbps:.2f} Mbps")
print(f"Upload speed: {upload_mbps:.2f} Mbps")
