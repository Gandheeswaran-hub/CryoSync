import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Mineral Oil Cooling System",
    page_icon="🧊",
    layout="wide"
)

# -------------------------------
# Sidebar: Theme Switch
# -------------------------------
st.sidebar.title("🧊 Cooling System")

theme = st.sidebar.radio(
    "🎨 Select Theme",
    ("Dark", "Light")
)

# -------------------------------
# Theme Settings
# -------------------------------
if theme == "Dark":
    bg_color = "#020617"
    sidebar_bg = "#020617"
    text_color = "white"
    heading_color = "#38bdf8"
    graph_bg = "#020617"
    grid_color = "#334155"
else:
    bg_color = "#f8fafc"
    sidebar_bg = "#e5e7eb"
    text_color = "#020617"
    heading_color = "#2563eb"
    graph_bg = "white"
    grid_color = "#cbd5e1"

# -------------------------------
# Apply CSS
# -------------------------------
st.markdown(f"""
<style>
.stApp {{
    background-color: {bg_color};
    color: {text_color};
}}
section[data-testid="stSidebar"] {{
    background-color: {sidebar_bg};
}}
h1, h2, h3 {{
    color: {heading_color};
}}
.stButton > button {{
    background-color: {heading_color};
    color: white;
    border-radius: 10px;
    font-weight: bold;
}}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.markdown("### 📌 Navigation")
page = st.sidebar.radio(
    "",
    ("Home", "Profile", "About Us", "Download", "Share")
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Team Details")
st.sidebar.markdown(
    """
    **Name:** Dhinagaran B  
    **Email:** dhinagaranboopathi  
    **GitHub:** [dhina-528](https://github.com/dhina-528)
    """
)

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "Home":
    st.title("🧊 Mineral Oil Cooling Simulation System")

    st.write(
        "This simulation visualizes **PC cooling performance** using a "
        "**temperature-based color gradient (Hot → Cold)**."
    )

    st.subheader("🔧 Input Parameters")

    col1, col2, col3 = st.columns(3)

    with col1:
        cpu_load = st.number_input("CPU Load (%)", 0, 100, 50)
    with col2:
        gpu_load = st.number_input("GPU Load (%)", 0, 100, 40)
    with col3:
        ambient_temp = st.number_input("Ambient Temperature (°C)", 20, 50, 25)

    cooling_type = st.selectbox(
        "Cooling Method",
        ("Air Cooling", "Liquid Cooling", "Mineral Oil Cooling")
    )

    run = st.button("▶ Run Simulation")

    cooling_factors = {
        "Air Cooling": 0.3,
        "Liquid Cooling": 0.6,
        "Mineral Oil Cooling": 0.9
    }

    if run:
        st.subheader("📊 Temperature Gradient Visualization")

        cooling_factor = cooling_factors[cooling_type]
        time_steps = np.arange(0, 10, 1)
        base_temp = ambient_temp + (cpu_load + gpu_load) / 4
        temperatures = base_temp - (cooling_factor * time_steps * 3)

        # -------------------------------
        # TEMPERATURE GRADIENT GRAPH
        # -------------------------------
        points = np.array([time_steps, temperatures]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        fig, ax = plt.subplots()

        norm = plt.Normalize(temperatures.min(), temperatures.max())
        lc = LineCollection(
            segments,
            cmap="coolwarm",   # 🔴 hot → 🔵 cold
            norm=norm
        )
        lc.set_array(temperatures)
        lc.set_linewidth(4)

        ax.add_collection(lc)

        ax.set_xlim(time_steps.min(), time_steps.max())
        ax.set_ylim(temperatures.min() - 2, temperatures.max() + 2)

        ax.set_xlabel("Time (seconds)", color=text_color)
        ax.set_ylabel("Temperature (°C)", color=text_color)
        ax.set_title(
            f"Temperature Gradient using {cooling_type}",
            color=heading_color
        )

        ax.tick_params(colors=text_color)
        ax.grid(True, linestyle="--", color=grid_color, alpha=0.6)

        fig.patch.set_facecolor(graph_bg)
        ax.set_facecolor(graph_bg)

        # Colorbar
        cbar = fig.colorbar(lc, ax=ax)
        cbar.set_label("Temperature (°C)")
        cbar.ax.yaxis.set_tick_params(color=text_color)

        st.pyplot(fig)

        st.success(
            f"Final Temperature: **{temperatures[-1]:.2f} °C**"
        )

# -------------------------------
# PROFILE PAGE
# -------------------------------
elif page == "Profile":
    st.title("👤 Profile")
    st.write(
        """
        **Project Lead:** Dhinagaran B  
        **Role:** Simulation & Visualization  
        **Special Feature:** Temperature Gradient Mapping
        """
    )

# -------------------------------
# ABOUT US PAGE
# -------------------------------
elif page == "About Us":
    st.title("ℹ️ About This Project")
    st.markdown(
        """
        ### 🌡️ Visualization Concept
        - Red indicates high temperature
        - Blue indicates low temperature
        - Gradient shows cooling progression clearly

        ### 🎯 Benefit
        Makes thermal behavior **intuitive and easy to understand**
        during demonstrations and viva.
        """
    )

# -------------------------------
# DOWNLOAD PAGE
# -------------------------------
elif page == "Download":
    st.title("⬇️ Download")
    st.warning("Project documents coming soon")

# -------------------------------
# SHARE PAGE
# -------------------------------
elif page == "Share":
    st.title("🔗 Share Project")
    st.code("https://github.com/dhina-528")


