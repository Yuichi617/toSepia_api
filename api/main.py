from flask import Flask, request, make_response, send_file, jsonify
from flask_cors import CORS
from PIL import Image
from io import BytesIO
# import numpy as np
# import cv2

app = Flask(__name__)
CORS(app) # 全てのオリジンからのアクセスを許可
model = None

# テスト用
@app.route('/test', methods=["GET"])
def get_test():
    response = {
        "success": True,
        "method": "GET"
    }
    return jsonify(response)

@app.route('/to-sepia', methods=["POST"])
def predict():
    try:
        # バイナリストリームに変換してPillowに変換  
        img = Image.open(BytesIO(request.data)).convert('RGB')
        # 画像処理
        gray = img.convert("L")
        img = Image.merge(
            "RGB",
            (   
                gray.point(lambda x: x * 240 / 255),
                gray.point(lambda x: x * 200 / 255),
                gray.point(lambda x: x * 145 / 255)
            )
        )
        # Pillowをバイナリストリームに変換
        img_io = BytesIO()
        img.save(img_io, 'JPEG', quality=95)
        img_io.seek(0)

        # レスポンスデータの作成
        print(type(send_file(img_io, mimetype='image/jpeg')))
        response = make_response(send_file(img_io, mimetype='image/jpeg'))
        return response

    except Exception as e: # デバッグ用
        print(e)  
        return "error"
    
if __name__ == '__main__':
    print(" * Flask starting server...")
    app.run(port=8080, debug=True)