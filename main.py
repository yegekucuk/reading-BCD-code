# Written in PyCharm
def encode():
    with open("enc.file", "r") as e:
        exec(e.read())


def decode():
    with open("encrypted.txt", "r") as f:
        characters = f.read().strip().split()
        asciicharacters = list(map(lambda x: int(x, 2), characters))
        p = "".join(list(map(chr, asciicharacters)))
        print(p)


if __name__ == "__main__":
    # encode()
    decode()

    
