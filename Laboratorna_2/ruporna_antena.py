import numpy as np
import matplotlib.pyplot as plt
import math

#(варіант 7)

lambd = 0.031   # м
a = 0.11        # м
b = 0.11        # м

theta_deg = []
FH = []
F1h = []
FC = []

max_x = []
max_y = []
min_x = []
min_y = []

theta_half = 0


for teta in np.arange(0.001, np.pi/2, 0.0005):

    theta = math.degrees(teta)

    f1 = abs((1 + np.cos(teta)) / 2)

    x = (np.pi * b * np.sin(teta)) / lambd
    if x != 0:
        fc = abs(np.sin(x) / x)
    else:
        fc = 1

    fh = f1 * fc

    theta_deg.append(theta)
    F1h.append(f1)
    FC.append(fc)
    FH.append(fh)

    if 0.707 < fh < 0.708:
        theta_half = theta

for i in range(1, len(FH)-1):
    if FH[i] > FH[i-1] and FH[i] > FH[i+1]:
        max_x.append(theta_deg[i])
        max_y.append(FH[i])

    if FH[i] < FH[i-1] and FH[i] < FH[i+1]:
        min_x.append(theta_deg[i])
        min_y.append(0)


plt.figure(figsize=(12, 6))

plt.plot(theta_deg, F1h, label=r"$F_{1h}(\theta)$")
plt.plot(theta_deg, FC, label=r"$F_{C}(\theta)$")
plt.plot(theta_deg, FH, label=r"$F_{H}(\theta)$", color="green")

plt.axhline(0.707, linestyle="--", color="red")
plt.axvline(theta_half, linestyle="--", color="red")

plt.scatter(theta_half, 0.707, color="red", zorder=5)
plt.annotate(f"(0.707, {theta_half:.2f}°)",
             xy=(theta_half, 0.707),
             xytext=(theta_half+5, 0.75),
             arrowprops=dict(arrowstyle="->"))

plt.scatter(max_x, max_y, color="black", label=r"$\theta_{max}$ H")
plt.scatter(min_x, min_y, color="blue", label=r"$\theta_{min}$ H")

plt.title(f"ДС пірамідального рупору в площині H з параметрами: λ = {lambd} м, Ap = {a}×{b} м")
plt.xlabel("θ (градуси)")
plt.ylabel("|Fh(θ)|, |F1h(θ)|, |Fc(θ)|")

plt.xlim(0, 90)
plt.ylim(0, 1.05)

plt.grid(True, linestyle=":", linewidth=0.5)
plt.legend()

plt.show()

# ГРАФІК ДЛЯ E-ПЛОЩИНИ

theta_deg_E = []
FE = []

max_x_E = []
max_y_E = []
min_x_E = []
min_y_E = []

theta_half_E = 0

for teta in np.arange(0.001, np.pi/2, 0.0005):

    theta = math.degrees(teta)

    x = (np.pi * a * np.sin(teta)) / lambd
    if x != 0:
        fe = abs(np.sin(x) / x)
    else:
        fe = 1

    theta_deg_E.append(theta)
    FE.append(fe)

    if 0.707 < fe < 0.708:
        theta_half_E = theta

# максимуми / мінімуми
for i in range(1, len(FE)-1):
    if FE[i] > FE[i-1] and FE[i] > FE[i+1]:
        max_x_E.append(theta_deg_E[i])
        max_y_E.append(FE[i])

    if FE[i] < FE[i-1] and FE[i] < FE[i+1]:
        min_x_E.append(theta_deg_E[i])
        min_y_E.append(0)

# графік
plt.figure(figsize=(12, 6))

plt.plot(theta_deg_E, FE, label=r"$F_E(\theta)$", color="green")

plt.axhline(0.707, linestyle="--", color="red")
plt.axvline(theta_half_E, linestyle="--", color="red")

plt.scatter(theta_half_E, 0.707, color="red")
plt.annotate(f"(0.707, {theta_half_E:.2f}°)",
             xy=(theta_half_E, 0.707),
             xytext=(theta_half_E+5, 0.75),
             arrowprops=dict(arrowstyle="->"))

plt.scatter(max_x_E, max_y_E, color="black", label=r"$\theta_{max}$ E")
plt.scatter(min_x_E, min_y_E, color="blue", label=r"$\theta_{min}$ E")

plt.title(f"ДС пірамідального рупору в площині E\nλ = {lambd} м, Ap = {a}×{b} м")
plt.xlabel("θ (градуси)")
plt.ylabel("|FE(θ)|")

plt.xlim(0, 90)
plt.ylim(0, 1.05)

plt.grid(True, linestyle=":", linewidth=0.5)
plt.legend()

plt.show()

print("Варіант = 7")
print(f"Довжина хвилі = {lambd} м")
print(f"Розмір розкриву рупора a*b = {a} × {b} м")
print(f"Ширина головної пелюстки H = {2*theta_half:.2f}°")
print(f"Ширина головної пелюстки E = {2*theta_half_E:.2f}°")

print("\n===== ТАБЛИЦЯ (H-площина) =====")

print("\nНулі ДС:")
print("-----------------")
print("| № |   θ   | F(θ) |")
print("-----------------")
for i in range(min(3, len(min_x))):
    print(f"| {i+1} | {min_x[i]:5.2f} |  0  |")
print("-----------------")

print("\nМаксимуми ДС:")
print("-----------------")
print("| № |   θ   | F(θ) |")
print("-----------------")
for i in range(min(3, len(max_x))):
    print(f"| {i+1} | {max_x[i]:5.2f} | {max_y[i]:.2f} |")
print("-----------------")


print("\n===== ТАБЛИЦЯ (E-площина) =====")

print("\nНулі ДС:")
print("-----------------")
print("| № |   θ   | F(θ) |")
print("-----------------")
for i in range(min(3, len(min_x_E))):
    print(f"| {i+1} | {min_x_E[i]:5.2f} |  0  |")
print("-----------------")

print("\nМаксимуми ДС:")
print("-----------------")
print("| № |   θ   | F(θ) |")
print("-----------------")
for i in range(min(3, len(max_x_E))):
    print(f"| {i+1} | {max_x_E[i]:5.2f} | {max_y_E[i]:.2f} |")
print("-----------------")