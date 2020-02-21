import requests
import shutil
    
for num in range(0, 500): #can roll over to 501, 502, etc.
    urlnum = ("000" + str(num + 1))[-4:]
    url = f"https://fromthepage.com/images/uploaded/21919/page_{urlnum}.jpg"
    resp = requests.get(url, stream=True)
    if resp.status_code is 404:
        print(f"404 at {urlnum}")
    
    f = open(f'{urlnum}.jpg', 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, f)
    f.close()
    del resp
