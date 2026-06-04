import streamlit as st
import pdfplumber
import skills

# Page Configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Modern UI
st.markdown("""
<style>
    * { box-sizing: border-box; }
    html, body, .stApp { height: 100%; }
    body { background: #05060a; color: #e6eef8; font-family: 'Rajdhani', sans-serif; }

    .header-container { text-align: center; padding: 40px 0; color: #e6eef8; }

    /* Glassy metric card for dark mode */
    .metric-card {
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.015));
        border: 1px solid rgba(255,255,255,0.04);
        backdrop-filter: blur(6px);
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 6px 24px rgba(2,6,23,0.6);
    }

    .role-card {
        background: linear-gradient(90deg, rgba(99,102,241,0.06), rgba(15,23,42,0.6));
        border-left: 4px solid rgba(99,102,241,0.9);
        border-radius: 12px;
        padding: 18px;
        margin: 10px 0;
        color: #e6eef8;
        box-shadow: 0 8px 40px rgba(2,6,23,0.7);
    }

    .upload-section {
        background: linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.015));
        border: 1px solid rgba(255,255,255,0.04);
        border-radius: 14px;
        padding: 28px;
        margin: 20px 0;
        box-shadow: 0 10px 50px rgba(2,6,23,0.65);
    }

    .skill-tag {
        display: inline-block;
        background: linear-gradient(90deg,#4f46e5,#7c3aed);
        color: white;
        padding: 8px 14px;
        border-radius: 999px;
        margin: 6px 6px 6px 0;
        font-size: 13px;
        font-weight: 600;
        box-shadow: 0 4px 18px rgba(79,70,229,0.18);
    }

    .skill-tag-missing {
        display: inline-block;
        background: linear-gradient(90deg,#fb7185,#ef4444);
        color: white;
        padding: 8px 14px;
        border-radius: 999px;
        margin: 6px 6px 6px 0;
        font-size: 13px;
        font-weight: 600;
        box-shadow: 0 4px 18px rgba(239,68,68,0.14);
    }

    h1, h2, h3, h4 { color: #e6eef8; font-weight: 700; }
    p, .metric-sub { color: #aab8d6; }

    /* Responsive tweaks */
    @media (max-width: 600px) {
        .metric-card { padding: 14px; }
        .upload-section { padding: 18px; }
    }
</style>
""", unsafe_allow_html=True)

