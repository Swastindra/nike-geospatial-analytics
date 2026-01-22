import streamlit as st
import os

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(page_title="DECODING NIKE’S GEOSPATIAL STRATEGY AND EXTENDING THE FRAMEWORK TO ADDRESS THE IMPORTANCE OF GEOSPATIAL ANALYTICS IN BRAND-BUIDLING AND SUPPLY CHAIN MANAGEMENT", layout="wide")

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
    The graph shows the number of Nike stores located in areas with and without nearby commercial or transit facilities.
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
    The first chart shows how Nike stores are distributed across different income groups in the brackets 0-2 lakhs, 2-7 lakhs and 7 and above lakhs. The chart besides is a quartile wise representation of the same.
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
    Buffer zones of 500 Meter are generated around Nike store locations to capture the estimated walkable influence areas. This helps in the analysis of customer reach, identify areas of overlap between nearby stores leading to market concentration etc.
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
    The Inter-store distance between all the stores are computed and plotted with the help of Shapely on the map. When we click on the line connecting the two stores, the pop-up displays the approximate distance between them.
    This helps in visualising the connectivity of different stores with each other and finding stores which are nearest or farthest from a particular store.
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
    The geospatial analysis of Nike’s store location strategy reveals several important
    spatial patterns that provide insight into the brand’s retail decision-making approach.

    1. Store Presence in Lower Population Density Regions

      The analysis indicates a relatively higher concentration of Nike stores in regions
      characterized by lower residential population density. This observation can be
      interpreted in two ways. First, population density values primarily represent residential
      distribution, whereas Nike stores are predominantly located in commercial and retail
      districts that experience high transient footfall. As a result, these areas may appear
      low-density in census-based data despite strong daily consumer movement.

      Secondly, the findings suggest that Nike, as an affordable-luxury brand, does not rely
      solely on residential population density as a determining factor for store placement.
      Instead, the brand prioritizes functional and experiential retail environments over
      pure demographic concentration.

    2. Role of Proximity and Commercial Context

     Proximity emerges as one of the most significant factors influencing Nike’s store
     location strategy. A deeper evaluation of the data-scraping stage reveals a clear
     pattern: Nike stores demonstrate a strong preference for shopping districts and
     commercial hubs over transit-oriented locations.

     This trend reinforces a brand-experience-driven retail model, where immersive
     shopping environments, brand visibility, and consumer engagement take precedence
     over purely convenience-based placement near transit nodes.

    3. Income-Level Distribution and Brand Positioning**

       The spatial distribution of Nike stores across income-level regions indicates that the
       brand operates within a wide economic spectrum. Stores are not confined exclusively
       to high-income zones, highlighting that Nike does not adopt a narrowly premium
       targeting strategy.

       Instead, the presence of stores across diverse income categories supports Nike’s
       mass-premium and accessibility-driven positioning, allowing the brand to cater to
       a broad consumer base while maintaining its aspirational identity.

   Overall, the findings demonstrate that Nike’s retail location strategy is shaped by a
   combination of accessibility, commercial vibrancy, and brand experience considerations
   rather than reliance on a single demographic or economic indicator.
    </div>
    """, unsafe_allow_html=True)
