import pyAesCrypt

password = input('Введите пароль для дешифрования файла: ')

pyAesCrypt.decryptFile('test.aes', 'testout', password)