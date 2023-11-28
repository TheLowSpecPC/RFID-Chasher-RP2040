from library import mfrc522
from time import sleep

rdr = mfrc522.MFRC522(sck=2, miso=4, mosi=3, cs=1, rst=0)

def run(inp,num):
    if num.isdigit() != True:
        num = "0"
    try:
        a = 0
        if inp == "add":
            while a == 0:
                (stat, tag_type) = rdr.request(rdr.REQIDL)

                if stat == rdr.OK:

                    (stat, raw_uid) = rdr.anticoll()

                    if stat == rdr.OK:

                        if rdr.select_tag(raw_uid) == rdr.OK:

                            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                            if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                                data = rdr.read(8)
                                datastr = ""
                                hexstr = []
                                for i in data:
                                    datastr = datastr + (chr(i))
                                    hexstr.append(hex(i))
                                
                                base = "0000000000000000"
                                if datastr.isdigit() != True:
                                    datastr = base
                                    byt = base.encode()
                                    stat = rdr.write(8, byt)
                                    
                                num = str(int(num) + int(datastr))
                                ba = base[:len(base) - len(num)]
                                byt = str(ba + num).encode()
                                stat = rdr.write(8, byt)
                                a += 1
                                rdr.stop_crypto1()
                                if stat == rdr.OK:
                                    re = byt.decode()
#                                    print(byt.decode())
                                return re

        elif inp == "sub":
            while a == 0:
                (stat, tag_type) = rdr.request(rdr.REQIDL)

                if stat == rdr.OK:

                    (stat, raw_uid) = rdr.anticoll()

                    if stat == rdr.OK:

                        if rdr.select_tag(raw_uid) == rdr.OK:

                            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                            if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                                data = rdr.read(8)
                                datastr = ""
                                hexstr = []
                                for i in data:
                                    datastr = datastr + (chr(i))
                                    hexstr.append(hex(i))
                                
                                base = "0000000000000000"
                                if datastr.isdigit() != True:
                                    datastr = base
                                    byt = base.encode()
                                    stat = rdr.write(8, byt)
                                    
                                if int(datastr) >= int(num):
                                    num = str(int(datastr) - int(num))
                                    ba = base[:len(base) - len(num)]
                                    byt = str(ba + num).encode()
                                    stat = rdr.write(8, byt)
                                    if stat == rdr.OK:
                                        re = byt.decode()
#                                        print(byt.decode())
                                    return re
                                else:
#                                    print("No Sufficient Balance")
                                    return "No Sufficient   Balance"
                                a += 1
                                rdr.stop_crypto1()
                                
        if inp == "bal":
            while a == 0:
                (stat, tag_type) = rdr.request(rdr.REQIDL)

                if stat == rdr.OK:

                    (stat, raw_uid) = rdr.anticoll()

                    if stat == rdr.OK:

                        if rdr.select_tag(raw_uid) == rdr.OK:

                            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                            if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                                data = rdr.read(8)
                                datastr = ""
                                hexstr = []
                                for i in data:
                                    datastr = datastr + (chr(i))
                                    hexstr.append(hex(i))
#                                    print(str(datastr))
                                a += 1
                                rdr.stop_crypto1()
                                return str(datastr)


    except KeyboardInterrupt:
        pass