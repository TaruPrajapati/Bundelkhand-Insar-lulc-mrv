# Bundelkhand-Insar-lulc-mrv
An InSAR &amp; LULC-Based MRV Framework
# 🛰️ Bundelkhand InSAR & LULC Land Subsidence Assessment

> **An InSAR and LULC-Based MRV Framework for Monitoring Land Subsidence in Bundelkhand: Supporting Evidence-Based Land & Resource Policy**

---

## 📌 Executive Summary

This project establishes an empirical, spatial **Measurement, Reporting, and Verification (MRV) framework** that isolates intensive agricultural groundwater extraction as the primary driver of localized land subsidence across the semi-arid Bundelkhand region of Uttar Pradesh (covering Jhansi, Lalitpur, Mahoba, Banda, and Jalaun). 

By integrating ground-truth **India-WRIS Land Use & Land Cover (LULC 2017–18)** data with **Sentinel-1 InSAR surface displacement rasters**, this study proves that continuous multi-season farming causes significant aquitard consolidation and surface sinking, peaking at **-11.5 mm/yr in Jhansi**.

---

## 🚨 The Problem

* **Unmonitored Aquifer Compression:** Intensive year-round irrigation (Double/Triple cropping) continuously extracts deep groundwater, causing clay-rich alluvial aquitards to compact and permanently lose structural integrity.
* **Policy Blindspots:** Traditional water monitoring relies on sparse point-based borewells, failing to capture continuous spatial deformation and surface sinking patterns.
* **Severe Hotspots:** High agricultural intensity areas like Jhansi (-11.5 mm/yr) and Mahoba (-9.4 mm/yr) face heightened long-term land degradation and infrastructure risks.

---

## 💡 The Solution

This project introduces an integrated **Geospatial MRV Framework** that links dynamic satellite radar interferometry with official land-use data:

1. **Spatial Isolation of Drivers:** By mapping InSAR deformation against land cover, the framework proves that land subsidence is directly tied to intensive agriculture rather than regional tectonic shifts.
2. **Natural Buffer Verification:** It highlights how natural forests (e.g., in Lalitpur) serve as critical aquifer recharge zones, capping subsidence despite high agricultural activity.
3. **Data-Driven Interventions:** It provides local governments with actionable spatial data to prioritize crop diversification, managed aquifer recharge, and water conservation where it is needed most.

---

## 📊 Key Findings & Integrated Data

| District | Primary LULC Class | Secondary LULC Class | Fallow / Control Coverage | Max InSAR Subsidence | Risk Tier |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Jhansi** | Double / Triple Crop (~1,750 km²) | Rabi Crop (~750 km²) | Current Fallow (~600 km²) | **-11.5 mm/yr** | 🔴 **CRITICAL** |
| **Lalitpur** | Double / Triple Crop (~2,250 km²) | Rabi Crop (~1,050 km²) | Deciduous Forest (~400 km²) | **-8.0 mm/yr** | 🟠 **HIGH** |
| **Mahoba** | Rabi Crop (~1,050 km²) | Double / Triple Crop (~650 km²) | Kharif Crop (~500 km²) | **-9.4 mm/yr** | 🟠 **HIGH** |
| **Banda** | Double / Triple Crop (~1,500 km²) | Rabi Crop (~1,200 km²) | Current Fallow (~400 km²) | **-8.5 mm/yr** | 🟠 **HIGH** |
| **Jalaun** | Rabi Crop (~2,100 km²) | Double / Triple Crop (~1,100 km²) | Current Fallow (~300 km²) | **-6.8 mm/yr** | 🟡 **MODERATE** |

> *All LULC figures sourced directly from official NRSC / India-WRIS 2017–18 statistics.*

---

## 🖼️ Visualizations & Maps

