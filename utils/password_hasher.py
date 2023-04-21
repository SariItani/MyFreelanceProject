import bcrypt

passwords = ["password123", "helloWorld!", "letmein", "p@ssword123", "qwerty1234", "letmein!", "hello123", "welcome123", "password1234", "12345678", "s3cur3Pa55word", "Pa$$word123"]

for password in passwords:
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    print(f"Password: {password}")
    print(f"Hash: {hashed.decode('utf-8')}\n")
