
# Encontrar la longitud de la Hipotenusa

import matplotlib.pyplot as plt
import pandas as pd
import math

plt.figure(figsize = (5, 3), layout = 'constrained')

A = int(input("Escribe tu coordenada : "))
B = int(input("Escribe tu coordenada : "))

H = math.sqrt(A ** 2 + B ** 2)

DF = pd.DataFrame({
    
	"Catetos": [A, B],
	"Hipotenusa": [H, 0]
})

DF["Hipotenusa"].plot()

plt.title('Hipotenusa')
plt.ylabel('Cateto A')
plt.xlabel('Cateto B')
plt.legend(loc = 'upper center', facecolor = 'pink') 

print(f'H = {H}')

plt.show()