| InSAR Surface Velocity Heatmap | LULC Cropping Intensity vs. Subsidence |
| :---: | :---: |
| <img width="2826" height="1948" alt="Bundelkhand_InSAR_Final_Geographic_Map" src="https://github.com/user-attachments/assets/fbd905b9-2f8a-4d6d-8e7f-738c39bd5dd0" />
 | <img width="900" height="500" alt="LULC-VS_INSAR" src="https://github.com/user-attachments/assets/b2d5475d-32e4-44ce-9c2d-611ad41b038b" />
 |

| Regional Displacement Overlay |
| :---: |
| <img width="1536" height="754" alt="Figure_1_-_timeseries_demErr" src="https://github.com/user-attachments/assets/7f65dc7c-d15b-40f5-b6f0-9e0787a55712" />
<img width="1536" height="754" alt="Cumulative_Displacement_Map" src="https://github.com/user-attachments/assets/4ebd4637-f0fb-4a32-b2d4-64a022471708" />
 |

---
## 🏗️ The MRV Framework Structure

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 MRV FRAMEWORK ARCHITECTURE                                        │
├───────────────────┬───────────────────────────────────────────────────────────────────────────────┤
│ M - MONITORING    │ • Continuous Sentinel-1 C-band SAR time-series acquisition (12-day orbit)     │
│                   │ • Small Baseline Subset (SBAS) time-series deformation inversion              │
│                   │ • Line-of-Sight (LOS) velocity mapping (mm/yr) to detect active surface sink │
├───────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│ R - REPORTING     │ • District-level deformation velocity heatmaps (Jhansi, Lalitpur, etc.)       │
│                   │ • Dual-axis cropping intensity vs. InSAR subsidence rate graphs               │
│                   │ • Dynamic spatial hazard categorization (Critical / High / Moderate Tiers)    │
├───────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│ V - VERIFICATION  │ • Cross-referencing InSAR velocity hotspots against official India-WRIS NRSC  │
│                   │   (2017–18) LULC ground-truth crop layers                             │
│                   │ • Ground control validation using stable baselines (Built-up areas & Forests) │
└───────────────────┴───────────────────────────────────────────────────────────────────────────────┘
```

---

## UN Alignment with UN Sustainable Development Goals (SDGs)

This framework directly supports the **UN 2030 Agenda for Sustainable Development** by using satellite remote sensing to monitor localized environmental degradation and guide resilient land management:

* **SDG 6: Clean Water and Sanitation**
  * **Target 6.6:** *Protect and restore water-related ecosystems.*
  * **Application:** Provides an empirical monitoring mechanism to detect severe groundwater over-extraction and prevent permanent aquifer aquitard destruction across semi-arid agricultural regions.

* **SDG 11: Sustainable Cities and Communities**
  * **Target 11.5:** *Reduce the adverse effects of natural disasters.*
  * **Application:** Uses InSAR hazard tiering (Critical / High / Moderate) to identify land subsidence hotspots early, mitigating structural risks to rural civil infrastructure and housing.

* **SDG 13: Climate Action**
  * **Target 13.3:** *Build knowledge and capacity to meet climate change.*
  * **Application:** Equips regional decision-makers with actionable, high-resolution Earth Observation (EO) data to build climate-resilient water management policies under growing drought pressure.

* **SDG 15: Life on Land**
  * **Target 15.3:** *End land degradation and restore degraded land.*
  * **Application:** Integrates ground-truth LULC data to prove the protective role of natural forest buffers against land compaction, supporting evidence-based land conservation strategies.

---
## 🌿 Policy & Resource Recommendations

1. **Crop Intensity Regulation:** Shift high-density double/triple cropping zones in Jhansi and Lalitpur toward low-water pulses and oilseeds during summer.
2. **Targeted Artificial Recharge:** Direct state funding (*Jal Shakti Abhiyan*) to construct check dams and percolation tanks directly over active deformation hotspots.
3. **GIS Portal Integration:** Integrate dynamic InSAR velocity rasters with national water portals (India-WRIS) for real-time risk surveillance.
