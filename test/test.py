import urllib.parse
import urllib.request
from PIL import Image
from io import BytesIO

# 画像データの読み込み (バイナリモード)
f = open("images/240_main.jpeg", mode="rb")
reqbody = f.read()
f.close()

# リクエストの作成
url = "http://127.0.0.1:8080/to-sepia"
req = urllib.request.Request(
    url,
    data =reqbody,
    method="POST",
    headers={"Content-Type": "application/octet-stream"},
)

# リクエストの送信とレスポンスの受け取り
with urllib.request.urlopen(req) as res:
    # Pillowに変換  
    img = Image.open(BytesIO(res.read())).convert('RGB')
    img.save('sepia.jpg', quality=95)