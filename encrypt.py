import pyAesCrypt

password = input('Введите пароль для шифрования файла: ')

pyAesCrypt.encryptFile('test', 'test.aes', password)