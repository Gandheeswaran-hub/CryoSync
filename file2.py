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

theme = st.sidebar.radio("🎨 Select Theme", ("Dark", "Light"))

# -------------------------------
# Theme Settings
# -------------------------------
if theme == "Dark":
    bg_gradient = "linear-gradient(135deg, #020617, #0f172a, #020617)"
    sidebar_bg = "linear-gradient(180deg, #020617, #0f172a)"
    text_color = "white"
    heading_color = "#38bdf8"
    graph_bg = "#020617"
    grid_color = "#334155"
else:
    bg_gradient = "linear-gradient(135deg, #f8fafc, #e0f2fe, #f8fafc)"
    sidebar_bg = "linear-gradient(180deg, #e5e7eb, #f8fafc)"
    text_color = "#020617"
    heading_color = "#2563eb"
    graph_bg = "white"
    grid_color = "#cbd5e1"

# -------------------------------
# Global CSS + Fonts + Effects
# -------------------------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Orbitron:wght@600;800&display=swap');

.stApp {{
    background: {bg_gradient};
    color: {text_color};
    font-family: 'Poppins', sans-serif;
}}

section[data-testid="stSidebar"] {{
    background: {sidebar_bg};
}}

.block-container {{
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 2rem;
}}

@keyframes glow {{
    0% {{ text-shadow: 0 0 10px #38bdf8; }}
    50% {{ text-shadow: 0 0 25px #22c55e; }}
    100% {{ text-shadow: 0 0 10px #38bdf8; }}
}}

.glow-title {{
    text-align: center;
    font-size: 3.2rem;
    font-weight: 900;
    font-family: 'Orbitron', sans-serif;
    background: linear-gradient(90deg, #38bdf8, #22c55e, #facc15, #ef4444);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 2.5s infinite alternate;
}}

.stButton > button {{
    background-color: {heading_color};
    color: white;
    border-radius: 12px;
    font-weight: bold;
    padding: 0.6rem 1.2rem;
}}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.markdown("### 📌 Navigation")
page = st.sidebar.radio("", ("Home", "Profile", "About Us", "Download", "Share"))

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Team Details")
st.sidebar.markdown("""
**Name:** Dhinagaran B  
**Email:** dhinagaranboopathi  
**GitHub:** [dhina-528](https://github.com/dhina-528)
""")

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "Home":

    st.markdown('<h1 class="glow-title">🧊 Mineral Oil Cooling Simulation System</h1>',
                unsafe_allow_html=True)

    st.write(
        "This simulation evaluates **PC cooling performance** using "
        "**temperature-based color gradients (Hot → Cold)**."
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

        factor = cooling_factors[cooling_type]
        time_steps = np.arange(0, 10, 1)
        base_temp = ambient_temp + (cpu_load + gpu_load) / 4
        temps = base_temp - (factor * time_steps * 3)

        # -------- Gradient Graph --------
        points = np.array([time_steps, temps]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        fig, ax = plt.subplots()
        norm = plt.Normalize(temps.min(), temps.max())
        lc = LineCollection(segments, cmap="coolwarm", norm=norm)
        lc.set_array(temps)
        lc.set_linewidth(4)
        ax.add_collection(lc)

        ax.set_xlim(time_steps.min(), time_steps.max())
        ax.set_ylim(temps.min() - 2, temps.max() + 2)
        ax.set_xlabel("Time (seconds)", color=text_color)
        ax.set_ylabel("Temperature (°C)", color=text_color)
        ax.set_title(f"Temperature Gradient using {cooling_type}",
                     color=heading_color)

        ax.tick_params(colors=text_color)
        ax.grid(True, linestyle="--", color=grid_color, alpha=0.6)
        fig.patch.set_facecolor(graph_bg)
        ax.set_facecolor(graph_bg)

        cbar = fig.colorbar(lc, ax=ax)
        cbar.set_label("Temperature (°C)")
        cbar.ax.yaxis.set_tick_params(color=text_color)

        st.pyplot(fig)

        # -------- Performance Metrics --------
        st.success(f"Final Temperature: **{temps[-1]:.2f} °C**")

        initial_temp = temps[0]
        final_temp = temps[-1]
        temp_drop = initial_temp - final_temp
        time_duration = time_steps[-1] - time_steps[0]
        cooling_rate = temp_drop / time_duration
        efficiency = (temp_drop / initial_temp) * 100
        stability_index = np.std(temps)

        st.markdown("## 📈 Performance Metrics")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Efficiency (%)", f"{efficiency:.2f}")
        m2.metric("Time Duration (sec)", f"{time_duration}")
        m3.metric("Cooling Rate (°C/sec)", f"{cooling_rate:.2f}")
        m4.metric("Stability Index", f"{stability_index:.2f}")

        # -------- Rating --------
        st.markdown("### 🏆 System Performance Rating")

        if efficiency >= 30:
            st.success("🔥 Excellent Cooling Performance")
        elif efficiency >= 20:
            st.info("⚙️ Good Cooling Performance")
        else:
            st.warning("❄️ Moderate Cooling Performance")

        # -------- Explanation --------
        st.markdown("### 🧠 Technical Interpretation")
        st.write(f"""
        - Cooling efficiency of **{efficiency:.2f}%** achieved over **{time_duration} seconds**
        - Cooling rate of **{cooling_rate:.2f} °C/sec** indicates heat dissipation speed
        - Lower stability index confirms smoother thermal behavior
        """)

# -------------------------------
# PROFILE PAGE
# -------------------------------
elif page == "Profile":
    st.title("👤 Profile")
    st.write("""
    **Project Lead:** Dhinagaran B  
    **Role:** Simulation & Visualization  
    **Special Feature:** Performance Metrics & Thermal Analysis
    """)

# -------------------------------
# ABOUT US PAGE
# -------------------------------
elif page == "About Us":

    st.markdown('<h1 class="glow-title">ℹ️ About This Project</h1>',
                unsafe_allow_html=True)

    st.markdown("### 📌 Project Title")
    st.markdown("""
    **Simulation and Performance Analysis of Mineral Oil Cooling  
    in Modern Computer Systems**
    """)

    st.markdown("### 🧪 Project Description")
    st.markdown("""
    Physical testing of **mineral oil immersion cooling systems** is
    costly, complex, and difficult to perform in academic environments.

    Currently, there is **no simple and user-friendly software tool**
    available to:
    - Simulate mineral oil cooling behavior  
    - Compare it with traditional cooling techniques  
    - Predict temperature changes under different CPU and GPU workloads  

    Hence, this project proposes a **software-based simulation system**
    that safely analyzes cooling efficiency without requiring
    any physical hardware setup.
    """)

    st.markdown("### 🎯 Project Objectives")
    st.markdown("""
    The main objectives of this project are:

    ✔️ To design a **software simulation model** for mineral oil cooling  
    ✔️ To calculate **heat generation and heat dissipation** dynamically  
    ✔️ To compare **Air Cooling, Liquid Cooling, and Mineral Oil Cooling**  
    ✔️ To visualize **temperature behavior using gradient-based graphs**  
    ✔️ To help users understand **cooling efficiency without physical testing**
    """)

    st.markdown("### 🚀 Outcome & Benefits")
    st.success("""
    - Reduces cost and risk compared to physical experimentation  
    - Provides clear thermal visualization for academic learning  
    - Useful for project demonstrations, viva, and research analysis  
    """)

# -------------------------------
# DOWNLOAD PAGE
# -------------------------------
elif page == "Download":
    st.title("⬇️ Download")
    st.warning("Project report and source files coming soon")

# -------------------------------
# SHARE PAGE
# -------------------------------
elif page == "Share":
    st.title("🔗 Share Project")
    st.code("https://github.com/dhina-528")


