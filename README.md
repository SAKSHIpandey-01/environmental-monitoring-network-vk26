# AI-Powered Environmental Monitoring Network

**Vishwakarma Awards 2026-27 | Stage 2 | Application ID: VK26-IITI-AHM-0602**
Theme: AI in Hardware & Manufacturing | Sub-theme: Edge AI & On-Chip Processing

Solar-powered LoRa edge-AI nodes for early warning of floods, forest fires and air pollution.

## Status
**Design stage.** This repository holds the Stage 2 submission and the design documents derived from it.
Fabrication, firmware, TinyML training and bench/field test data will be committed from November 2026
following the roadmap in the submission. All performance values in the submission are design-stage estimates.

## Repository layout
| Folder | Contents |
|---|---|
| `docs/` | Stage 2 submission (PPT/PDF) |
| `hardware/` | Itemized BOM (`BOM.xlsx`) |
| `firmware/` | `pin_config.h`: ESP32 pin map from the submission's pinout slide |
| `calculations/` | Wind-load screening calc, power/runtime estimate (Python), plot |

## Node summary (from the submission)
- Controller: ESP32-WROOM-32, deep-sleep duty cycle (5 min normal, 30 s alert mode)
- Sensors: DHT22, PMS5003, MQ-135, JSN-SR04T (water level), NEO-6M GPS
- Uplink: RFM95W (SX1276) LoRa, 865-867 MHz, to an ESP32 + LoRa + GSM gateway
- Power: 6 V 3 W solar, TP4056, 2x 18650, MT3608 (5 V), AMS1117 (3.3 V)
- Mechanical: IP65 ABS enclosure, radiation shield, 2 m GI mast (32 NB)
- Estimated node cost: Rs 6,820 (BOM v2, starred prices are estimates)

## Calculations
```
python calculations/wind_load.py      # mast bending stress and factor of safety
python calculations/power_budget.py   # average current, runtime, solar margin
```
Both are screening calculations, not FEA or measured results.

## Notes
- Native CAD (.STEP/.SLDPRT), KiCad files, firmware and `.tflite` models are not yet in this repository.
  They will be added as they are created; commit history is the record of progress.
- Some documents here were drafted with AI assistance from the team's Stage 2 submission and reviewed by the team.

## Team
Sakshi Pandey (team lead), Prachi Nigam, Shivam, Swarnim, Rishikesh
