import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Function to convert image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Page Configuration
st.set_page_config(page_title="Pranav Thakur's Portfolio", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        body {background-color: #f4f4f4;}
        .title {text-align: center; font-size: 30px; font-weight: bold; color: #555;}
        .subtitle {text-align: center; font-size: 16px; color: #555; background: linear-gradient(90deg, #0073b1, #00c6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;}
        .section-title {font-size: 20px; font-weight: bold; color: #444; margin-top: 20px; background: linear-gradient(90deg, #0073b1, #00c6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
        .navbar {background-color: #0073b1; padding: 10px; text-align: center; border-radius: 10px; margin-bottom: 20px;}
        .navbar a {color: white; text-decoration: none; font-size: 14px; margin: 0 15px; padding: 8px 15px; transition: all 0.3s ease;}
        .navbar a:hover {background-color: white; color: #0073b1; border-radius: 5px;}
        .profile-img {border-radius: 50%; display: block; margin: 0 auto; width: 200px; height: 200px; object-fit: cover;}
    </style>
    """,
    unsafe_allow_html=True
)

# Navbar
st.markdown(
    """
    <div class='navbar'>
        <a href='#about'>About</a>
        <a href='#skills'>Skills</a>
        <a href='#projects'>Projects</a>
        <a href='#contact'>Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Load Profile Image
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    image = Image.open("pranav_photo.jpg")  # Replace with your image file path
    st.markdown(f"<img src='data:image/jpeg;base64,{image_to_base64(image)}' class='profile-img'>", unsafe_allow_html=True)
with col2:
    st.markdown("<p class='title'>🚀 Hey There, I am Pranav Thakur</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Data Engineer | Data Analyst | Big Data Enthusiast</p>", unsafe_allow_html=True)

# About Me Section
st.markdown("<p class='section-title' id='about'>👨‍💻 About Me</p>", unsafe_allow_html=True)
st.write("""
- 🎓 **BE in Computer Science & Engineering** from Prof. Ram Meghe Institute of Technology & Research | **PG-DBDA** from C-DAC
- 💡 Passionate about **Data Engineering, Big Data, and Analytics**
- 🛠 Skilled in **Python, Java, R, SQL, Big Data Technologies, Machine Learning, Cloud Computing**
- 📊 Experience in **Fraud Detection, Network Security Monitoring, and Data Visualization**
- 🎯 Certified in **Python for Data Science, Power BI, and Databricks Fundamentals**
- 🌍 Languages: English, Hindi, Marathi
""")

# Skills Section
st.markdown("<p class='section-title' id='skills'>🛠️ Skills</p>", unsafe_allow_html=True)
skills = ["Python", "Java", "R", "SQL", "Big Data Technologies", "Machine Learning", "Cloud Computing", "Data Visualization", "Power BI", "Linux Programming"]
st.write(" | ".join(skills))

# Projects Section
st.markdown("<p class='section-title' id='projects'>📂 Projects</p>", unsafe_allow_html=True)
project = st.selectbox("Select a Project to View Details", [
    "Fraud Detection Pipeline Using Azure Databricks", 
    "Network Security Monitoring Using Machine Learning", 
    "Student Result Analysis"
])

if project == "Fraud Detection Pipeline Using Azure Databricks":
    st.write("""
    🛒 Built a fraud detection pipeline to identify fraudulent banking transactions using Azure Databricks.
    Utilized **Python, PySpark, SparkSQL, Azure Databricks, AWS, and Power BI**.
    Project Repository: [GitHub](https://github.com/Pranavvthakur/Fraud-Detection-Pipeline-Using-Azure-Databricks.git)
    """)
elif project == "Network Security Monitoring Using Machine Learning":
    st.write("""
    📹 Developed a system to detect DDoS attacks and network anomalies using Machine Learning.
    Integrated **Python, Streamlit, and Machine Learning** for visualization and alerting.
    """)
elif project == "Student Result Analysis":
    st.write("""
    📊 Analyzed student results using **Python, Pandas, and Power BI** to identify trends and areas for improvement.
    """)

# Contact Info
st.sidebar.header("📬 Connect with Me")
st.sidebar.markdown("""
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/pranavsing-thakur-318215227)  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-lightgray?style=flat&logo=github)](https://github.com/Pranavvthakur)  
📧 Email: pranavthakur@example.com  
📞 Mobile: +91 1234567890
""")

st.markdown("<p class='section-title' id='contact'>📩 Let's Connect!</p>", unsafe_allow_html=True)
st.write("I am always open to collaboration and learning new technologies. Let's connect and explore how we can work together! 🚀")

# Call-to-Action Button
st.markdown("""
    <a href='mailto:pranavthakur@example.com' class='button'>📩 Contact Me</a>
""", unsafe_allow_html=True)
