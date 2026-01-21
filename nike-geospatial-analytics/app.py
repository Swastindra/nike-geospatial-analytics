import streamlit as st
import os

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(page_title="Nike Geospatial Analytics", layout="wide")

# ==================================================
# SAFE IMAGE LOADER (PREVENTS WHITE SCREEN)
# ==================================================
def safe_image(path, caption=None):
    """
    Prevents app crash if image filename/path is wrong or missing.
    Shows warning instead of blank screen.
    """
    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=True)
    else:
        st.warning(f"⚠️ Image not found: {path}")

# ==================================================
# GLOBAL STYLING (CSS)
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #f7f9fb;
}

h1 {
    color: #0b3c5d;
    font-weight: 700;
}

h2, h3 {
    color: #1f6f8b;
    font-weight: 600;
}

p {
    color: #2e2e2e;
    font-size: 16px;
    line-height: 1.7;
}

section[data-testid="stSidebar"] {
    background-color: #0b3c5d;
}

section[data-testid="stSidebar"] * {
    color: white;
    font-weight: 500;
}

img {
    border-radius: 10px;
    box-shadow: 0px 6px 14px rgba(0,0,0,0.08);
}

hr {
    border: none;
    height: 1px;
    background-color: #d0d7de;
    margin: 2rem 0;
}

.box {
    background-color: #ffffff;
    padding: 22px;
    border-left: 6px solid #1f6f8b;
    border-radius: 8px;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR NAVIGATION
# ==================================================
page = st.sidebar.radio(
    "Navigation",
    [
        "Project Overview",
        "Factor 1: Population Density",
        "Factor 2: Commercial Proximity",
        "Factor 3: Income Level",
        "Map Analysis 1: Store Catchment Area Analysis",
        "Map Analysis 2: Population Exposure Analysis",
        "Map Analysis 3: Inter-Store Distance Analysis",
        "Conclusion"
    ]
)

# ==================================================
# PAGE 1 — OVERVIEW
# ==================================================
if page == "Project Overview":

    st.markdown("<h1 style='text-align:center;'>Geospatial Analysis of Nike Store Location Strategy</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.subheader("Methodological Framework")
    safe_image("nike-geospatial-analytics/methodology.jpeg")

    st.subheader("Snapshot of the Dataset")
    safe_image("nike-geospatial-analytics/dataset.jpeg")

    st.subheader("Base Map with Interactive Pop-Ups")
    safe_image("nike-geospatial-analytics/base map with pop ups.png")


# ==================================================
# FACTOR 1
# ==================================================
elif page == "Factor 1: Population Density":

    st.markdown("<h1>Factor 1: Population Density</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
    Correlation analysis was conducted to examine the relationship between population density
    and the spatial distribution of Nike stores across selected cities.
    </div>
    """, unsafe_allow_html=True)

    safe_image("nike-geospatial-analytics/pop density EDA .jpeg")

    st.subheader("Choropleth Representation of Population Density")
    safe_image("nike-geospatial-analytics/CHLOROPLETH.png")


# ==================================================
# FACTOR 2
# ==================================================
elif page == "Factor 2: Commercial Proximity":

    st.markdown("<h1>Factor 2: Commercial Proximity</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
    This analysis evaluates Nike’s preference for commercial shopping areas compared
    to transit-oriented locations, highlighting a brand-experience-driven retail strategy.
    </div>
    """, unsafe_allow_html=True)

    safe_image("nike-geospatial-analytics/Commercial Proximity .jpeg")

    st.subheader("Spatial Classification Based on Commercial Proximity")
    safe_image("nike-geospatial-analytics/visualisation of commerical proximity .jpeg")


# ==================================================
# FACTOR 3
# ==================================================
elif page == "Factor 3: Income Level":

    st.markdown("<h1>Factor 3: Income Level</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
    Income-level analysis was performed to examine whether Nike follows
    a premium-only location strategy or operates across diverse economic zones.
    </div>
    """, unsafe_allow_html=True)

    safe_image("nike-geospatial-analytics/income EDA.jpeg")

    st.subheader("Income-Based Spatial Visualization")
    safe_image("nike-geospatial-analytics/Visualisation of income .jpeg")


# ==================================================
# MAP 1 — BUFFER
# ==================================================
elif page == "Map Analysis 1: Store Catchment Area Analysis":

    st.markdown("<h1>Store Catchment Area Analysis (500-Meter Buffer)</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
    Buffer zones of 500 meters were generated around Nike store locations to represent
    approximate walkable influence areas. This analysis supports assessment of customer
    reach, coverage intensity, and spatial clustering.
    </div>
    """, unsafe_allow_html=True)

    safe_image("nike-geospatial-analytics/map1.png")


# ==================================================
# MAP 2 — POPULATION EXPOSURE ANALYSIS
# ==================================================
elif page == "Map Analysis 2: Population Exposure Analysis":

    st.markdown("<h1>Population Exposure Analysis</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
    This map visualizes the estimated population exposure within the spatial influence zones of Nike stores.
    A circular buffer has been generated around each store to represent its effective catchment area.
    </div>
    """, unsafe_allow_html=True)

    safe_image("nike-geospatial-analytics/map2.png")


# ==================================================
# MAP 3 — DISTANCE
# ==================================================
elif page == "Map Analysis 3: Inter-Store Distance Analysis":

    st.markdown("<h1>Inter-Store Distance Analysis Using Shapely</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
    Inter-store distances were computed using geometric operations in the Shapely library.
    Lines connecting store pairs represent spatial separation, enabling evaluation of
    proximity patterns and potential market cannibalization.
    </div>
    """, unsafe_allow_html=True)

    safe_image("nike-geospatial-analytics/map3.png")


# ==================================================
# CONCLUSION
# ==================================================
elif page == "Conclusion":

    st.markdown("<h1>Conclusion</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
    The geospatial analysis reveals that Nike’s store location strategy is not governed
    by a single demographic factor. Instead, store placement reflects a balanced
    consideration of accessibility, commercial vibrancy, and experiential retail value.

    The findings indicate that Nike stores are frequently located in lower residential
    density zones that experience high transient footfall, demonstrate strong preference
    for shopping districts over transit-only locations, and operate across diverse
    income-level regions.

    Overall, the study highlights how geospatial analytics can effectively support
    retail decision-making by uncovering spatial patterns that extend beyond traditional
    demographic indicators.
    </div>
    """, unsafe_allow_html=True)
