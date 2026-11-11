from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/goods/g001')
def goods_detail():
    return jsonify({
        "id": "g001",
        "name": "奶油法式猫眼",
        "price": 68,
        "unit": "副"
    })

if __name__ == '__main__':
    app.run(port=8080, debug=True)