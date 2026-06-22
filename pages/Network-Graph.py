import streamlit as st
from pyvis.network import Network
import tempfile
import os

st.title("🕸️ Fraud Network Graph")

def graph():

    net = Network(height="600px", width="100%", bgcolor="#0a0a0a", font_color="white")

    net.add_node("Scammer", color="red", size=30)
    net.add_node("Victim A", color="green")
    net.add_node("Victim B", color="green")
    net.add_node("Bank", color="yellow")

    net.add_edge("Scammer", "Victim A")
    net.add_edge("Scammer", "Victim B")
    net.add_edge("Victim A", "Bank")

    path = os.path.join(tempfile.gettempdir(), "graph.html")
    net.save_graph(path)

    return path

if st.button("Generate Graph"):
    path = graph()
    st.components.v1.html(open(path, "r", encoding="utf-8").read(), height=600)