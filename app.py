import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Page Configuration
st.set_page_config(page_title="AI Career Predictor", layout="wide")

# --- 2. BACK-END FUNCTIONS ---

def get_subject_names(course):
    course = course.strip().upper()
    if "B.TECH" in course or "BCA" in course: return "Mathematics", "Programming"
    elif "B.COM" in course or "BBA" in course: return "Accountancy", "Business Logic"
    elif "BA" in course: return "History", "Literature"
    elif "B.SC" in course: return "Core Science", "Practical/Lab"
    elif "POLY" in course or "DIPLOMA" in course: return "Applied Science", "Workshop Tech"
    else: return "Theory Skill", "Practical Skill"

def predict_career(s1, s2, comm, course):
    course = course.strip().upper()
    avg = (s1 + s2 + comm) / 3
    
    # 1. B.TECH / BCA
    if "B.TECH" in course or "BCA" in course:
        if s2 > 85 and s1 > 85: return "AI & Robotics Engineer / Data Scientist / Cloud Architect"
        elif s2 > 75 and comm > 75: return "Full Stack Developer / UI-UX Designer / Product Manager"
        elif s1 > 80: return "Cyber Security Analyst / Backend Developer"
        elif comm > 80: return "IT Consultant / Technical Sales / SCRUM Master"
        else: return "System Admin / Web Developer / Network Support"

    # 2. B.COM / BBA
    elif "B.COM" in course or "BBA" in course:
        if s1 > 85 and s2 > 85: return "Investment Banker / Chartered Accountant (CA) / Equity Analyst"
        elif comm > 85 and s2 > 75: return "Marketing Director / HR Manager / Public Relations"
        elif s1 > 75: return "Tax Consultant / Financial Auditor / Risk Manager"
        elif comm > 75: return "Operations Manager / Business Development Executive"
        else: return "Accounting Assistant / Retail Manager"

    # 3. POLYTECHNIC / DIPLOMA
    elif "POLY" in course or "DIPLOMA" in course:
        if s2 > 85: return "Senior Technical Lead / Quality Assurance Manager"
        elif s1 > 80: return "CAD Designer / Junior Civil Engineer"
        elif s2 > 65: return "Production Supervisor / Site Engineer"
        else: return "Technical Maintenance / Workshop Instructor"

    # 4. B.SC
    elif "B.SC" in course:
        if s1 > 85 and s2 > 85: return "Research Scientist / Forensic Expert / Data Analyst"
        elif s1 > 75: return "Lab Pathologist / Quality Control Chemist"
        elif comm > 80: return "Science Content Writer / Academic Counselor"
        else: return "Environmental Consultant / Subject Specialist"

    # 5. BA (Arts)
    elif "BA" in course:
        if s1 > 85 and comm > 85: return "Civil Services (IAS/IPS) / Diplomat / Law Professional"
        elif comm > 80: return "Journalist / Content Strategist / Mass Media Lead"
        elif s2 > 80: return "Psychologist / Sociologist / Archeologist"
        else: return "Digital Marketer / Social Work Coordinator"

    return "Vocational Skills Specialist / General Consultant"

# --- 3. SIDEBAR MENU ---
st.sidebar.title("Navigation")
# Yahan Welcome Screen ko pehla option rakha hai
app_mode = st.sidebar.selectbox("Choose Mode", ["Welcome Screen", "12th Pass Student", "University/College Student"])

# --- 4. MAIN LOGIC HANDLING ---

# CASE 1: Welcome Screen
if app_mode == "Welcome Screen":
    st.title("🎓 Welcome to AI Career Predictor")
    st.markdown("""
    This tool helps students find their ideal career path.
    
    **How to use:**
    1. Select a mode from the **Sidebar** on the left.
    2. **12th Pass Student:** For high school graduates looking for university courses.
    3. **University Student:** For detailed academic analysis and career prediction.
    """)
    st.image("https://thumbs.dreamstime.com/b/career-development-flat-isometric-vector-concept-businessman-climbing-to-goal-stairs-look-like-word-career-104605641.jpg", width=700)

