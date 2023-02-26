
import matplotlib.pyplot as plt

Eje_X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Eje_Y = [20340, 21033, 21440, 22509, 23887, 21490, 22400, 24943, 23098, 23450, 26900, 28034]
Eje = [20340, 21033, 21440, 22509, 23887, 21490, 22400, 24943, 23098, 23450, 26900, 28034]

print(plt.style.available)
plt.style.use('seaborn')

plt.plot(Eje_X, Eje_Y, color = 'b', linestyle = 'dotted', marker = 'o', label = "Empresa A")
plt.plot(Eje_X, Eje, color = 'r', linestyle = 'dotted', marker = 'd', label = "Empresa B")

plt.xlabel("Meses")
plt.ylabel("Valor de mercado empresa A (c)")
plt.title("Valor de mercado por meses (c)")

plt.ylim(0, 30000)
plt.xticks(Eje_X)

plt.minorticks_on()
plt.tick_params(axis = 'both', which = 'both', top = True, right = True)

plt.grid(True)
plt.legend()

plt.show()