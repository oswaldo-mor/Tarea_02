#encoding: UTF-8

# Autor: Morales Rodriguez Oswaldo
# Descripcion: Con las coordenadas cartesianas, obtener las polares


from math import atan2, pi
x=int(input("valor de x"))
y=int(input("valor de y"))
r=((x**2)+(y**2))**0.5
z=atan2(y,x)
ang=(180*z)/pi
print("Hipotenusa es",r,"angulo es",ang)
