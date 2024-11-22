import bcrypt

# Генерация соли
salt = bcrypt.gensalt()

# Хэширование пароля
password = "pass3"
pass_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

# Сохраните pass_hash в базе данных
print(pass_hash)