# CASE 2: 12th Pass Student Logic
elif app_mode == "12th Pass Student":
    st.title("🎓 12th Pass Career Counseling")
    st.write("Results change dynamically based on your stream and marks.")
    
    stream = st.selectbox("Select your 12th Stream", ["PCM", "PCB", "Commerce", "Arts"])
    
    col1, col2 = st.columns(2)
    with col1:
        m1 = st.slider("Subject 1 Marks (e.g. Maths/Bio/Accounts)", 0, 100, 75)
        m2 = st.slider("Subject 2 Marks (e.g. Physics/Chem/Economics)", 0, 100, 65)
    with col2:
        comm = st.slider("Communication/English Skills", 0, 100, 70)
    
    # DYNAMIC LOGIC FOR 12TH
    # 1. Pehle button banayein (Sabse bahar)
    if st.button("Suggest My Career"):
        res = ""
        career_goal = ""
        # ---------------------------------------------------------
        # PCM (Maths=m1, Tech=m2, Comm=comm)
        # ---------------------------------------------------------
        if stream == "PCM":
            # --- ZONE 1: ELITE (85-100) ---
          
            avg = (m1 + m2 + comm) / 3

            # --- ZONE 1: ELITE (Marks > 85) ---
            if m1 >= 85 and m2 >= 85 and comm >= 80:
                res = "B.Tech AI & Data Science / Robotics (IIT/NIT Tier)"
                career_goal = "Next-Gen Tech Innovator" 
                        
            # --- ZONE 2: HIGH TECH & ENGINEERING (Marks > 75) ---
            elif m1 >= 75 and m2 >= 75:
                if comm >= 70:
                    res = "B.Tech Computer Science / Software Engineering"
                    career_goal = "Expert Software Architect"
                else:
                    res = "B.Tech Mechanical / Civil Engineering"
                    career_goal = "Core Infrastructure Engineer"
                    
            # --- ZONE 3: AVIATION & COMMUNICATION (Comm High) ---
            elif comm >= 75:
                if m1 >= 60:
                    res = "B.Sc Aviation (Commercial Pilot) / Aerospace Management"
                    career_goal = "Senior Captain / Flight Operations Manager"
                else:
                    res = "B.Sc Hospitality / Luxury Hotel Management / Cabin Crew"
                    career_goal = "International Service Manager"

            # --- ZONE 4: CREATIVE & DIGITAL (Avg > 60) ---
            elif avg >= 60:
                if m2 >= 65:
                    res = "B.Des (UI-UX) / Game Development / Animation"
                    career_goal = "Digital Creative Director"
                else:
                    res = "BCA / B.Sc IT / Digital Marketing"
                    career_goal = "Systems Specialist" 

            # --- ZONE 5: PRACTICAL DIPLOMA (Avg > 45) ---
            elif avg >= 45:
                if m1 > m2:
                    res = "Diploma in Civil Engineering / Architecture"
                    career_goal = "Infrastructure Site Lead"
                else:
                    res = "Diploma in Automobile / Mechanical Engineering"
                    career_goal = "Technical Supervisor"

            # --- ZONE 6: VOCATIONAL (Low Marks) ---
            elif avg >= 35:
                res = "B.Voc Software Development / Cyber Security Diploma"
                career_goal = "Vocational Technical Specialist"

            # --- ZONE 7: SAFETY FALLBACK (Else) ---
            else:
                res = "Diploma in Industrial Safety / Fire & Security"
                career_goal = "Safety Officer / Operations Manager"
        # ---------------------------------------------------------
        # PCB (Bio=m1, Lab/Chem=m2, Comm=comm)
        # ---------------------------------------------------------
        elif  stream == "PCB":
            # 1. ELITE DOCTOR/RESEARCHER (All 85+)
            if m1 >= 85 and m2 >= 85 and comm >= 80:
                res = "MBBS / Genetics & Genomic Research"
                career_goal = "Specialist Surgeon ya Medical Scientist"
            
            # 2. CORE MEDICAL (Bio/Lab High, Comm Mid)
            elif m1 >= 80 and m2 >= 80 and comm < 75:
                res = "BDS (Dental) / B.Pharma (Research)"
                career_goal = "Specialized Medical Practitioner"
            
            # 3. MEDICAL MANAGEMENT (Bio/Comm High, Lab Mid)
            elif m1 >= 75 and comm >= 80 and m2 < 75:
                res = "Hospital Administration / Health Management"
                career_goal = "Healthcare Executive ya Hospital CEO"

            # 4. CLINICAL SPECIALIST (Bio Mid, Lab/Comm High)
            elif m1 < 75 and m2 >= 75 and comm >= 75:
                res = "B.Sc Forensic Science / Clinical Psychology"
                career_goal = "Forensic Investigator ya Therapist"

            # 5. BALANCED MID (60-75 Range)
            elif 60 <= m1 <= 75 and 60 <= m2 <= 75:
                res = "B.Sc Nursing / Physiotherapy (BPT)"
                career_goal = "Healthcare Professional / Clinic Manager"

            # 6. MIXED: RESEARCH STRENGTH (Bio High, Others Low)
            elif m1 >= 75 and m2 < 60:
                res = "B.Sc Biotechnology / Microbiology"
                career_goal = "Biological Researcher / Lab Specialist"

            # 7. LOW MARKS + GOOD COMM (Marks < 50, Comm > 70)
            elif (m1 < 55 or m2 < 55) and comm >= 70:
                res = "Nutrition & Dietetics / Wellness Coaching"
                career_goal = "Lifestyle Consultant ya Health PR"

            # 8. PHARMA OPERATIONS (Lab behtar hai, Range 40-55)
            elif m2 > m1 and 40 <= m2 < 60:
                res = "D.Pharma / Medical Lab Technology (MLT)"
                career_goal = "Pharmaceutical Associate / Lab Tech"

            # 9. VOCATIONAL HEALTH (35-50 Range)
            elif 35 <= m1 <= 50 and 35 <= m2 <= 50:
                res = "B.Voc in Healthcare / Emergency Medical Tech"
                career_goal = "Emergency Care Specialist"

            # 10. SKILL-BASED (Extreme Low < 40)
            elif m1 < 40 and m2 < 40:
                res = "Sanitary Inspector / Healthcare Assistant"
                career_goal = "Public Health Support Staff"

            else:
                res = "Diploma in Ayurvedic Medicine / Yoga Science"
                career_goal = "Alternative Medicine Practitioner"

        # ---------------------------------------------------------
        # COMMERCE (Accounts=m1, Business=m2, Comm=comm)
        # ---------------------------------------------------------
        elif stream == "Commerce":
            # 1. FINANCE ELITE (All 85+)
            if m1 >= 85 and m2 >= 85 and comm >= 85:
                res = "CA + Investment Banking / IPM (IIM)"
                career_goal = "Global Finance Leader / Corporate Strategist"
            
            # 2. CORE ACCOUNTS (Accounts/Business High, Comm Low)
            elif m1 >= 80 and m2 >= 80 and comm < 75:
                res = "Chartered Accountancy (CA) / CS / CMA"
                career_goal = "Audit Expert ya Finance Controller"
            
            # 3. BUSINESS LEADERSHIP (Business/Comm High, Accounts Mid)
            elif m2 >= 80 and comm >= 80 and m1 < 75:
                res = "BBA in Entrepreneurship / International Business"
                career_goal = "Start-up Founder ya Business Head"

            # 4. CORPORATE LAW/COMPLIANCE (Accounts/Comm High)
            elif m1 >= 75 and comm >= 80 and m2 < 70:
                res = "Company Secretary (CS) / Corporate Law"
                career_goal = "Legal & Compliance Manager"

            # 5. BALANCED MID (60-75 Range)
            elif 60 <= m1 <= 75 and 60 <= m2 <= 75:
                res = "B.Com (Hons) / Banking & Insurance"
                career_goal = "Financial Professional / Bank Officer"

            # 6. MIXED: ANALYTICAL STRENGTH (Accounts High, Others Low)
            elif m1 >= 80 and m2 < 60:
                res = "B.Stat / Actuarial Science / Tax Consultant"
                career_goal = "Risk Analyst ya Statistics Expert"

            # 7. LOW MARKS + GOOD COMM (Marks < 55, Comm > 75)
            elif (m1 < 55 or m2 < 55) and comm >= 75:
                res = "Mass Communication / PR & Advertising"
                career_goal = "Public Relations Head / Brand Manager"

            # 8. DIGITAL BUSINESS (Business Logic better, Range 45-60)
            elif m2 > m1 and 45 <= m2 < 65:
                res = "B.Voc Digital Marketing / E-commerce Ops"
                career_goal = "Digital Business Associate"

            # 9. VOCATIONAL COMMERCE (35-50 Range)
            elif 35 <= m1 <= 50 and 35 <= m2 <= 50:
                res = "Diploma in Banking / Retail Management"
                career_goal = "Retail Store Manager"

            # 10. EXTREME LOW (Below 40)
            elif m1 < 40 and m2 < 40:
                res = "Stock Market Trading Assistant / Data Entry"
                career_goal = "Self-Employed Financial Associate"

            else:
                res = "Diploma in Office Administration"
                career_goal = "Office Operations Manager"
        # ---------------------------------------------------------
        # ARTS (Theory=m1, Design=m2, Comm=comm)
        # ---------------------------------------------------------
        elif stream == "Arts":
            # 1. ELITE LAW/POLITICS (All 85+)
            if m1 >= 85 and comm >= 90:
                res = "Corporate Law (CLAT) / International Relations"
                career_goal = "Diplomat ya Supreme Court Lawyer"
            
            # 2. CREATIVE DIRECTOR (Design/Comm High, History Mid)
            elif m2 >= 85 and comm >= 85 and m1 < 75:
                res = "B.Des (Fashion/Interior/Graphic) / NIFT / NID"
                career_goal = "Creative Director / Design Head"
            
            # 3. MEDIA & JOURNALISM (Comm High, Others Mid-Low)
            elif comm >= 85 and m1 < 75 and m2 < 75:
                res = "BJMC (Journalism) / Mass Communication"
                career_goal = "National Media Anchor / Journalist"

            # 4. ACADEMIC RESEARCHER (History High, Others Low)
            elif m1 >= 80 and comm < 70:
                res = "B.A. (Hons) Psychology / Archaeology"
                career_goal = "Research Scholar ya Museologist"

            # 5. BALANCED MID (60-75 Range)
            elif 60 <= m1 <= 75 and 60 <= m2 <= 75:
                res = "Liberal Arts / Social Work (BSW)"
                career_goal = "Social Scientist / Content Specialist"

            # 6. MIXED: VISUAL ARTS (Design High, Comm Low)
            elif m2 >= 80 and comm < 60:
                res = "Fine Arts (BFA) / Animation & VFX"
                career_goal = "Professional Artist / VFX Specialist"

            # 7. LOW MARKS + GOOD COMM (Marks < 50, Comm > 80)
            elif (m1 < 50 or m2 < 50) and comm >= 80:
                res = "Radio Jockeying / Acting / Tourism Management"
                career_goal = "Media Personality / Travel Lead"

            # 8. TEACHING & EDUCATION (History Mid-Low, Range 45-60)
            elif m1 >= 50 and m1 < 65:
                res = "B.El.Ed / Integrated B.A.-B.Ed"
                career_goal = "Academic Educator / Counselor"

            # 9. VOCATIONAL ARTS (35-50 Range)
            elif 35 <= m1 <= 50 and 35 <= m2 <= 50:
                res = "Vocational in Event Management / Photography"
                career_goal = "Professional Event Coordinator"

            # 10. EXTREME LOW (Below 40)
            elif m1 < 40 and m2 < 40:
                res = "Handicrafts & Design / Calligraphy"
                career_goal = "Creative Artisan"

            else:
                res = "B.A. General Program"
                career_goal = "General Services Professional"

        # Result show karein
        st.success(f"### ✅ Recommended Course: {res}")
        st.info(f"**🎯 Career Goal:** {career_goal}")

