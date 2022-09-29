import socket, json
from collections import defaultdict

IP = "0.0.0.0"
PORT = 53533

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))
    print("DNS Listening on {0}:{1} ...".format(IP, PORT))
    while True:
        data, addr = sock.recvfrom(512)
        data = data.decode("utf-8")
        str_list = data.split("\n")

        dic = defaultdict(list)
        for s in str_list:
            item = s.split("=")
            dic[item[0]] = item[1]

        if dic["VALUE"]: # Registration
            dic = json.dumps(dic).encode("utf-8")
            print(dic)
            f = open("list.txt", mode="ab")
            f.write(dic)
            f.write(b"\n")
            f.close()
        else: # DNS Query
            f = open("list.txt", mode="r")
            txt = f.read()
            f.close()
            data = txt.split("\n")
            idx = -1
            for record in data:
                record = record[1:-1]
                record = record.split(", ")
                flag = 0
                for i, items in enumerate(record):
                    items = items[1:-1]
                    kv = items.split("\"")
                    if kv[0] == "TYPE":
                        if kv[2] == dic["TYPE"]:
                            flag += 1

                    if kv[0] == "NAME":
                        if kv[2] == dic["NAME"]:
                            flag += 1

                    if flag == 2:
                        idx = i
            
            response = ""
            for items in record[idx]:
                items = items[1:-1]
                kv = items.split("\"")
                response += "{0}={1}\n".format(kv[0], kv[2])

            # sock.sendto(bytes(response, "utf-8"), (IP, PORT))

if __name__ == "__main__":
    main()