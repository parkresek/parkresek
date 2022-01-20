username = str(input("masukkan username : "))
password = str(input("masukkan password : "))
username_from_db = "user"
password_from_db = "admin"
if username == username_from_db :
 if password == password_from_db :
     print ("Username dan password cocok ")
 else:
     print ("Password salah ")
else:
 print ("User tidak terdaftar")
