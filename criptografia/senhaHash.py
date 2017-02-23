# encoding: utf-8
import uuid
import hashlib

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = input('Por favor entre com uma senha: ')
hashed_password = hash_password(new_pass)
print('A string armazenada no bd é: ' + hashed_password)
old_pass = input('Agora por favor entre com a senha novamente para checar: ')
if check_password(hashed_password, old_pass):
    print('A senha está correta!')
else:
    print('Desculpe, essa senha não confere!')
