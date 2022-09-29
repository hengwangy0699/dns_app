from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'FS server'

import socket
@app.route('/register', methods = ['PUT'])
def register():
    req = request.json
    hostname = req['hostname']
    ip = req['ip']
    as_ip = req['as_ip']
    as_port = int(req['as_port'])

    MESSAGE = "TYPE=A\nNAME={0}\nVALUE={1}\nTTL=10".format(hostname, ip)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(bytes(MESSAGE, "utf-8"), (as_ip, as_port))
    
    return "", 201

@app.route('/fibonacci', methods = ['GET'])
def fib():
    req = request.args
    seq_num = req.get("number")

    if seq_num:
        try:
            seq_num = int(seq_num)
        except:
            return "Required number is not an integer.", 400

        f = [0, 1]
        for i in range(2, seq_num):
            f.append(f[i-1]+f[i-2])
        
        return str(f[seq_num-1]), 200
    else:
        return "Failed", 400
    
app.run(host='0.0.0.0',
        port=9090,
        debug=True)
