import os
import pyaes
file_name= "foto.txt.pyransom"
file= open(file_name, "rb")
file_data= file.read()
file.close()
key= b"0143256879fravtr"
aes= pyaes.AESModeOfOperationCTR(key)
decrypt_data= aes.decrypt(file_data)
#removendo o arquivo
os.remove(file_name)
new_file_name= "foto.txt"
new_file= open(new_file_name, "wb")
new_file.write(decrypt_data)
new_file.close()