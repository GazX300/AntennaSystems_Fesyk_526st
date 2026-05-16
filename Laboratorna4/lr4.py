import numpy as np
import matplotlib.pyplot as plt

# Вхідні дані для Варіанту 7
lambda_val = 2.6
N = 14
l = 1.6
d = 2.0

k = 2 * np.pi / lambda_val

theta_deg = np.linspace(-90, 90, 1000)
theta_rad = np.radians(theta_deg)

psi_space = k * d * np.sin(theta_rad)
Fc = np.zeros_like(theta_rad)
for i, p in enumerate(psi_space):
    if abs(p) < 1e-5:
        Fc[i] = 1.0
    else:
        Fc[i] = np.sin(N * p / 2) / (N * np.sin(p / 2))
Fc = np.abs(Fc)

F1_H = np.zeros_like(theta_rad)
kl_2 = (k * l) / 2
for i, th in enumerate(theta_rad):
    cos_term = np.cos(th)
    sin_th = np.sin(th)
    if abs(cos_term) < 1e-5:
        F1_H[i] = 0
    else:
        num = np.cos(kl_2 * sin_th) - np.cos(kl_2)
        den = (1 - sin_th**2) * (1 - np.cos(kl_2))
        F1_H[i] = num / den if den != 0 else 1.0
F1_H = np.abs(F1_H)

F_H = F1_H * Fc
F_H_norm = F_H / np.max(F_H)

# В площині E (решітка не діє уздовж цієї осі, працює тільки одиночна щілина у площині E ~ константа)

F_E_norm = np.ones_like(theta_deg)

#ПЛОЩИНА H
indices_above_0707 = np.where(F_H_norm >= 0.707)[0]
theta_0707_range = theta_deg[indices_above_0707]
beamwidth_0707 = np.max(theta_0707_range) - np.min(theta_0707_range)

from scipy.signal import find_peaks
peaks, _ = find_peaks(F_H_norm, height=0)
peak_heights = F_H_norm[peaks]
sorted_peaks = np.sort(peak_heights)
if len(sorted_peaks) > 1:
    sll = sorted_peaks[-2]
    sll_db = 20 * np.log10(sll)
else:
    sll = 0
    sll_db = -np.inf

print(f"--- Результати розрахунку для Варіанту 7 ---")
print(f"Ширина головної пелюстки (2Δθ) на рівні 0.707: {beamwidth_0707:.2f}°")
print(f"Рівень бічних пелюсток (відносний): {sll:.3f}")
print(f"Рівень бічних пелюсток (у дБ): {sll_db:.2f} дБ")

plt.figure(figsize=(10, 6))
plt.plot(theta_deg, F_H_norm, label='Площина H (вдовж решітки)', color='blue', lw=2)
plt.plot(theta_deg, F_E_norm, label='Площина E (поперечна)', color='red', linestyle='--', lw=1.5)
plt.axhline(y=0.707, color='green', linestyle=':', label='Рівень 0.707 (половинна потужність)')
plt.title('Нормована діаграма спрямованості ХвЩА (Варіант №7)', fontsize=14)
plt.xlabel('Кут θ, градуси', fontsize=12)
plt.ylabel('F(θ) нормована', fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlim([-90, 90])
plt.ylim([0, 1.05])
plt.legend(loc='upper right')
plt.savefig('ДС ХвЩА.png', dpi=300, bbox_inches='tight')
plt.show()