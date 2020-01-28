from PIL import Image
import binascii
import optparse
import codecs

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def hex2rgb(hexcode):
    return tuple(map(ord, codecs.decode(hexcode[1:].encode())))[3:]


def str2bin(message):
    binary = bin(int(binascii.hexlify(message.encode()), 16))
    return binary[2:]


def binary2str(binary):
    message = binascii.unhexlify('%x' % (int('0b' + binary, 2)))
    return message


def encode(hexcode, digit):
    if hexcode[-1] in ('0', '1', '2', '3', '4', '5'):
        hexcode = hexcode[:-1] + digit
        return hexcode
    else:
        return None


def decode(hexcode):
    if hexcode[-1] in ('0', '1'):
        return hexcode[-1]
    else:
        return None


def hide(filename, message):
    img = Image.open(filename)
    binary = str2bin(message) + '1111111111111110'
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        new_data = []
        digit = 0
        temp = ''
        for item in datas:
            if (digit < len(binary)):
                newpix = encode(rgb2hex(item[0], item[1], item[2]), binary[digit])
                if newpix == None:
                    new_data.append(item)
                else:
                    r, g, b = hex2rgb(newpix)
                    new_data.append((r, g, b, 255))
                    digit += 1
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(filename, 'BMP')
        return "Completed!"
    return "Incorrect image mode, couldn't hide"


def retr(filename):
    img = Image.open(filename)
    binary = ''

    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        for item in datas:
            digit = decode(rgb2hex(item[0], item[1], item[2]))
            if digit == None:
                pass
            else:
                binary = binary + digit
                if (binary[-16:] == '1111111111111110'):
                    print("Success")
                    return binary2str(binary[:-16])
        return binary2str(binary)
    return "Incorrect image mode,couldn't retrieve"


choice = input("1.Hide\n2.Retrieve\n")
if choice == '1':
    filename = input('Enter path to file: ')
    message = input('Enter message you wanna hide: ')
    print(hide(filename, message))
elif choice == '2':
    filename = input('Enter path to file: ')
    print(retr(filename))
