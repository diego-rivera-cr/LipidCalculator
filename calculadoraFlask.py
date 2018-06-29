from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

HDLcolesterol = 35
colesterol = 218
trigliceridos = 131

def main():
	app.run()
	print('Colesterol:', colesterol)
	print('HDL-Colesterol:', HDLcolesterol)
	LDL = calculoLDL(colesterol, HDLcolesterol, trigliceridos)
	print('LDL:', LDL)
	print('VLDL:',calculoVLDL(trigliceridos))
	print('Relación Colesterol/HDL:',RelacionCHOLtoHDL(colesterol,HDLcolesterol))
	print('Relación LDL/HDL:',LDL/HDLcolesterol)
	print('Triglicéridos',trigliceridos)
	return 0

def calculoVLDL(Trigliceridos):
	if Trigliceridos <400:
		VLDL = Trigliceridos/5
	else:
		VLDL = 'No se puede calcular por TG>400'
	return VLDL

def calculoLDL(CHOL, HDL, TRIG):
	if TRIG <400:
		LDL = CHOL - HDL - calculoVLDL(TRIG)
	else:
		LDL = 'No se puede calcular por TG>400'
	return LDL

def RelacionCHOLtoHDL(CHOL, HDL):
	relaxCH = CHOL/HDL
	return relaxCH		
		
def RelacionCHOLtoLDL(CHOL,LDL):
	try:
		relaxCL = CHOL/LDL
	except:
		relaxCL = 'No se puede calcular'
	return relaxCL
		
if __name__ == '__main__':
	main()

