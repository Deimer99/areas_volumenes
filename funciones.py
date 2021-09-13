import math
def calcular_area_cuadrado (lado):
	area=lado*lado
	return area

def calcular_volumen_paralelepipedo(base,altura, alto):
	volumen=base*altura*alto
	return volumen
	
def calcular_volumen_cilindro(radio,altura):
	volumenc=math.pi*radio**2*altura
	return volumenc
		
#print(f"El area del cuadrado es {calcular_area_cuadrado(4)}")

	 
	
