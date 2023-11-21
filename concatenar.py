a = "Danilo"
b = "Santos"

nome_completo = a + " " + b
nome_completo2 = "{} {}".format(a,b)
nome_completo3 = f"{a} {b}"

print(nome_completo)
print(nome_completo2)
print(nome_completo3)
print(nome_completo3[0:4])

nome_alterado = nome_completo3.replace("Santos", "Aparecido")
print(nome_alterado)

nome_strip = "    Joana de lima   "
nome_strip = nome_strip.strip()
# nome_strip = nome_strip.rstrip()
# nome_strip = nome_strip.lstrip()
print(f"[{nome_strip}]")
