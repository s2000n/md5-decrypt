import hashlib

def read_file(file_path, inp1):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if inp1 == hashlib.md5(line.strip().encode()).hexdigest():
                    print('Hash ',inp1 ,' decrypted is: ', line.strip())
                    return
            print('Hash not found.')
    except FileNotFoundError:
        print("File not found.")

input1 = input('Enter hash: ')
read_file('wordlist.txt', input1)
input('Press Enter to exit')