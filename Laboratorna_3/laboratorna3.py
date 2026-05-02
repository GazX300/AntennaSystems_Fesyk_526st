import numpy as np
import matplotlib.pyplot as plt

# Дані Варіанта №7
lam = 3.9
h = 16.0
L = 23.7
xi = 1 + lam / (2 * L)

theta_deg = np.linspace(-90, 90, 1000)
theta_rad = np.deg2rad(theta_deg)

psi = (np.pi * L / lam) * (xi - np.cos(theta_rad))
F_b = np.abs(np.sin(psi) / psi)
F_b_max = np.abs(np.sin((np.pi * L / lam)*(xi - 1)) / ((np.pi * L / lam)*(xi - 1)))
F_single_H = F_b / F_b_max
F_single_E = F_single_H * np.abs(np.cos(theta_rad))

F_c = np.abs(np.cos((np.pi * h / lam) * np.sin(theta_rad)))
F_double_H = F_single_H * F_c
F_double_E = F_single_E * F_c

fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Площина H
axs[0].plot(theta_deg, F_single_H, 'b--', label='Один стрижень')
axs[0].plot(theta_deg, F_double_H, 'r-', label='Два стрижні')
axs[0].axhline(y=0.707, color='g', linestyle=':', label='Рівень 0.707')
axs[0].set_title('ДС у площині H')
axs[0].legend()

# Площина E
axs[1].plot(theta_deg, F_single_E, 'b--', label='Один стрижень')
axs[1].plot(theta_deg, F_double_E, 'r-', label='Два стрижні')
axs[1].axhline(y=0.707, color='g', linestyle=':', label='Рівень 0.707')
axs[1].set_title('ДС у площині E')
axs[1].legend()

for ax in axs:
    ax.set_xlabel('Кут Theta, град')
    ax.set_ylabel('Нормована ДС')
    ax.grid(True)
    ax.set_xlim([-90, 90])

plt.savefig('ДС_ДСА.png', dpi=300, bbox_inches='tight')
plt.show()

theta_05 = 61 * np.sqrt(lam / L)
print(f"Теоретична ширина головної пелюстки (2*theta_0.5): {theta_05:.2f} град")