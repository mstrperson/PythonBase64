__author__ = "jcox@vms.edu (Jason Cox)"

# This is the base64 charset
base64_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

def b64ToBytes(b64string):
    data = bytearray()

    for i in range(0, len(b64string), 4):
        # boolean flag to know if this is the last run of the loop.
        lastRun = i + 5 == len(b64string)

        # How do I deal with = ?
        print("reading 4 characters...")
        print(b64string[i] + b64string[i+1] + b64string[i+2] + b64string[i+3])

        # There is an error in this insanely complicated line........
        chunk = int(((base64_charset.index(b64string[i]) * 64
                      + base64_charset.index(b64string[i+1])) * 64
                     + (base64_charset.index(b64string[i+2])%64)) * 64
                    + (base64_charset.index(b64string[i+3]%64)))
        print(chunk)

        #break down the 4 character chunk into 3 bytes
        firstByte = int(chunk / 256*256)
        secondByte = int((chunk % 265*256) / 256)
        thirdByte = int(chunk % 256)

        # append the read bytes to the data array.
        data.append(firstByte)

        if not lastRun or b64string[i+2] != '=':
            data.append(secondByte)
            if not lastRun or b64string[i+3] != '=':
                data.append(thirdByte)

    print(data)
    return data


inFile = open('C:\\temp\\SecretMessage.txt.b64', 'r')
b64data = inFile.readline()
print(b64data)
data = b64ToBytes(b64data)