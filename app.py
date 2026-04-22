import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="VisionPark Dashboard", layout="wide")

st.title("🚗 VisionPark Smart Parking Dashboard")

# 🔹 Load data
@st.cache_data
def load_data():
    if os.path.exists("parking_log.csv"):
        return pd.read_csv("parking_log.csv")
    return pd.DataFrame()

df = load_data()

# 🔹 Metrics
col1, col2, col3 = st.columns(3)

if not df.empty:
    total = len(df)
    inside = len(df[df["status"] == "IN"])
    exited = len(df[df["status"] == "OUT"])

    col1.metric("🚗 Total Vehicles", total)
    col2.metric("🅿️ Currently Inside", inside)
    col3.metric("🚪 Exited", exited)
else:
    st.warning("No data available yet")

st.divider()

# 🔹 Current vehicles inside
st.subheader("🅿️ Vehicles Currently Inside")

if not df.empty:
    inside_df = df[df["status"] == "IN"]
    st.dataframe(inside_df, use_container_width=True)
else:
    st.write("No vehicles inside")

st.divider()

# 🔹 Full logs
st.subheader("📊 Parking Logs")

if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.write("No logs available")

st.divider()

# 🔹 Blacklist
st.subheader("🚨 Blacklisted Vehicles")

if os.path.exists("blacklist.csv"):
    bl = pd.read_csv("blacklist.csv")
    st.dataframe(bl)
else:
    st.write("No blacklist file")

# 🔹 Whitelist
st.subheader("✅ Whitelisted Vehicles")

if os.path.exists("whitelist.csv"):
    wl = pd.read_csv("whitelist.csv")
    st.dataframe(wl)
else:
    st.write("No whitelist file")

st.divider()

# 🔹 Show captured images
st.subheader("📸 Captured Vehicles")

if os.path.exists("captures"):
    images = os.listdir("captures")

    if images:
        for img in sorted(images[-6:], reverse=True):
            st.image(os.path.join("captures", img), caption=img, width=300)
    else:
        st.write("No images yet")
else:
    st.write("No capture folder found")

st.divider()

# 🔹 Auto refresh button
if st.button("🔄 Refresh"):
    st.cache_data.clear()