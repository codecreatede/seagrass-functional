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
import os
import sys

st.header("Photosystem analyzer")
st.subheader("Developed by Gaurav Sablok")

help = st.button("Display the help toggle button")
if help:
    st.write("The following parameters are needed for the BLAST analysis")
    st.write("1. PATH to the BLAST/DIAMOND executable")
    st.write("2. Input sequence for the BLAST/DIAMOND analysis")

 fasta = st.text_input("Please enter the sequences which you want to add for the BLAST/DIAMOND analysis")
 database =


