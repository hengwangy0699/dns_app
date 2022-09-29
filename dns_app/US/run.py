from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'US Server'

@app.route('/fibonacci', methods = ['GET'])
def fib():
    req = request.args
    hostname = req.get("hostname")
    fs_port = req.get("fs_port")
    seq_num = req.get("number")
    as_ip = req.get("as_ip")
    as_port = req.get("as_port")

    if hostname and fs_port and seq_num and as_ip and as_port:
        print("Success")
        try:
            seq_num = int(seq_num)
        except:
            return "Required number is not an integer.", 400

        f = [0, 1]
        for i in range(2, seq_num):
            f.append(f[i-1]+f[i-2])
        
        return str(f[seq_num-1]), 200
    else:
        print("Failed")
        return "Failed", 400
    

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
