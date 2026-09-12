import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="AI-LEW-RMS", layout="wide")

st.title("🏔️ AI-LEW-RMS Dashboard")
st.subheader("Landslide Early Detection & Risk Management System | Team: The Bugs Slayers (VCDH-18)")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", ["Dashboard", "Analytics", "Alerts", "Settings"])

# ============== DASHBOARD PAGE ==============
if page == "Dashboard":
    st.header("📊 Real-time Monitoring Dashboard")
    
    # Generate simulated sensor data
    soil_moisture = random.uniform(60, 90)
    rainfall_rate = random.uniform(20, 60)
    tilt_angle = random.uniform(5, 20)
    temperature = random.uniform(20, 35)
    
    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🌊 Soil Moisture", f"{soil_moisture:.1f}%", "+5%", delta_color="inverse")
    col2.metric("🌧️ Rainfall Rate", f"{rainfall_rate:.1f} mm/h", "+12 mm/h")
    col3.metric("📐 Tilt Angle (MPU6050)", f"{tilt_angle:.1f}°", "+2.1°", delta_color="inverse")
    col4.metric("🌡️ Temperature", f"{temperature:.1f}°C", "+2°C")
    
    # Risk Score Calculation
    st.header("⚠️ Multi-Evidence Risk Score")
    risk_score = int((soil_moisture * 0.3) + (rainfall_rate * 0.4) + (tilt_angle * 0.3))
    
    # Color-coded progress bar
    if risk_score > 70:
        st.error(f"🚨 HIGH RISK WARNING: Score {risk_score}/100 - Immediate Action Required!")
    elif risk_score > 50:
        st.warning(f"⚠️ MODERATE RISK: Score {risk_score}/100 - Monitor Closely")
    else:
        st.success(f"✅ LOW RISK: Score {risk_score}/100 - Safe Zone")
    
    st.progress(risk_score / 100)
    
    # Telemetry Stream
    st.header("📈 Real-time Telemetry Stream")
    
    # Generate time series data
    dates = [datetime.now() - timedelta(minutes=i) for i in range(20, 0, -1)]
    telemetry_data = pd.DataFrame({
        'Time': dates,
        'Soil Moisture (%)': [random.uniform(60, 90) for _ in range(20)],
        'Rainfall (mm/h)': [random.uniform(20, 60) for _ in range(20)],
        'Tilt Angle (°)': [random.uniform(5, 20) for _ in range(20)]
    })
    
    st.line_chart(telemetry_data.set_index('Time'))
    
    # Location Map (Placeholder)
    st.header("🗺️ Monitoring Locations")
    locations_df = pd.DataFrame({
        'Location': ['Zone A', 'Zone B', 'Zone C', 'Zone D'],
        'Latitude': [28.7041, 28.7150, 28.7200, 28.7100],
        'Longitude': [77.1025, 77.1150, 77.1200, 77.1050],
        'Risk Level': ['High', 'Moderate', 'Low', 'Moderate']
    })
    st.map(locations_df[['Latitude', 'Longitude']])
    
    # Recent Data Table
    st.header("📋 Recent Sensor Readings")
    recent_data = pd.DataFrame({
        'Timestamp': [datetime.now() - timedelta(minutes=i) for i in range(5)],
        'Soil Moisture (%)': [random.uniform(60, 90) for _ in range(5)],
        'Rainfall (mm/h)': [random.uniform(20, 60) for _ in range(5)],
        'Tilt Angle (°)': [random.uniform(5, 20) for _ in range(5)],
        'Temperature (°C)': [random.uniform(20, 35) for _ in range(5)]
    })
    st.dataframe(recent_data, use_container_width=True)

# ============== ANALYTICS PAGE ==============
elif page == "Analytics":
    st.header("📊 Advanced Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Risk Distribution")
        risk_categories = ['Low', 'Moderate', 'High', 'Critical']
        risk_counts = [15, 25, 35, 10]
        fig = go.Figure(data=[go.Bar(x=risk_categories, y=risk_counts, marker_color=['green', 'yellow', 'orange', 'red'])])
        fig.update_layout(title="Risk Level Distribution", height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Rainfall vs Tilt Correlation")
        rainfall_data = [random.uniform(20, 60) for _ in range(30)]
        tilt_data = [random.uniform(5, 20) for _ in range(30)]
        fig = go.Figure(data=[go.Scatter(x=rainfall_data, y=tilt_data, mode='markers', marker=dict(size=8, color='blue'))])
        fig.update_layout(title="Rainfall vs Tilt Angle", xaxis_title="Rainfall (mm/h)", yaxis_title="Tilt Angle (°)", height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Historical Risk Trends (30 Days)")
    days = pd.date_range(end=datetime.now(), periods=30)
    historical_risk = pd.DataFrame({
        'Date': days,
        'Risk Score': [random.uniform(30, 80) for _ in range(30)]
    })
    st.line_chart(historical_risk.set_index('Date'))

# ============== ALERTS PAGE ==============
elif page == "Alerts":
    st.header("🚨 Alerts & Notifications")
    
    alerts = [
        {"type": "Critical", "message": "High soil moisture detected in Zone A", "time": "5 mins ago", "status": "Active"},
        {"type": "Warning", "message": "Rainfall rate increasing in Zone B", "time": "15 mins ago", "status": "Active"},
        {"type": "Info", "message": "Routine maintenance completed in Zone C", "time": "1 hour ago", "status": "Resolved"},
    ]
    
    for alert in alerts:
        if alert["type"] == "Critical":
            st.error(f"🚨 {alert['type']}: {alert['message']} ({alert['time']})")
        elif alert["type"] == "Warning":
            st.warning(f"⚠️ {alert['type']}: {alert['message']} ({alert['time']})")
        else:
            st.info(f"ℹ️ {alert['type']}: {alert['message']} ({alert['time']})")
    
    st.header("📧 Alert Configuration")
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Email Notifications", value=True)
        st.checkbox("SMS Alerts", value=True)
    with col2:
        st.checkbox("Push Notifications", value=True)
        st.checkbox("In-app Notifications", value=True)

# ============== SETTINGS PAGE ==============
elif page == "Settings":
    st.header("⚙️ System Settings")
    
    st.subheader("Sensor Configuration")
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("Soil Moisture Threshold (%)", min_value=0, max_value=100, value=75)
        st.number_input("Rainfall Alert Threshold (mm/h)", min_value=0, max_value=100, value=50)
    with col2:
        st.number_input("Tilt Angle Alert Threshold (°)", min_value=0, max_value=90, value=15)
        st.number_input("Temperature Alert Threshold (°C)", min_value=0, max_value=50, value=40)
    
    st.subheader("System Status")
    st.info("✅ All sensors operational")
    st.info("✅ Connection to server: Active")
    st.info("✅ Data synchronization: Real-time")
    
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

st.sidebar.markdown("---")
st.sidebar.markdown("📍 **Developed by:** Team: The Bugs Slayers (VCDH-18)")
st.sidebar.markdown("🏆 **SIH Prototype** - Landslide Early Detection & Risk Management System")
