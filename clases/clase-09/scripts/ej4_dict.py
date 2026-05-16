usuario_dict = {
    "usuario": "chazargl",
    "email": "chazargl@gmail.com",
    "activo": True
}

print('El mail del usuario es: ',usuario_dict["email"])
usuario_dict["activo"] = False
usuario_dict["ultimo_login"] = 2026
print(usuario_dict)