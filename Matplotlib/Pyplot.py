
import matplotlib.pyplot as plt

eje_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
eje_y = [20340, 21033, 21440, 22509, 23887, 21490, 22400, 24943, 23098, 23450, 26900, 28034]
eje = [20340, 21033, 21440, 22509, 23887, 21490, 22400, 24943, 23098, 23450, 26900, 28034]

print(plt.style.available)
plt.style.use('seaborn')

plt.plot(eje_x, eje_y, color = 'b', linestyle = 'dotted', marker = 'o', label = "Empresa A")
plt.plot(eje_x, eje, color = 'r', linestyle = 'dotted', marker = 'd', label = "Empresa B")

plt.xlabel("Meses")
plt.ylabel("Valor de mercado empresa A (c)")
plt.title("Valor de mercado por meses (c)")

plt.ylim(0, 30000)
plt.xticks(eje_x)

plt.minorticks_on()
plt.tick_params(axis = 'both', which = 'both', top = True, right = True)

plt.grid(True)
plt.legend()

plt.show()