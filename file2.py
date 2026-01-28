import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Mineral Oil Cooling Simulation System")
st.write("This application simulates PC cooling using different cooling methods.")

# Sidebar inputs
st.sidebar.header("Input Parameters")

cpu_load = st.sidebar.slider("CPU Load (%)", 0, 100, 50)
gpu_load = st.sidebar.slider("GPU Load (%)", 0, 100, 40)
ambient_temp = st.sidebar.slider("Ambient Temperature (°C)", 20, 40, 25)

cooling_type = st.sidebar.selectbox(
    "Select Cooling Method",
    ("Air Cooling", "Liquid Cooling", "Mineral Oil Cooling")
)

# Cooling efficiency values (simulation constants)
if cooling_type == "Air Cooling":
    cooling_factor = 0.3
elif cooling_type == "Liquid Cooling":
    cooling_factor = 0.6
else:
    cooling_factor = 0.9

# Simulation button
if st.button("Run Simulation"):
    time = np.arange(0, 60, 1)  # 60 seconds simulation
    heat_generated = (cpu_load * 0.6 + gpu_load * 0.4)
    
    temperature = ambient_temp + heat_generated * cooling_factor * np.exp(-time / 30)

    # Display results
    st.subheader("Simulation Result")
    st.write(f"Final CPU Temperature: **{temperature[-1]:.2f} °C**")
    st.write(f"Cooling Method Used: **{cooling_type}**")

    # Plot graph
    fig, ax = plt.subplots()
    ax.plot(time, temperature)
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Temperature vs Time")

    st.pyplot(fig)

    # Efficiency display
    efficiency = cooling_factor * 100
    st.success(f"Cooling Efficiency: {efficiency:.0f}%")
