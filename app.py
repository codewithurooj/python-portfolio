from pathlib import Path
import streamlit as st
from PIL import Image

# Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "images" / "CV.pdf"
profile_pic = current_dir / "images" / "profile.png"

# Details
PAGE_TITLE = "My Portfolio| Syeda Urooj Fatima"
PAGE_ICON = ":wave:"
NAME = "Urooj Fatima"
DESCRIPTION = """
Python Enthusiast with a Passion for AI Development As 
a dedicated AI student with a strong foundation in Python programming, 
I bring a proactive and problem-solving mindset to every challenge. 
I have hands-on experience with Python libraries such as NumPy, Pandas,
 and Matplotlib, and have worked on projects related to this.
"""
EMAIL = "fatimaurooj152@gmail.com"

# Social Links
SOCIAL_MEDIA_LINKS = {
    "Linkedin": "https://www.linkedin.com/in/syeda-urooj-fatima-a4b708301",
    "GitHub": "https://github.com/codewithurooj",
    "Twitter": "https://x.com/UroojFatim1376",
}


# Projects
PROJECTS = {
    "🧠 Growth Mindset Challenge - showing creativity": {
        "GitHub": "https://github.com/codewithurooj/mindset-growth.git",
        "Streamlit": "https://mindset-growth-lwioomgerq3pwertsule2p.streamlit.app/"
    },
    "⚖️ Unit Conversion App": {
        "GitHub": "https://github.com/codewithurooj/unit-convertor.git",
        "Streamlit": "https://unit-convertor-abcd.streamlit.app/"
    },
    "🔒 Password Strength Checker": {
        "GitHub": "https://github.com/codewithurooj/password-strength-checker.git",
        "Streamlit": "https://passward.streamlit.app/"
    },
    "🕮 CLI Based Personal Library Manager": {
        "GitHub": "https://github.com/codewithurooj/personal-library-manager.git",
    }
}

# Page Config
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# Loading Resources
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(label="📄 Download Resume", data=PDFbyte, file_name=resume_file.name, mime="application/pdf")
    st.write("📫", EMAIL)

# Social Links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA_LINKS))
for index, (platform, link) in enumerate(SOCIAL_MEDIA_LINKS.items()):
    cols[index].write(f"[{platform}]({link})")

# Experience
st.write("#")
st.subheader("Experience & Education")
st.write(
    """
    - ✔️ While I am new to professional roles, I am deeply passionate about Python
      programming and AI development. I have independently completed projects such
      as a Password Strength Checker and Unit Conversion App, showcasing my ability 
      to apply theoretical knowledge to practical challenges.
    """
)

# Skills
st.write("#")
st.subheader("Skills")
st.write(
    """
    - ✔️ Python
    - ✔️ Web development (HTML, CSS, TypeScript, Next.js, Tailwind CSS)
    - ✔️ Familiarity with libraries like NumPy, Pandas, Matplotlib.
    - ✔️ Git/GitHub for version control.
    """
)

# Projects Section
st.write("#")
st.subheader(" Python Projects")
for project_name, links in PROJECTS.items():
    st.write(f"**{project_name}**")
    if "GitHub" in links:
        st.write(f"[GitHub Repository]({links['GitHub']})")
    if "Streamlit" in links:
        st.write(f"[Live Demo]({links['Streamlit']})")
    st.write("---")  # Separator for visual clarity
