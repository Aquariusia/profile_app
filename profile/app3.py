import streamlit as st
import plotly.graph_objects as go

# -------------------------------
# Streamlit Pages
# -------------------------------
st.set_page_config(
    page_title="Richard Luo's Research Portfolio Page",
    page_icon=":mortar_board:",
    layout="wide"
)

# -------------------------------
# CSS + Hover
# -------------------------------
st.markdown("""
<style>
body { font-family: 'Helvetica', sans-serif; background-color:#FAFAFA; }
h1,h2,h3 { color:#0B3D91; }
.stButton>button { background-color:#0B3D91;color:white;border-radius:8px;padding:6px 20px; }
.stContainer {
    background-color:white; 
    border-radius:10px; 
    padding:15px; 
    margin-bottom:15px; 
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}
.stContainer:hover {
    transform: translateY(-5px);
    box-shadow: 4px 6px 15px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar Navigate
# -------------------------------
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Publications", "Projects", "Contact"]
)

# -------------------------------
# Home
# -------------------------------
if page == "Home":
    col1, col2 = st.columns([1,2])
    with col1:
        st.image("https://raw.githubusercontent.com/Aquariusia/profile_app/refs/heads/main/profile/profile.jpg", width=500)
    with col2:
        st.markdown("""
        <div style="padding:10px">
        <h1>Yucheng / Richard Luo</h1>
        <p><b>Data Scientist & Researcher & Composer</b></p>
        <p>Welcome to my portfolio. I hold a B.Econ from the University of Sydney, majored Data Science and Econometrics. My research interests include data science, machine learning, AI in Health, agent-based social simulation, and machine learning based causal inference.</p>
        <p>I am currently focused on data-driven approaches to understanding social systems and policy impacts, and I am preparing applications for Ph.D. or M.Phil programs commencing in 2026, with the aim of advancing my work in quantitative methods and intelligent systems.</p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------
# Publications
# -------------------------------
elif page == "Publications":
    st.header("Publications & Research")

    publications = [
        {"Title": "Replication and Critique of David Card’s 1993 Work: Re-estimating the Returns on Education with Distance to College as an Instrumental Variable.",
         "Type": "Research",
         "Details": "This research revisits David Card’s 1993 study on the causal effect of college attendance on returns to education by leveraging a new dataset and several updated estimation methods. I re-evaluate the relationship between students’ family proximity to universities and educational outcomes, and examine how the validity of distance as an instrumental variable may have attenuated in the context of widespread internet access and remote learning. Proposing and reporting a novel discovering for the weakening IV validity linked to structural behavioral shifts under digital transformation, bringing spatiotemporal perspective to IV, a widely deployed econometric identification strategy."}
    ]

    search = st.text_input("Search Publications")
    filtered_pubs = [p for p in publications if search.lower() in p['Title'].lower()]

    for i, pub in enumerate(filtered_pubs):
        st.markdown(f"""
        <div class="stContainer">
            <h3>{pub['Title']}</h3>
            <p>{pub['Type']}</p>
        </div>
        """, unsafe_allow_html=True)
        with st.expander("View Details", expanded=False):
            st.write(pub["Details"])

# -------------------------------
# Projects
# -------------------------------
elif page == "Projects":
    st.header("Projects")

    projects = [
        {"Name": "Data-Driven Identification for Optimal Locations of New Primary Schools in Sydney, Taking Parramatta, Blacktown, City & Inner South as Examples.",
         "Description": "Geospatial Data Case",
         "Details": "This project selects four representative suburbs in Sydney and integrates multiple resource indicators as points of interest (POIs), which are normalized and incorporated into a comprehensive, visualized geographic information system (GIS) map. By analyzing resource enrichment at the neighborhood level, the study provides data-driven insights and policy recommendations for the optimal siting of new primary schools."},
        {"Name": "XGBoost Classification of Acute Leukemia and Key Biomarker Discovery Using the Golub et al. (Science, 1999) Gene Expression Dataset.",
         "Description": "ML Healthcare Case",
         "Details": "This project provided a foundational classification model pipeline for an Accenture healthcare consulting team. It utilized gene expression data from leukemia patients reported in Golub et al. (Science, 1999) and involved exploratory data analysis (EDA), data cleaning, preprocessing, and feature engineering. Due to the high-dimensional and low-sample-size nature of the dataset, multiple classification models were trained and compared. XGBoost was ultimately selected as the optimal model, and the cleaned dataset was used to train the model to obtain the final weighted classifier for acute leukemia prediction."},
        {"Name": "Next-Generation Community-Based Service Solutions.",
         "Description": "Led  data analysis & drafted actionable report.",
         "Details": "Conducted data-driven analysis for a Rotary International report by collecting income level data from multiple authoritative sources as an intermediate variable. Using this, a causal relationship between charitable participation and educational attainment was established, providing a quantitative basis to support subsequent policy and decision-making recommendations."},
        {"Name": "A genomic data-based diagnostic assistant for leukemia.",
         "Description": "Developed LLM + XGBoost pipeline for genome data; Achieved 90% accuracy & recall; Deployed with Streamlit for interactive demo.",
         "Details": "Developed a Streamlit-based web application that serves as an AI-powered diagnostic assistant for leukemia. The system integrates a base classification model with a feature-refined dataset selected via leave-one-out methods and fine-tunes a large language model (LLM) to assist analysis. Complex prompt engineering is applied to guide the AI outputs. The deployed chatbot enables healthcare professionals to upload patient genomic data and receive AI-assisted risk assessments, supporting clinical decision-making and personalized medical recommendations."}
    ]

    for i, proj in enumerate(projects):
        st.markdown(f"""
        <div class="stContainer">
            <h3>{proj['Name']}</h3>
            <p>{proj['Description']}</p>
        </div>
        """, unsafe_allow_html=True)
        with st.expander("View Details", expanded=False):
            st.write(proj["Details"])

    # radarchat
    st.subheader("Skill Overview")
    categories = ["ML", "ECMT", "DSci", "Causal inference", "Bio Med"]
    values = [5,4,5,4,3]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skill Level'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,5])))
    st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Contact
# -------------------------------
elif page == "Contact":
    st.header("Contact Me")
    st.write("""
    - Twitter/X: [https://x.com/Seiya_Hoshimi](https://x.com/Seiya_Hoshimi)
    - Email: kiruohoshi@hotmail.com
    """)










