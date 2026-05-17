import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv

lam = 0.026
D = 0.5
f = 0.2

k = 2 * np.pi / lam
R0 = D / 2
p = 2 * f
v = 3.5 * (R0 / p)

theta = np.linspace(-np.pi/4, np.pi/4, 2000) + 1e-12
u = k * R0 * np.sin(theta)

norm_factor = 1 / (0.74 * (jv(1, v) / v) + 0.13)

term1 = 0.74 * (v * jv(1, v) * jv(0, u) - u * jv(1, u) * jv(0, v)) / (v**2 - u**2)
term2 = 0.26 * (jv(1, u) / u)
term3 = 0.25 * (u * jv(1, u) * jv(2, 1.5*v) - 1.5*v * jv(1, 1.5*v) * jv(2, u)) / ((1.5*v)**2 - u**2)

cos_half_theta_sq = np.cos(theta / 2)**2

F_H = cos_half_theta_sq * (term1 + term2 - term3) * norm_factor
F_E = cos_half_theta_sq * (term1 + term2 + term3) * norm_factor

F_H_abs = np.abs(F_H)
F_E_abs = np.abs(F_E)

plt.figure(figsize=(10, 6))

plt.plot(np.degrees(theta), F_E_abs, label='Площина E ($F_E$)', color='blue')
plt.plot(np.degrees(theta), F_H_abs, label='Площина H ($F_H$)', color='red', linestyle='--')

plt.axhline(y=0.707, color='green', linestyle=':', label='Рівень 0.707')

plt.title('Нормовані діаграми спрямованості ДЗА (Варіант 7)')
plt.xlabel('Кут $\\theta$, градуси')
plt.ylabel('Амплітуда (нормована)')
plt.grid(True)
plt.legend()
plt.xlim(-20, 20)
plt.savefig('ДС ДзА.png', dpi=300, bbox_inches='tight')
plt.show()