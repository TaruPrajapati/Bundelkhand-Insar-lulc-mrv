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
| ![InSAR Surface Velocity Map](assets/surface_velocity_map.png) | ![LULC vs InSAR Chart](assets/lulc_vs_insar_graph.png) |

| Regional Displacement Overlay |
| :---: |
| ![Displacement Mapping](assets/displacement_mapping.png) |

---

## 🌿 Policy & Resource Recommendations

1. **Crop Intensity Regulation:** Shift high-density double/triple cropping zones in Jhansi and Lalitpur toward low-water pulses and oilseeds during summer.
2. **Targeted Artificial Recharge:** Direct state funding (*Jal Shakti Abhiyan*) to construct check dams and percolation tanks directly over active deformation hotspots.
3. **GIS Portal Integration:** Integrate dynamic InSAR velocity rasters with national water portals (India-WRIS) for real-time risk surveillance.
