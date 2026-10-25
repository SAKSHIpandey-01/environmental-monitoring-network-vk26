"""Mast wind-load screening calculation (not FEA).
Inputs follow the Stage 2 submission, slide 11. Run: python wind_load.py
"""
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

Q_DESIGN = 1500.0        # Pa, 0.5*rho*v^2 at 50 m/s rounded as in the submission
V_DESIGN = 50.0          # m/s design wind (site zone to be confirmed per IS 875 Part 3)
AREA = 0.032 + 0.021 + 0.015   # m^2: box + panel + shield
CD = 1.2
HEIGHT = 2.0             # m, lever arm to base (approximate)
OD, WALL = 42.4, 3.2     # mm, 32 NB GI pipe, medium class
YIELD = 210.0            # MPa, assumed

ID = OD - 2 * WALL
I = math.pi / 64 * (OD**4 - ID**4)     # mm^4
Z = I / (OD / 2)                       # mm^3

def stress_at(v):
    q = Q_DESIGN * (v / V_DESIGN) ** 2
    force = q * AREA * CD              # N
    moment = force * HEIGHT            # N.m
    return force, moment, moment * 1000 / Z   # MPa (N.mm / mm^3)

F, M, sigma = stress_at(V_DESIGN)
print(f"Area {AREA:.3f} m2 | Z = {Z/1000:.2f} cm3")
print(f"At {V_DESIGN:.0f} m/s: F = {F:.0f} N, M = {M:.0f} N.m, stress = {sigma:.1f} MPa, FoS = {YIELD/sigma:.2f}")

speeds = list(range(10, 71, 5))
stresses = [stress_at(v)[2] for v in speeds]
plt.figure(figsize=(7, 4))
plt.plot(speeds, stresses, marker="o", label="Bending stress at mast base")
plt.axhline(YIELD, color="red", linestyle="--", label=f"Assumed yield {YIELD:.0f} MPa")
plt.xlabel("Wind speed (m/s)"); plt.ylabel("Stress (MPa)")
plt.title("Mast base stress vs wind speed (hand calc, 32 NB GI)")
plt.grid(alpha=0.3); plt.legend(); plt.tight_layout()
plt.savefig("wind_load_plot.png", dpi=200)
