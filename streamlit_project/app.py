import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Simple Streamlit App", layout="centered")

st.title("Simple Streamlit Project")
st.write("A simple Streamlit app with inputs, charts, and data display.")

name = st.text_input("Enter your name")
if name:
    st.success(f"Hello, {name}! Welcome to the Streamlit demo.")

option = st.selectbox(
    "Choose a dataset",
    ["Random values", "Sine wave", "Cosine wave"],
)

n_points = st.slider("Number of points", min_value=10, max_value=100, value=50, step=5)

if option == "Random values":
    data = pd.DataFrame({"x": np.arange(n_points), "y": np.random.randn(n_points).cumsum()})
elif option == "Sine wave":
    x = np.linspace(0, 2 * np.pi, n_points)
    data = pd.DataFrame({"x": x, "y": np.sin(x)})
else:
    x = np.linspace(0, 2 * np.pi, n_points)
    data = pd.DataFrame({"x": x, "y": np.cos(x)})

st.subheader("Dataset preview")
st.dataframe(data.head())

st.subheader("Chart")
st.line_chart(data.set_index("x"))

st.markdown("---")
st.write(
    "Use the controls above to change the dataset type and point count. "
    "Streamlit updates instantly when you interact with the widgets."
)
