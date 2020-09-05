import time
import speedtest
import datetime


while True:

    f = open("internet_speed_monitor.csv", "a")
    try:
        st = speedtest.Speedtest()
        dl_speed = st.download() / 1000000
        up_speed = st.upload() / 1000000
        latency = st.results.ping
        timestamp = datetime.datetime.now()

        print("Down: ", dl_speed)
        print("Up: ", up_speed)
        print(latency)

        f.write(str(timestamp))
        f.write(",")
        f.write(str(dl_speed))
        f.write(",")
        f.write(str(up_speed))
        f.write(",")
        f.write(str(latency))
        f.write(" ms")
        f.write("\n")
        f.close()

        time.sleep(600)
    except:
        timestamp = datetime.datetime.now()
        f.write(str(timestamp))
        f.write(",")
        f.write("0")
        f.write(",")
        f.write("0")
        f.write(",")
        f.write("0")
        f.write("--")
        f.write("\n")
        f.close()
        print("DNS Down")
        time.sleep(10)