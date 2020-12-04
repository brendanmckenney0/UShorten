import requests

text = "UShorten"
from PIL import Image, ImageDraw, ImageFont
import numpy as np
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getsize(text)
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ','#'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print( "\n".join(strings))

intro_text = """


Hi. Enter any url to shorten it!



Contact me at www.brendanmckenney.com or at brendanmckenney@gmail.com.

Thanks!




"""


# Bitly account creds
username = "brendanmckenney"
passwd = "Bobcats0114"

auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, passwd))
if auth_res.status_code == 200:
    access_token = auth_res.content.decode()
    print("Retrieved access token!")
else:
    print("Couldn't get access token.")
    exit()



headers = {"Authorization": f"Bearer {access_token}"}

groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)

if groups_res.status_code == 200:
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("Couldn't get GUID. Bye!")
    exit()

#Shortening

while True:
    print(intro_text)
    url = input()
