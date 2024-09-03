#! /usr/bin/env python3
# Author Gaurav Sablok
# Universitat Potsdam
# Date 2024-9-3
# multipage streamlit application for seagrass health monitoring
 # inbuilt support for all genes and ecosystems
 # inbuilt support for BLAST analysis

"""
    defining the entry point for the main streamlit application.
    The application consists of the following pages.
    import streamlit as st
    st.markdown('<div style="text-align: center;">Hello World!</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: left;">Hello World!</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: right;">Hello World!</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Hello World!</div>', unsafe_allow_html=True)
"""

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Seagrass Health Genomics Monitoring System",
    page_icon="Universitat Potsdam",
    layout="wide",
    initial_sidebar_state="expanded")
st.image("https://www.uni-potsdam.de/typo3conf/ext/up_template/Resources/Public/Images/logos/up_logo_international_2.png", width=100)
st.header("Seagrass Health Genomics Monitoring System")
st.subheader(
    "Developed by Gaurav Sablok, Universitat Potsdam, Germany")


st.html(
        "<p><h3>This is a desktop utility to carry for the seagrass expedition</p></h3>"
        "<p><h4>It offers following:<h4>"
        "<li><ul>Inbuild database for carbonic anhydrase, light dependent, light independent, photosystem</ul></li>"
        "<ul><li>In-built support for BLAST</ul></li>"
        "<ul><li>in build sequence retriveal system</ul></li>"
        )

st.html(
        "<h2> Welcome to the Seagrass Functional Health Monitoring System </h2>"
        "<br>"

        "<p><h2>Intoduction to the Seagrass Systems<h2></p>"
        "<p><h3>This streamlit application allows you to mine all the seagrass Genomics related genes and ecosystems for monitoring the seagrass health.It has inbuilt support for the functional genome analysis of the seagrasses and also has support for the identifcation and characterization of the genomes and their regions.It boasts a large amount of the internallly hosted genes without the need of the relationsal database as the databases are relatively small, well crafted health monitoring system.</h3></p>"
        "<br>"
        "<br>"
        "<br>"
        "<p><h2>Seagrass system attributes:<h2></p>"
        "<p><h3>It contains the following genes and their ecosystems</h3></p>"
        "<li><ul><h4>Carbonic Annhydrase: Genes related to the carbonic annhydrase ecosystem</h4></ul></li>"
        "<li><ul><h4>Light-Dependent-Nucletoide: It allows you to get the nucleotide sequences for the same</h4></ul></li>"
        "<li><ul><h4>Light-Independent-Nucleotide: Functionally associates proteins</h4></ul></li>"
        "<li><ul><h4>Photosystem: Functionally associated photosyste related genes</h4></ul></li>"
        )

carbonic = st.Page(
        "carbonic.py", title="Carbonic Annhydrase", icon=":material/add_circle:"
        )

lightdependentnucl = st.Page(
    "lightdep.py", title="Light-Dependent-Nucleotide", icon=":material/add_circle:")

lightindependent = st.Page(
        "lightindep.py", title="Light-Independent-Nucleotide", icon=":material/add_circle:"
        )
photosystem = st.Page("photosystem.py", title="Photosystem",
                      icon=":material/add_circle:")

pg = st.navigation([carbonic, lightdependentnucl, lightindependent, photosystem])
pg.run()