# Small helper CSS animations for metric values
st.markdown("""
<style>
    .metric-value {
        animation: popIn 900ms cubic-bezier(.2,.8,.2,1);
    }
    @keyframes popIn {
        0% { transform: translateY(8px) scale(0.98); opacity: 0 }
        60% { transform: translateY(-4px) scale(1.02); opacity: 1 }
        100% { transform: translateY(0) scale(1); }
    }
    .header-hero { position: relative; overflow: hidden; }
    .hero-accent {
        position: absolute; inset: -20% -10% auto -10%; height: 220px; background: radial-gradient(circle at 20% 30%, rgba(124,58,237,0.12), transparent 30%);
        filter: blur(40px); pointer-events: none; transform: translateZ(0);
    }
    .subtle-fade { opacity: 0.92 }
</style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='header-container'><h1>📄 AI Resume Analyzer</h1></div>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: white; font-size: 18px; margin-bottom: 30px;'>Unlock your career potential with intelligent resume analysis</p>", unsafe_allow_html=True)

# Upload Section
st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "📤 Upload Your Resume (PDF)",
    type=["pdf"],
    help="Upload a PDF resume for analysis"
)
st.markdown("</div>", unsafe_allow_html=True)

# Load job roles from `skills` module with a safe fallback in case Streamlit
# imports a different `skills` (name collision) or the attribute is missing.
try:
    job_roles = skills.job_roles
except Exception:
    import importlib.util, os
    spec = importlib.util.spec_from_file_location("local_skills", os.path.join(os.path.dirname(__file__), "skills.py"))
    local_skills = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(local_skills)
    job_roles = getattr(local_skills, "job_roles", {})

if uploaded_file:
    # Extract text from PDF
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
    
    # Calculate scores
    scores = {}
    for role, role_skills in job_roles.items():
        count = sum(1 for skill in role_skills if skill.lower() in text.lower())
        scores[role] = count
    
    best_role = max(scores, key=scores.get)
    role_skills = job_roles[best_role]
    
    found_skills = [skill for skill in role_skills if skill.lower() in text.lower()]
    matched = len(found_skills)
    ats_score = (matched / len(role_skills)) * 100
    
    missing = [skill for skill in role_skills if skill.lower() not in text.lower()]
    
    # Recommended Role Section
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div class='role-card' style='text-align: center; border-left: none; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);'>
            <h3 style='color: white; font-size: 24px; margin-bottom: 10px;'>🎯 Best Match</h3>
            <h2 style='color: #ffd700; font-size: 32px;'>{best_role}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # ATS Score Section
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='color: #667eea; margin-bottom: 15px;'>📊 ATS Score</h3>
            <h1 style='color: #667eea; font-size: 48px;'>{ats_score:.1f}%</h1>
            <p style='color: #666; margin-top: 10px;'>{matched} out of {len(role_skills)} skills matched</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='color: #667eea; margin-bottom: 15px;'>🎓 Progress</h3>
            <p style='color: #666; font-size: 14px; margin-bottom: 10px;'>Your skill match progress</p>
        """, unsafe_allow_html=True)
        st.progress(ats_score / 100)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Top Career Matches
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: white;'>🏆 Top Career Matches</h2>", unsafe_allow_html=True)
    
    sorted_roles = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    cols = st.columns(len(sorted_roles[:3]))
    for idx, (role, score) in enumerate(sorted_roles[:3]):
        with cols[idx]:
            match_percent = (score / len(job_roles[role])) * 100
            st.markdown(f"""
            <div class='metric-card'>
                <h4 style='color: #667eea;'>{idx+1}. {role}</h4>
                <h3 style='color: #667eea; font-size: 24px;'>{match_percent:.0f}%</h3>
                <p style='color: #666; font-size: 12px;'>{score} skills matched</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Skills Section
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3 style='color: white;'>✅ Skills Found</h3>", unsafe_allow_html=True)
        if found_skills:
            skills_html = "".join([f"<span class='skill-tag'>{skill}</span>" for skill in found_skills])
            st.markdown(f"<div style='margin: 15px 0;'>{skills_html}</div>", unsafe_allow_html=True)
        else:
            st.info("No skills found in resume")
    
    with col2:
        st.markdown("<h3 style='color: white;'>❌ Missing Skills</h3>", unsafe_allow_html=True)
        if missing:
            missing_html = "".join([f"<span class='skill-tag-missing'>{skill}</span>" for skill in missing])
            st.markdown(f"<div style='margin: 15px 0;'>{missing_html}</div>", unsafe_allow_html=True)
        else:
            st.success("🎉 All skills matched!")
    
    # Learning Roadmap
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: white;'>📚 Learning Roadmap</h2>", unsafe_allow_html=True)
    
    if missing:
        for i, skill in enumerate(missing, 1):
            with st.expander(f"📖 Week {i}: Learn {skill}", expanded=(i == 1)):
                st.markdown(f"""
                **Skill:** {skill}  
                **Week:** {i}  
                **Priority:** {'High' if i <= 3 else 'Medium'}  
                **Status:** Not Yet Started ⏳
                """)
    else:
        st.balloons()
        st.success("🌟 You have all the required skills!")
    
    # Resume Rating
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: white;'>⭐ Resume Rating</h2>", unsafe_allow_html=True)
    
    if ats_score >= 80:
        rating = "🌟 Excellent"
        rating_color = "#10b981"  # green
    elif ats_score >= 60:
        rating = "👍 Good"
        rating_color = "#818cf8"  # soft purple
    else:
        rating = "⚠️ Needs Improvement"
        rating_color = "#f59e0b"  # amber
    
    st.markdown(f"""
    <div class='metric-card' style='text-align:center;'>
        <h3 style='color: {rating_color}; margin-bottom: 8px;'>{rating}</h3>
        <p style='color: #aab8d6;'>Based on your skill match percentage</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.info("📤 Upload a PDF resume to get started!")
