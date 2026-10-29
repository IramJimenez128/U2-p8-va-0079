import numpy as np
import matplotlib.pyplot as plt

diasx = ["Lun", "Mar", "Mie", "Jue", "Vie"]
califa_va_y = [5, 6, 3, 8, 10]
plt.bar(diasx,califa_va_y)
plt.title("Calificaciones en VA de Iram Jimenez NC = 0079")
plt.xlabel("Dias de la semana habil")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()
