from flask import Flask, request, jsonify, render_template
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aes')
def aes_page():
    return render_template('aes.html')

@app.route('/rsa')
def rsa_page():
    return render_template('rsa.html')

# AES şifreleme
@app.route('/aes/encrypt', methods=['POST'])
def aes_encrypt():
    data = request.json.get('data')
    key = request.json.get('key')
    if not data or not key:
        return jsonify({'error': 'Data and key required'}), 400
    key_bytes = hashlib.sha256(key.encode()).digest()[:16]
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode()
    ct = base64.b64encode(ct_bytes).decode()
    return jsonify({'iv': iv, 'ciphertext': ct})

# AES şifre çözme
@app.route('/aes/decrypt', methods=['POST'])
def aes_decrypt():
    ct = request.json.get('ciphertext')
    key = request.json.get('key')
    iv = request.json.get('iv')
    if not ct or not key or not iv:
        return jsonify({'error': 'Ciphertext, key and iv required'}), 400
    key_bytes = hashlib.sha256(key.encode()).digest()[:16]
    iv_bytes = base64.b64decode(iv)
    ct_bytes = base64.b64decode(ct)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv=iv_bytes)
    pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return jsonify({'plaintext': pt.decode()})

# RSA anahtar üret
@app.route('/rsa/generate', methods=['POST'])
def rsa_generate():
    key = RSA.generate(2048)
    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()
    return jsonify({'public_key': public_key, 'private_key': private_key})

# RSA şifreleme
@app.route('/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.json.get('data')
    public_key = request.json.get('public_key')
    if not data or not public_key:
        return jsonify({'error': 'Data and public_key required'}), 400
    try:
        key = RSA.import_key(public_key)
        cipher = PKCS1_OAEP.new(key)
        ct_bytes = cipher.encrypt(data.encode())
        ct = base64.b64encode(ct_bytes).decode()
        return jsonify({'ciphertext': ct})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# RSA şifre çözme
@app.route('/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    ct = request.json.get('ciphertext')
    private_key = request.json.get('private_key')
    if not ct or not private_key:
        return jsonify({'error': 'Ciphertext and private_key required'}), 400
    try:
        key = RSA.import_key(private_key)
        cipher = PKCS1_OAEP.new(key)
        pt = cipher.decrypt(base64.b64decode(ct))
        return jsonify({'plaintext': pt.decode()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# SHA256 özet
@app.route('/sha256', methods=['POST'])
def sha256_hash():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'Data required'}), 400
    hash_obj = hashlib.sha256(data.encode())
    return jsonify({'sha256': hash_obj.hexdigest()})

@app.route('/sha256/file', methods=['POST'])
def sha256_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Dosya bulunamadı.'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Dosya seçilmedi.'}), 400
    file_content = file.read()
    hash_obj = hashlib.sha256(file_content)
    return jsonify({'sha256': hash_obj.hexdigest()})

if __name__ == '__main__':
    app.run(debug=True) 