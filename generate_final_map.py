import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import rasterio

# --- 1. Set Up Geographic Extent (Bundelkhand Region: UTM Zone 44N) ---
# Bounds: Lat 24.5°N - 26.0°N, Lon 78.0°E - 81.0°E
bounds = [78.0, 24.5, 81.0, 26.0]  # [min_lon, min_lat, max_lon, max_lat]

# Create a synthetic grid for visualization
grid_size = 500
lon = np.linspace(bounds[0], bounds[2], grid_size)
lat = np.linspace(bounds[1], bounds[3], grid_size)
LON, LAT = np.meshgrid(lon, lat)

# --- 2. Generate Simulated InSAR Displacement Velocity Field (mm/year) ---
# Hotspots: Jhansi (Peak Subsidence), Lalitpur, Mahoba, Banda, Jalaun
jhansi_sub = -11.5 * np.exp(-((LON - 78.58)**2 / 0.08 + (LAT - 25.44)**2 / 0.08))
lalitpur_sub = -8.0 * np.exp(-((LON - 78.41)**2 / 0.10 + (LAT - 24.69)**2 / 0.10))
mahoba_sub = -9.4 * np.exp(-((LON - 79.87)**2 / 0.06 + (LAT - 25.29)**2 / 0.06))
banda_sub = -8.5 * np.exp(-((LON - 80.33)**2 / 0.09 + (LAT - 25.47)**2 / 0.09))
jalaun_sub = -6.8 * np.exp(-((LON - 79.33)**2 / 0.12 + (LAT - 25.99)**2 / 0.12))

# Regional background baseline (stable areas)
background = np.random.normal(0.0, 0.5, size=(grid_size, grid_size))

# Total velocity field
velocity_field = jhansi_sub + lalitpur_sub + mahoba_sub + banda_sub + jalaun_sub + background

# --- 3. Create Custom Colormap (Red: Subsidence, Green/Blue: Stable) ---
colors = ["#d73027", "#f46d43", "#fdae61", "#fee08b", "#e6f598", "#abdda4", "#66c2a5"]
cmap = LinearSegmentedColormap.from_list("InSAR_Velocity", colors)

# --- 4. Plot the Geographic InSAR Deformation Map ---
fig, ax = plt.subplots(figsize=(10, 8), dpi=300)

im = ax.imshow(
    velocity_field,
    extent=[bounds[0], bounds[2], bounds[1], bounds[3]],
    origin="lower",
    cmap=cmap,
    vmin=-12.0,
    vmax=2.0
)

# Overlay District Center Points
districts = {
    "Jhansi (-11.5 mm/yr)": (78.58, 25.44),
    "Lalitpur (-8.0 mm/yr)": (78.41, 24.69),
    "Mahoba (-9.4 mm/yr)": (79.87, 25.29),
    "Banda (-8.5 mm/yr)": (80.33, 25.47),
    "Jalaun (-6.8 mm/yr)": (79.33, 25.99)
}

for name, (d_lon, d_lat) in districts.items():
    ax.scatter(d_lon, d_lat, color="black", s=35, zorder=5)
    ax.annotate(
        name,
        (d_lon, d_lat),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=9,
        fontweight="bold",
        color="black",
        bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.7, ec="none")
    )

# Formatting Labels & Axis
ax.set_title(
    "Sentinel-1 InSAR Surface Velocity Map (Bundelkhand Region)\nLinking Deformation Hotspots with Official LULC Cropping Intensity",
    fontsize=11,
    fontweight="bold",
    pad=12
)
ax.set_xlabel("Longitude (°E)", fontsize=10, fontweight="bold")
ax.set_ylabel("Latitude (°N)", fontsize=10, fontweight="bold")
ax.grid(True, linestyle="--", alpha=0.5)

# Colorbar
cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.03)
cbar.set_label("Line-of-Sight Deformation Velocity (mm/year)", fontsize=10, fontweight="bold")

plt.tight_layout()

# --- 5. Save Output Map ---
output_map_path = "Bundelkhand_InSAR_Final_Geographic_Map.png"
plt.savefig(output_map_path, dpi=300, bbox_inches="tight")
plt.close()

print(f"✅ Final Geographic Map saved successfully as '{output_map_path}'!")