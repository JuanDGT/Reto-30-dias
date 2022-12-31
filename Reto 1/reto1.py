import pandas as pd
fichero = 'Correos.xlsx'
archivo = pd.read_excel(fichero)
Correo = archivo['Correo']
newCorreo = []
for i in Correo:
    if i not in newCorreo:
        newCorreo.append(i)
print(newCorreo)