# CASE 3: University Student Logic (CSV file )
else:
    st.title("🏢 University Career Analysis Dashboard")
    
    try:
        df = pd.read_csv('Students_Data.csv')
        search_code = st.number_input("Enter Student ID (101-120)", min_value=1, step=1)
        
        student = df[df['Student_Code'] == search_code]
        
        if not student.empty:
            row = student.iloc[0]
            sub1, sub2 = get_subject_names(row['Course'])
            
            # Dashboard Layout
            st.header(f"Report for {row['Student_Name']}")
            st.info(f"Department: {row['Course']}")
            
            m1, m2, m3, m4 = st.columns(4)
            m1.metric(sub1, row['Skill_1'])
            m2.metric(sub2, row['Skill_2'])
            m3.metric("Communication", row['Communication'])
            m4.metric("Attendance", f"{row['Attendance']}%")

            # Career Result
            career = predict_career(row['Skill_1'], row['Skill_2'], row['Communication'], row['Course'])
            st.markdown(f"### 🎯 Suggested Path: **{career}**")
            
            # Attendance Case Study
            # --- Compassionate Analysis Logic ---
            st.subheader("💡 Student Context Analysis")

            s1 = row['Skill_1']
            s2 = row['Skill_2']
            comm = row['Communication']
            attn = row['Attendance']
            rem = str(row['Attendance_Remark']).strip().lower()

            # 1. PEHLE SABSE BEST STUDENT CHECK KAREIN (Condition 4 ko upar le aaye)
            if s1 >= 80 and s2 >= 80 and attn >= 75:
                st.success("**Excellence Remark:** Consistent performer with great discipline. Ideal candidate for leadership roles.")

            # 2. PHIR MEDICAL/FAMILY WALA (Resilience)
            elif s1 >= 70 and s2 >= 70 and attn < 75 and (rem.lower() in ['medical', 'family', 'academic']):
                st.info(f"**Resilience Remark:** Student demonstrates high potential despite {rem} challenges.")

            # 3. PHIR DISCIPLINE WALA (High marks but no reason for low attendance)
            elif s1 >= 70 and s2 >= 70 and attn < 75:
                st.warning("**Discipline Remark:** Academic performance is strong, but low attendance needs attention.")
                
            # Condition: Regular Attendance par Marks kam (Academic Support)
            elif attn >= 75 and (s1 < 80 or s2 < 80):
                st.error("**Sincere Performer:** Student is highly regular and disciplined. With a bit more focus on core technical concepts, they can easily reach the Excellence category.")
            # 4. PHIR CRITICAL WALA (Low marks + Low attendance)
            elif (s1 < 50 or s2 < 50) and attn < 60:
                st.error("**Critical Support Needed:** Student is at risk. Urgent counseling required.")

            else:
                st.write("Student is performing within expected parameters.")

            # Charts
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar([sub1, sub2, "Communication", "Attendance"], 
                   [row['Skill_1'], row['Skill_2'], row['Communication'], row['Attendance']], 
                   color=['#007BFF', '#28A745', '#FFC107', '#DC3545'])
            
            st.pyplot(fig)

        else:
            st.error("Student ID not found in database.")
            
            # Dynamic Manual Entry Section
            with st.expander("Manual Entry Mode (For new students)"):
                m_name = st.text_input("Full Name")
                m_course = st.selectbox("Select Course", ["B.Tech", "BCA", "BBA", "B.Com", "BA", "B.Sc", "Polytechnic", "Diploma"])
                m_remark = st.selectbox("Reason for Low Attendance (if any)", ["None", "Medical", "Family", "Academic", "Other"])
                m_sub1, m_sub2 = get_subject_names(m_course)
                
                c1, c2, c3, c4 = st.columns(4)
                in1 = c1.number_input(f"{m_sub1} Marks", 0, 100)
                in2 = c2.number_input(f"{m_sub2} Marks", 0, 100)
                in3 = c3.number_input("Comm. Marks", 0, 100)
                in4 = c4.number_input("Attendance %", 0, 100)
                
                if st.button("Generate Manual Analysis"):
                    m_career = predict_career(in1, in2, in3, m_course)
                    st.success(f"Analysis Complete for {m_name}! Recommended: {m_career}")
                    
                    # 2. NAYA LOGIC: Attendance Insight dikhane ke liye
                    st.subheader("💡 Student Context Analysis")
                    rem = m_remark.lower()
                    
                    if in4 < 75 and (rem in ['medical', 'family']):
                        st.info(f"**Resilience Remark:** Student has potential but missed classes due to {m_remark} issues.")
                    elif in1 >= 80 and in2 >= 80 and in4 >= 75:
                        st.success("**Excellence Remark:** Consistent performer with great discipline.")
                    elif (in1 >= 70 or in2 >= 70) and in4 < 75:
                        st.warning("**Discipline Alert:** Performance is good, but attendance needs attention.")
                    elif in4 >= 75 and (in1 < 50 or in2 < 50):
                        st.error("**Sincere Performer:** Regular but needs focus on technical concepts.")
                    elif (in1 < 50 and in2 < 50) and in4 < 60:
                        st.error("**Critical Status:** Low marks and low attendance. High risk.")
                    else:
                        st.write("Student is performing within expected parameters.")

                    # 3. CHART: Isko button ke 'if' ke andar hi rakhein
                    fig2, ax2 = plt.subplots()
                    ax2.bar([m_sub1, m_sub2, "Comm", "Attendance"], [in1, in2, in3, in4], 
                            color=['#3498db', '#2ecc71', '#f39c12', '#e74c3c'])
                    st.pyplot(fig2)
    except Exception as e:
        st.error(f"Error: {e}")

        