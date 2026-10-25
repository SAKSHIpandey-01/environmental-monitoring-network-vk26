"""Runtime and solar margin estimate. Mirrors the arithmetic on slide 7 of the Stage 2 submission.
Design-stage estimate, not a measurement. Run: python power_budget.py
"""
ACTIVE_MA, ACTIVE_S = 450.0, 30.0     # sensing + LoRa burst
SLEEP_MA, SLEEP_S = 1.0, 270.0
BATTERY_MAH = 5200.0                  # 2 x 2600 mAh in parallel
PANEL_W, PANEL_V = 3.0, 6.0
PEAK_SUN_H, DERATE = 4.5, 0.7

avg_ma = (ACTIVE_MA * ACTIVE_S + SLEEP_MA * SLEEP_S) / (ACTIVE_S + SLEEP_S)
runtime_h = BATTERY_MAH / avg_ma
load_ah_day = avg_ma * 24 / 1000
solar_ah_day = (PANEL_W / PANEL_V) * PEAK_SUN_H * DERATE   # TP4056 is a linear charger, so battery Ah ~ panel Ah

print(f"Average current: {avg_ma:.1f} mA")
print(f"Battery-only runtime: {runtime_h:.0f} h ({runtime_h/24:.1f} days)")
print(f"Load: {load_ah_day:.2f} Ah/day | Solar: {solar_ah_day:.2f} Ah/day | Margin: {solar_ah_day/load_ah_day:.2f}x")
