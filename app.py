import streamlit as st
from career_data import CAREER_DATA


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Main Application Background */
.stApp {
    background-color: white;
    color: black;
}

/* Main Content */
.main {
    background-color: white;
    color: black;
}

/* Title */
.title {
    text-align: center;
    color: black;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: black;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Cards */
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    color: black;
    border: 1px solid #dddddd;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Skill Tags */
.skill {
    display: inline-block;
    background-color: #f0f0f0;
    color: black;
    padding: 6px 12px;
    border-radius: 20px;
    margin: 4px;
    font-size: 14px;
    border: 1px solid #cccccc;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: white;
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: black !important;
}

/* All Text */
p, h1, h2, h3, h4, h5, h6, label {
    color: black !important;
}

/* Input Boxes */
input {
    color: black !important;
    background-color: white !important;
}

/* Select Boxes */
div[data-baseweb="select"] {
    background-color: white !important;
}

/* Button */
.stButton > button {
    background-color: black;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #333333;
    color: white;
}

/* Horizontal Line */
hr {
    border-color: #cccccc;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🎓 AI-Based Career Guidance and Skill Gap Analysis System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Discover the right career, identify your skill gaps and build your learning roadmap.</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("👤 Student Profile")

name = st.sidebar.text_input(
    "Enter your name"
)

education = st.sidebar.selectbox(
    "Education",
    [
        "10th",
        "Intermediate",
        "Diploma",
        "B.Tech",
        "B.Sc",
        "BCA",
        "MCA",
        "Other"
    ]
)

interests = st.sidebar.multiselect(
    "Select your interests",
    [
        "Artificial Intelligence",
        "Machine Learning",
        "Data Science",
        "Web Development",
        "Programming",
        "Cybersecurity",
        "Software Development"
    ]
)

user_skills = st.sidebar.multiselect(
    "Select your current skills",
    [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "Statistics",
        "Data Structures",
        "HTML",
        "CSS",
        "JavaScript",
        "Django",
        "Networking",
        "Linux",
        "Cybersecurity",
        "Ethical Hacking",
        "Cryptography",
        "Java",
        "C++",
        "Algorithms",
        "Data Analysis",
        "Data Visualization"
    ]
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze = st.sidebar.button(
    "🚀 Analyze My Career",
    use_container_width=True
)


# =========================================================
# HOME PAGE
# =========================================================

if not analyze:

    st.markdown("""
    <div class="card">

    <h2>🌟 Welcome to AI Career Guidance</h2>

    <p>
    This system helps students understand their career opportunities
    based on their education, interests and technical skills.
    </p>

    <h3>What this system provides:</h3>

    <p>🎯 Suitable career recommendations</p>
    <p>📊 Skill gap analysis</p>
    <p>📚 Personalized learning roadmap</p>
    <p>💼 Career-specific skill requirements</p>
    <p>🚀 Career readiness percentage</p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🎯 Career Guidance</h3>
        <p>
        Find careers that match your interests and current skills.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>📊 Skill Gap Analysis</h3>
        <p>
        Identify the skills you already have and the skills you need.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>📚 Learning Roadmap</h3>
        <p>
        Follow a step-by-step learning path toward your career.
        </p>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# CAREER ANALYSIS
# =========================================================

else:

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not name:
        st.warning("⚠️ Please enter your name.")
        st.stop()

    if not interests:
        st.warning("⚠️ Please select at least one interest.")
        st.stop()

    st.success(
        f"Welcome {name}! Your career analysis is ready. 🎉"
    )


    # =====================================================
    # CAREER MATCHING
    # =====================================================

    career_scores = {}

    for career, details in CAREER_DATA.items():

        score = 0

        career_skills = set(
            skill.lower()
            for skill in details["skills"]
        )

        selected_skills = set(
            skill.lower()
            for skill in user_skills
        )

        # Skill matching
        matching_skills = career_skills.intersection(
            selected_skills
        )

        score += len(matching_skills) * 10

        # Interest matching
        career_name = career.lower()

        for interest in interests:

            interest_words = interest.lower().split()

            for word in interest_words:

                if word in career_name:
                    score += 15

        career_scores[career] = score


    # Sort careers
    recommended_careers = sorted(
        career_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )


    # =====================================================
    # RECOMMENDED CAREERS
    # =====================================================

    st.header("🎯 Recommended Careers")

    for career, score in recommended_careers[:3]:

        details = CAREER_DATA[career]

        if score > 0:
            match = min(score, 100)
        else:
            match = 20

        st.markdown(
            f"""
            <div class="card">

            <h2>💼 {career}</h2>

            <p>{details["description"]}</p>

            <p>
            <strong>Career Match: {match}%</strong>
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # BEST CAREER
    # =====================================================

    best_career = recommended_careers[0][0]

    best_details = CAREER_DATA[best_career]

    st.header("🏆 Best Career Recommendation")

    st.success(
        f"Based on your interests and current skills, "
        f"your recommended career is **{best_career}**."
    )

    st.write(
        f"**Recommended Education:** {best_details['education']}"
    )


    # =====================================================
    # REQUIRED SKILLS
    # =====================================================

    st.header("🧠 Required Skills for This Career")

    for skill in best_details["skills"]:

        st.markdown(
            f'<span class="skill">{skill}</span>',
            unsafe_allow_html=True
        )


    # =====================================================
    # SKILL GAP ANALYSIS
    # =====================================================

    st.header("📊 Skill Gap Analysis")

    required_skills = set(
        skill.lower()
        for skill in best_details["skills"]
    )

    current_skills = set(
        skill.lower()
        for skill in user_skills
    )

    matched_skills = required_skills.intersection(
        current_skills
    )

    missing_skills = required_skills.difference(
        current_skills
    )


    col1, col2 = st.columns(2)


    # -----------------------------------------------------
    # EXISTING SKILLS
    # -----------------------------------------------------

    with col1:

        st.subheader("✅ Your Existing Skills")

        if matched_skills:

            for skill in sorted(matched_skills):

                st.markdown(
                    f'<span class="skill">✓ {skill.title()}</span>',
                    unsafe_allow_html=True
                )

        else:

            st.write(
                "No matching skills found."
            )


    # -----------------------------------------------------
    # MISSING SKILLS
    # -----------------------------------------------------

    with col2:

        st.subheader("❌ Skills to Develop")

        if missing_skills:

            for skill in sorted(missing_skills):

                st.markdown(
                    f'<span class="skill">+ {skill.title()}</span>',
                    unsafe_allow_html=True
                )

        else:

            st.success(
                "Excellent! You have all required skills."
            )


    # =====================================================
    # SKILL READINESS
    # =====================================================

    total = len(required_skills)

    if total > 0:

        skill_percentage = int(
            (len(matched_skills) / total) * 100
        )

    else:

        skill_percentage = 0


    st.header("📈 Skill Readiness")

    st.progress(
        skill_percentage / 100
    )

    st.write(
        f"### Your current skill readiness: {skill_percentage}%"
    )


    # =====================================================
    # LEARNING ROADMAP
    # =====================================================

    st.header("🛣️ Personalized Learning Roadmap")

    for index, step in enumerate(
        best_details["roadmap"],
        start=1
    ):

        st.markdown(
            f"""
            <div class="card">
            <strong>Step {index}</strong>
            <p>{step}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # CAREER SUMMARY
    # =====================================================

    st.header("📋 Career Summary")

    st.markdown(
        f"""
        <div class="card">

        <h2>🎓 {best_career}</h2>

        <p>
        <strong>Student:</strong> {name}
        </p>

        <p>
        <strong>Education:</strong> {education}
        </p>

        <p>
        <strong>Skill Readiness:</strong> {skill_percentage}%
        </p>

        <p>
        <strong>Skills to Improve:</strong>
        {len(missing_skills)}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # FINAL MESSAGE
    # =====================================================

    st.markdown("---")

    st.success(
        "💡 Keep learning, build real-world projects, "
        "practice your skills regularly, and update your GitHub portfolio."
    )