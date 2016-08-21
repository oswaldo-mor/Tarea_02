#encoding: UTF-8

# Autor: Morales Rodriguez Oswaldo, A01378566
# Descripcion: Conociendo el subtotal, conocer la propina, IVA y gran total.

# A partir de aqui escribe tu programa
subtotal=int(input("Subtotal de la comida"))
propina=subtotal*0.15
iva=subtotal*0.16
total=subtotal+propina+iva
print("El subtotal es",subtotal, "la propina es",propina,"El IVA es",iva, "total completo es",total)
