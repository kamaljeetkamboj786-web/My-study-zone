import streamlit as st
from datetime import date, timedelta
import json
from pathlib import Path

st.set_page_config(page_title="BCA Exam Buddy", page_icon="📚", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1.3rem; padding-bottom: 2rem; max-width: 1100px;}
h1, h2, h3 {letter-spacing: -0.02em;}
div[data-testid="stMetric"] {background: #f5f7fb; padding: 12px; border-radius: 12px;}
</style>
""", unsafe_allow_html=True)

DATA_FILE = Path("study_progress.json")
START = date(2026, 10, 14)
EXAM_START = date(2026, 11, 18)

SUBJECTS = [
    "Computer Architecture",
    "Operating Systems",
    "Information Systems",
    "Cybersecurity Fundamentals",
    "Data Structures & File Processing Lab",
]

# Date-wise combined plan: one topic for each of the five subjects each day.
PLAN = [
("2026-10-14","RTL and registers","OS introduction and types","Information concepts and systems","Internet, IP/MAC addresses","Arrays"),
("2026-10-15","Register types and common bus","Processes and process states","Business information systems","Client-server, P2P and cloud computing","Linear search"),
("2026-10-16","Multiplexers","IPC and threads","IS in society and industry","CIA triad","Binary search"),
("2026-10-17","Logic micro-operations","CPU scheduling basics","Organizations and information systems","Authentication and authorization","Strings"),
("2026-10-18","Arithmetic micro-operations","Scheduling algorithms","Competitive advantage","Malware, viruses and worms","Linked lists"),
("2026-10-19","Shift micro-operations","Scheduling criteria and evaluation","Careers in IS","Trojans, spam and spoofing","Stack using arrays"),
("2026-10-20","Register-transfer practice","Process and scheduling revision","Section A revision","Phishing and social engineering","Stack using linked lists"),
("2026-10-21","Instruction codes","Critical-section problem","Management fundamentals","Ransomware and spyware","Queue using arrays"),
("2026-10-22","Computer instructions","Semaphores","Management decisions","Adware and botnets","Queue using linked lists"),
("2026-10-23","Timing signals and instruction cycle","Synchronization problems","MIS and its role","DoS attacks and data breaches","Tree basics"),
("2026-10-24","Basic computer design","Multithreading and address spaces","MIS development pitfalls","Public Wi-Fi risks","BST traversals"),
("2026-10-25","General register organisation","Swapping and contiguous allocation","Building information systems","HTTPS and antivirus","BST insertion/search"),
("2026-10-26","Stack-organised CPU","Paging and segmentation","Maintaining information systems","Password managers and secure Wi-Fi","AVL tree basics"),
("2026-10-27","Instruction formats","Memory management revision","IS security and control","Updates and patches","B-tree basics"),
("2026-10-28","Addressing modes","Virtual memory","DSS foundations","Encryption and decryption","Bubble sort"),
("2026-10-29","Program control","Demand paging","DSS concepts and software","Public/private-key cryptography","Selection sort"),
("2026-10-30","Hardwired control unit","Page-replacement algorithms","DSS strategies","Digital signatures","Insertion sort"),
("2026-10-31","Microprogrammed control and Wilkes' design","Thrashing","Group Support Systems","Backup and recovery","Quick sort"),
("2026-11-01","RISC and CISC","Deadlock characterisation","Executive Support Systems","Backup types","Merge sort"),
("2026-11-02","RISC vs CISC comparison","Deadlock prevention and avoidance","Expert systems and DSS integration","URL filtering and patches","Heap sort"),
("2026-11-03","Architecture Sections A-B revision","Deadlock detection and recovery","Knowledge-management fundamentals","Privacy vs security vs anonymity","Graph traversal"),
("2026-11-04","Memory hierarchy","OS security and access control","Knowledge-management process","Incognito and Tor","Shortest path"),
("2026-11-05","Main and auxiliary memory","Password vulnerabilities","Knowledge spiral","Social-media privacy","File handling"),
("2026-11-06","Associative and cache memory","Windows/Linux case study","Knowledge repositories and databases","Cybercrime and IT Act","Practise arrays/searching"),
("2026-11-07","Virtual memory","OS Sections A-B revision","Knowledge-sharing practices","Intellectual property and licensing","Practise strings/linked lists"),
("2026-11-08","I/O interface","Memory and deadlock revision","SCM and CRM","Laws and compliance","Stack/queue programs"),
("2026-11-09","Modes of transfer, interrupts","Scheduling and synchronization revision","E-commerce and mobile commerce","Threat revision","Trees and sorting"),
("2026-11-10","DMA, I/O processor, pipelining, vector/parallel processing","Full syllabus test","Full syllabus revision","Full syllabus test","Graphs and file handling"),
("2026-11-11","Section A revision","Section A revision","Section A revision","Section A revision","Arrays and searching"),
("2026-11-12","Section B revision","Section B revision","Section B revision","Section B revision","Linked lists, stacks, queues"),
("2026-11-13","Section C revision","Section C revision","Section C revision","Section C revision","Trees and sorting"),
("2026-11-14","Section D revision","Section C revision","Section C revision","Section C revision","Graphs and shortest path"),
("2026-11-15","Mock test and corrections","Mock test and corrections","Section D revision","Section D revision","File handling and viva"),
("2026-11-16","Weak topics and diagrams","Weak topics and algorithms","Mock test and corrections","Full syllabus revision","Run important programs"),
("2026-11-17","Definitions and diagrams","Definitions and algorithms","Important questions","Important definitions and laws","Code and viva notes"),
]

PAPER_LINKS = [
    ("GNDU BCA previous-paper collection (third-party)", "https://www.gnduonline.com/bca.html"),
    ("Computer Architecture paper listing — 2024", "https://www.gnduonline.com/papers/bca-3-sem-computer-architecture-101884-2024.html"),
    ("Computer Architecture paper listing — 2022", "https://www.gnduonline.com/papers/bca-3-sem-computer-architecture-1675-2022.html"),
    ("GNDU official syllabus page", "https://collegeadmissions.gndu.ac.in/Syllabus/"),
]

SUBJECT_GUIDES = {
    "Computer Architecture": [
        "RTL, registers, common bus, multiplexers",
        "Logic, arithmetic and shift micro-operations",
        "Instruction codes, timing signals and instruction cycle",
        "Register organisation, stack CPU, instruction formats and addressing modes",
        "Hardwired/microprogrammed control, Wilkes' design, RISC vs CISC",
        "Memory hierarchy, cache, associative and virtual memory",
        "I/O interface, interrupts, DMA, pipelining, vector and parallel processing",
    ],
    "Operating Systems": [
        "Introduction, OS types and services",
        "Processes, states, IPC and threads",
        "CPU scheduling and algorithms",
        "Critical sections, semaphores and synchronization",
        "Memory allocation, paging, segmentation and virtual memory",
        "Demand paging, page replacement and thrashing",
        "Deadlocks: prevention, avoidance, detection and recovery",
        "Protection, security and Windows/Linux case study",
    ],
    "Information Systems": [
        "Information, systems and business information systems",
        "Organizations, competitive advantage and IS careers",
        "MIS, management decisions and development pitfalls",
        "Building/maintaining information systems; security and control",
        "DSS, Group Support Systems, ESS and expert systems",
        "Knowledge management, repositories, knowledge sharing and collaboration",
        "SCM, CRM, e-commerce and mobile commerce",
    ],
    "Cybersecurity Fundamentals": [
        "Internet, IP/MAC, client-server/P2P and cloud computing",
        "CIA triad, authentication and authorization",
        "Malware, phishing, spoofing, ransomware, spyware and botnets",
        "DoS, data breaches, social engineering and public Wi-Fi risks",
        "HTTPS, antivirus, passwords, updates, encryption and digital signatures",
        "Privacy, security, anonymity, backups and safe browsing",
        "Cybercrime, IT Act, intellectual property, licensing and compliance",
    ],
    "Data Structures & File Processing Lab": [
        "Arrays, strings, linear and binary search",
        "Linked lists",
        "Stacks and queues using arrays and linked lists",
        "Trees, BST, AVL/B-tree basics and traversals",
        "Bubble, selection, insertion, quick, merge and heap sort",
        "Graphs, traversal and shortest path",
        "File handling, program tracing and viva",
    ],
}

PRACTICE_QUESTIONS = {
    "Computer Architecture": [
        "Explain register transfer language with examples.",
        "Explain the instruction cycle with a diagram.",
        "Compare hardwired and microprogrammed control units.",
        "Explain cache memory and memory hierarchy.",
        "Explain DMA and interrupt-driven I/O.",
    ],
    "Operating Systems": [
        "Explain process states and process scheduling.",
        "Explain semaphores and the critical-section problem.",
        "Compare paging and segmentation.",
        "Explain page-replacement algorithms.",
        "Explain deadlock prevention, avoidance and recovery.",
    ],
    "Information Systems": [
        "Explain MIS and its role in management decisions.",
        "Compare MIS, DSS and ESS.",
        "Explain knowledge management and knowledge repositories.",
        "Explain SCM and CRM.",
        "Discuss information-system security and control.",
    ],
    "Cybersecurity Fundamentals": [
        "Explain the CIA triad with examples.",
        "Differentiate viruses, worms, Trojans and ransomware.",
        "Explain phishing and social engineering.",
        "Compare symmetric and asymmetric encryption.",
        "Discuss cybercrime, privacy and the IT Act topics in your syllabus.",
    ],
    "Data Structures & File Processing Lab": [
        "Write a C program for linear and binary search.",
        "Implement a stack using an array.",
        "Implement a queue using a linked list.",
        "Write tree traversal algorithms.",
        "Explain quick sort and merge sort with examples.",
    ],
}

def load_progress():
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except (json.JSONDecodeError, OSError):
            pass
    return {}

def save_progress(data):
    try:
        DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return True
    except OSError:
        return False

progress = load_progress()
progress.setdefault("topic_checks", {})
progress.setdefault("notes", {})
progress.setdefault("daily_hours", {})
progress.setdefault("scores", {})
progress.setdefault("done_dates", [])

st.title("📚 BCA Exam Buddy")
st.write("**Your all-in-one study companion** • Exams start 18 November 2026 • 5 subjects • 4 hours/day")
today = date.today()
days_left = (EXAM_START - today).days
m1, m2, m3 = st.columns(3)
m1.metric("Exam date", "18 Nov 2026")
m2.metric("Days remaining", max(0, days_left))
m3.metric("Daily target", "4 hours")

with st.sidebar:
    st.header("My subjects")
    for name in SUBJECTS:
        st.write(f"• {name}")
    st.divider()
    st.markdown("### Daily time plan")
    st.write("Computer Architecture — 60 min")
    st.write("Operating Systems — 60 min")
    st.write("Information Systems — 45 min")
    st.write("Cybersecurity — 35 min")
    st.write("Data Structures Lab — 40 min")
    st.caption("Save your progress regularly. This first version uses a local JSON file.")

today_tab, plan_tab, syllabus_tab, papers_tab, tracker_tab, practice_tab = st.tabs([
    "🏠 Today", "🗓️ Day-wise plan", "📚 Syllabus checklist", "📄 GNDU papers", "📈 Progress", "✍️ Practice"
])

with today_tab:
    st.subheader("Today's focused plan")
    default_date = max(START, min(today, EXAM_START - timedelta(days=1)))
    chosen = st.date_input("Select date", value=default_date, min_value=START, max_value=EXAM_START - timedelta(days=1), key="chosen_day")
    row = next((x for x in PLAN if x[0] == chosen.isoformat()), None)
    if row:
        st.caption(chosen.strftime("%A, %d %B %Y"))
        tasks = [
            (SUBJECTS[0], row[1], 60),
            (SUBJECTS[1], row[2], 60),
            (SUBJECTS[2], row[3], 45),
            (SUBJECTS[3], row[4], 35),
            (SUBJECTS[4], row[5], 40),
        ]
        for subject, topic, minutes in tasks:
            with st.container(border=True):
                left, right = st.columns([4, 1])
                with left:
                    key = f"{chosen.isoformat()}::{subject}"
                    checked = st.checkbox(f"**{subject}**", value=progress["topic_checks"].get(key, False), key=f"check_{key}")
                    st.write(topic)
                    progress["topic_checks"][key] = checked
                with right:
                    st.metric("Minutes", minutes)
        st.markdown("#### Study method")
        st.write("1. Understand the topic in Hinglish.")
        st.write("2. Write a short English exam answer.")
        st.write("3. Recall the main points without notes.")
        st.write("4. Solve a question or practise a program.")
        st.write("5. Note mistakes for revision.")
        note_key = chosen.isoformat()
        progress["notes"][note_key] = st.text_area("Mistakes / notes for this date", value=progress["notes"].get(note_key, ""), key=f"notes_{note_key}")
        if st.button("💾 Save today's progress", type="primary"):
            if save_progress(progress):
                st.success("Saved.")
            else:
                st.error("Could not save progress.")

with plan_tab:
    st.subheader("Combined daily timetable: 14 October – 17 November")
    st.info("This is a planning guide based on the syllabus topics discussed. Verify every unit against your current college syllabus.")
    for item in PLAN:
        d = date.fromisoformat(item[0])
        with st.expander(f"{d.strftime('%a, %d %b %Y')}"):
            st.write(f"**Computer Architecture:** {item[1]}")
            st.write(f"**Operating Systems:** {item[2]}")
            st.write(f"**Information Systems:** {item[3]}")
            st.write(f"**Cybersecurity Fundamentals:** {item[4]}")
            st.write(f"**Data Structures Lab:** {item[5]}")
            done = st.checkbox("Mark full day complete", value=item[0] in progress["done_dates"], key=f"full_day_{item[0]}")
            if done and item[0] not in progress["done_dates"]:
                progress["done_dates"].append(item[0])
            elif not done and item[0] in progress["done_dates"]:
                progress["done_dates"].remove(item[0])
    if st.button("Save day-wise progress"):
        if save_progress(progress):
            st.success("Calendar progress saved.")

with syllabus_tab:
    st.subheader("Subject-wise checklist")
    for subject, topics in SUBJECT_GUIDES.items():
        with st.expander(subject):
            for i, topic in enumerate(topics):
                key = f"syllabus::{subject}::{i}"
                progress["topic_checks"][key] = st.checkbox(topic, value=progress["topic_checks"].get(key, False), key=f"syll_{i}_{subject}")
    if st.button("Save syllabus checklist"):
        if save_progress(progress):
            st.success("Checklist saved.")

with papers_tab:
    st.subheader("GNDU previous-year paper references")
    st.warning("These are links, not embedded PDFs. The paper collection is third-party, not an official GNDU website. Verify subject, semester, paper code and syllabus year.")
    for label, url in PAPER_LINKS:
        st.markdown(f"- [{label}]({url})")
    st.markdown("### How to use previous papers")
    st.write("1. Download a paper only from a source you trust.")
    st.write("2. Match the paper code and syllabus with your college's current syllabus.")
    st.write("3. Attempt it with a timer before checking notes.")
    st.write("4. Mark questions you could not answer and revise those topics.")
    st.write("Older papers are practice references, not a guarantee of repeated questions.")

with tracker_tab:
    st.subheader("Study-hours and confidence tracker")
    completed = len(set(progress["done_dates"]))
    st.progress(completed / len(PLAN))
    st.write(f"**Full days marked complete:** {completed} / {len(PLAN)}")
    log_date = st.date_input("Date to record", value=today, key="log_date")
    hours = st.slider("Hours studied", 0.0, 8.0, float(progress["daily_hours"].get(log_date.isoformat(), 0.0)), 0.5)
    confidence = st.select_slider("How well could you answer without notes?", options=["Not tested", "Needs revision", "Okay", "Good", "Excellent"])
    if st.button("Save tracker entry"):
        progress["daily_hours"][log_date.isoformat()] = hours
        progress["scores"][log_date.isoformat()] = confidence
        if save_progress(progress):
            st.success("Tracker entry saved.")
    if progress["daily_hours"]:
        st.markdown("### Recent log")
        for day in sorted(progress["daily_hours"], reverse=True)[:10]:
            st.write(f"- {day}: {progress['daily_hours'][day]} hours • {progress['scores'].get(day, 'Not tested')}")

with practice_tab:
    st.subheader("Exam-style practice")
    chosen_subject = st.selectbox("Choose a subject", SUBJECTS)
    st.write("Try to answer from memory first. Then compare your answer with your notes and add missing points.")
    for i, question in enumerate(PRACTICE_QUESTIONS[chosen_subject], start=1):
        st.markdown(f"**{i}. {question}**")
        st.text_area("Write your answer / key points", key=f"answer_{chosen_subject}_{i}", height=90)
    st.info("These are practice prompts, not guaranteed exam questions. Use the full syllabus and previous papers too.")

st.divider()
st.caption("BCA Exam Buddy • Personal study aid • Always follow your official date sheet and latest college syllabus.")
