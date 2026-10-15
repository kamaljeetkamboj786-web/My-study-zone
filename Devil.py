import streamlit as st
import json
from pathlib import Path
from datetime import date

st.set_page_config(
    page_title="BCA Bloom",
    page_icon="🌷",
    layout="wide"
)

# ---------- BEAUTIFUL UI ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

.stApp {
    background: linear-gradient(
        135deg, #fff5f8, #f4f0ff, #effffc
    );
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
}

.hero {
    background: linear-gradient(
        110deg, #292544, #7868e6, #f36b9a
    );
    padding: 30px;
    border-radius: 25px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 42px;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 18px;
    border: 1px solid #eee5fa;
}

div[data-testid="stExpander"] {
    background: #ffffffdd;
    border-radius: 15px;
    border: 1px solid #e9e2f7;
    margin-bottom: 10px;
}

.stButton > button {
    background: linear-gradient(90deg, #7868e6, #f36b9a);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 18px;
    font-weight: bold;
}

.study-card {
    background: white;
    padding: 16px;
    border-radius: 15px;
    margin: 8px 0;
    border: 1px solid #eee5fa;
}
</style>
""", unsafe_allow_html=True)


# ---------- DATA ----------
SUBJECTS = [
    "Computer Architecture",
    "Operating Systems",
    "Information Systems",
    "Cybersecurity Fundamentals",
    "Data Structures & File Processing Lab"
]

EXAM_DATE = date(2026, 11, 18)

DATA_FILE = Path("study_progress.json")


def load_data():
    try:
        if DATA_FILE.exists():
            data = json.loads(
                DATA_FILE.read_text(encoding="utf-8")
            )
            if isinstance(data, dict):
                return data
    except (OSError, json.JSONDecodeError):
        pass

    return {
        "completed": [],
        "hours": {},
        "notes": {},
        "topics": {}
    }


def save_data(data):
    try:
        DATA_FILE.write_text(
            json.dumps(data, indent=2),
            encoding="utf-8"
        )
        return True
    except OSError:
        return False


data = load_data()

# ---------- HEADER ----------
days_left = max(0, (EXAM_DATE - date.today()).days)

st.markdown("""
<div class="hero">
    <h1>🌷 BCA Bloom</h1>
    <h3 style="color:white">
        Your Personal Exam Preparation Companion
    </h3>
    <p>Small steps every day. Big confidence on exam day.</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

c1.metric("📅 Days to Exam", days_left)
c2.metric("⏰ Daily Study Goal", "4 Hours")
c3.metric("📚 Total Subjects", len(SUBJECTS))


# ---------- NAVIGATION ----------
tabs = st.tabs([
    "🏡 My Day",
    "🗓️ Timetable",
    "🌿 Syllabus",
    "📄 GNDU Papers",
    "📈 My Progress",
    "🧩 Practice"
])


# ---------- MY DAY ----------
with tabs[0]:

    st.header("🌸 Your Daily Study Plan")

    today = date.today()
    selected_date = st.date_input(
        "Select study date",
        value=today
    )

    st.info(
        "Study for 4 hours daily. "
        "Take short breaks between sessions."
    )

    tasks = [
        ("🧠 Computer Architecture", 60),
        ("⚙️ Operating Systems", 60),
        ("💡 Information Systems", 45),
        ("🛡️ Cybersecurity", 35),
        ("💻 Data Structures Lab", 40)
    ]

    completed_count = 0

    for subject, minutes in tasks:

        key = f"{selected_date}_{subject}"

        if key not in data["completed"]:
            data["completed"].append(key)

        checked = st.checkbox(
            f"{subject} — {minutes} minutes",
            key=f"task_{selected_date}_{subject}"
        )

        if checked:
            completed_count += 1

    st.progress(completed_count / len(tasks))

    st.write(
        f"Completed: {completed_count}/{len(tasks)} tasks"
    )

    note = st.text_area(
        "📝 Today's notes",
        placeholder="Write important points or topics to revise..."
    )

    if st.button("💾 Save Today's Progress"):
        data["notes"][str(selected_date)] = note

        if save_data(data):
            st.success("Your progress has been saved!")
        else:
            st.error("Unable to save. Please try again.")


# ---------- TIMETABLE ----------
with tabs[1]:

    st.header("🗓️ Four-Hour Timetable")

    timetable = [
        ("🧠", "Computer Architecture", "60 minutes"),
        ("⚙️", "Operating Systems", "60 minutes"),
        ("💡", "Information Systems", "45 minutes"),
        ("🛡️", "Cybersecurity Fundamentals", "35 minutes"),
        ("💻", "Data Structures Lab", "40 minutes")
    ]

    for emoji, subject, duration in timetable:
        st.markdown(
            f"""
            <div class="study-card">
                <h4>{emoji} {subject}</h4>
                <p>⏰ Study time: {duration}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success(
        "Tip: Spend the final 10 minutes recalling "
        "what you learned without looking at your notes."
    )


# ---------- SYLLABUS ----------
with tabs[2]:

    st.header("🌿 Subject-wise Syllabus Checklist")

    syllabus = {
        "Computer Architecture": [
            "Register Transfer Language",
            "Micro-operations",
            "Instruction Cycle",
            "Register Organisation",
            "Hardwired and Microprogrammed Control",
            "RISC and CISC",
            "Memory Hierarchy and Cache",
            "Input/Output Organisation",
            "DMA and Interrupts",
            "Pipelining"
        ],

        "Operating Systems": [
            "Introduction to Operating Systems",
            "Processes and Threads",
            "CPU Scheduling",
            "Process Synchronisation",
            "Memory Management",
            "Virtual Memory",
            "Page Replacement",
            "Deadlocks",
            "OS Security"
        ],

        "Information Systems": [
            "Information Systems Fundamentals",
            "Management Information Systems",
            "Decision Support Systems",
            "Executive Support Systems",
            "Knowledge Management",
            "Supply Chain Management",
            "Customer Relationship Management",
            "E-commerce"
        ],

        "Cybersecurity Fundamentals": [
            "CIA Triad",
            "Authentication and Authorization",
            "Malware and Ransomware",
            "Phishing and Social Engineering",
            "Encryption",
            "Digital Signatures",
            "Privacy and Security",
            "Cybercrime and IT Law"
        ],

        "Data Structures & File Processing Lab": [
            "Arrays and Strings",
            "Linear and Binary Search",
            "Linked Lists",
            "Stacks and Queues",
            "Trees and BST",
            "Sorting Algorithms",
            "Graph Traversal",
            "File Handling"
        ]
    }

    for subject, topics in syllabus.items():

        with st.expander(f"📚 {subject}"):

            completed = 0

            for index, topic in enumerate(topics):

                key = f"{subject}_{index}"

                if key not in data["topics"]:
                    data["topics"][key] = False

                data["topics"][key] = st.checkbox(
                    topic,
                    value=data["topics"][key],
                    key=f"syllabus_{key}"
                )

                if data["topics"][key]:
                    completed += 1

            st.progress(completed / len(topics))

            st.caption(
                f"{completed}/{len(topics)} topics completed"
            )

    if st.button("💾 Save Syllabus Progress"):
        if save_data(data):
            st.success("Syllabus progress saved!")


# ---------- GNDU PAPERS ----------
with tabs[3]:

    st.header("📄 GNDU Previous Question Papers")

    st.warning(
        "These external links are references. "
        "Verify the paper code and semester before studying."
    )

    papers = [
        (
            "GNDU BCA Previous Papers",
            "https://www.gnduonline.com/bca.html"
        ),
        (
            "Computer Architecture Paper — 2024",
            "https://www.gnduonline.com/papers/"
            "bca-3-sem-computer-architecture-101884-2024.html"
        ),
        (
            "Computer Architecture Paper — 2022",
            "https://www.gnduonline.com/papers/"
            "bca-3-sem-computer-architecture-1675-2022.html"
        ),
        (
            "GNDU Official Syllabus",
            "https://collegeadmissions.gndu.ac.in/Syllabus/"
        )
    ]

    for title, url in papers:
        st.markdown(f"### 📘 {title}")
        st.markdown(f"[Open resource ↗]({url})")
        st.divider()


# ---------- PROGRESS ----------
with tabs[4]:

    st.header("📈 Your Progress Dashboard")

    study_date = st.date_input(
        "Date",
        value=date.today(),
        key="progress_date"
    )

    hours = st.slider(
        "How many hours did you study?",
        0.0,
        8.0,
        0.0,
        0.5
    )

    if st.button("Save Study Hours"):

        data["hours"][str(study_date)] = hours

        if save_data(data):
            st.success("Study hours saved!")

    total_hours = sum(data["hours"].values())

    st.metric("⏰ Total Recorded Study Hours", total_hours)

    st.caption(
        "Consistency matters more than studying "
        "for very long hours on one day."
    )


# ---------- PRACTICE ----------
with tabs[5]:

    st.header("🧩 Practice Zone")

    questions = {
        "Computer Architecture": [
            "Explain the instruction cycle.",
            "Compare RISC and CISC.",
            "Explain cache memory."
        ],
        "Operating Systems": [
            "Explain process states.",
            "What is a semaphore?",
            "Explain deadlock."
        ],
        "Information Systems": [
            "Explain MIS.",
            "Differentiate MIS and DSS.",
            "Explain knowledge management."
        ],
        "Cybersecurity Fundamentals": [
            "Explain the CIA triad.",
            "What is phishing?",
            "Compare symmetric and asymmetric encryption."
        ],
        "Data Structures & File Processing Lab": [
            "Write a linear search program.",
            "Implement a stack using arrays.",
            "Explain binary search."
        ]
    }

    selected_subject = st.selectbox(
        "Choose your subject",
        SUBJECTS
    )

    for i, question in enumerate(
        questions[selected_subject], 1
    ):

        st.markdown(f"**Question {i}:** {question}")

        st.text_area(
            "Write your answer",
            key=f"answer_{selected_subject}_{i}"
        )

        st.divider()


# ---------- FOOTER ----------
st.markdown("---")

st.markdown(
    "<center>🌷 BCA Bloom | Keep learning, keep growing.</center>",
    unsafe_allow_html=True
)
