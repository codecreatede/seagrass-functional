#! /usr/bin/env python3
# Author Gaurav Sablok
# Universitat Potsdam
# Date 2024-9-3
# multipage streamlit application for seagrass health monitoring
 # inbuilt support for all genes and ecosystems
 # inbuilt support for BLAST analysis

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.header("Photosystem analyzer")
st.subheader("Developed by Gaurav Sablok")

help = st.button("Display the help toggle button")
if help:
    st.write("The following options are present in the Photosystem Analyzer")
    st.write("1. select the gene")
    st.write("2. fasta will come and download for the analysis")

