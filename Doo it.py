import streamlit as st
from datetime import date, timedelta
import json
from pathlib import Path

st.set_page_config(page_title="BCA Exam Buddy", page_icon="📚", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1rem; padding-bottom: 2rem; max-width: 1100px;}
.small-note {font-size: 0.9rem; color: #555;}
</style>
""", unsafe_allow_html=True)

START = date(2026, 10, 14)
EXAM_START = date(2026, 11, 18)
DATA_FILE = Path("study_progress.json")

SUBJECTS = [
    "Computer Architecture",
    "Operating Systems",
    "Information Systems",
    "Cybersecurity Fundamentals",
    "Data Structures & File Processing Lab",
]

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
    "Computer Architecture": ["RTL, registers, common bus, multiplexers", "Logic, arithmetic and shift micro-operations", "Instruction codes, timing signals and instruction cycle", "Register organisation, stack CPU, instruction formats and addressing modes", "Hardwired/microprogrammed control, Wilkes' design, RISC vs CISC", "Memory hierarchy, cache, associative and virtual memory", "I/O interface, interrupts, DMA, pipelining, vector and parallel processing"],
    "Operating Systems": ["Introduction, OS types and services", "Processes, states, IPC and threads", "CPU scheduling and algorithms", "Critical sections, semaphores and synchronization", "Memory allocation, paging, segmentation and virtual memory", "Demand paging, page replacement and thrashing", "Deadlocks: prevention, avoidance, detection and recovery", "Protection, security and Windows/Linux case study"],
    "Information Systems": ["Information, systems and business information systems", "Organizations, competitive advantage and IS careers", "MIS, management decisions and development pitfalls", "Building/maintaining information systems; security and control", "DSS, Group Support Systems, ESS and expert systems", "Knowledge management, repositories, knowledge sharing and collaboration", "SCM, CRM, e-commerce and mobile commerce"],
    "Cybersecurity Fundamentals": ["Internet, IP/MAC, client-server/P2P and cloud computing", "CIA triad, authentication and authorization", "Malware, phishing, spoofing, ransomware, spyware and botnets", "DoS, data breaches, social engineering and public Wi-Fi risks", "HTTPS, antivirus, passwords, updates, encryption and digital signatures", "Privacy, security, anonymity, backups and safe browsing", "Cybercrime, IT Act, intellectual property, licensing and compliance"],
    "Data Structures & File Processing Lab": ["Arrays, strings, linear and binary search", "Linked lists", "Stacks and queues using arrays and linked lists", "Trees, BST, AVL/B-tree basics and traversals", "Bubble, selection, insertion, quick, merge and heap sort", "Graphs, traversal and shortest path", "File handling, program tracing and viva"],
}

PRACTICE_QUESTIONS = {
    "Computer Architecture": ["Explain register transfer language with examples.", "Explain the instruction cycle with a diagram.", "Compare hardwired and microprogrammed control units.", "Explain cache memory and memory hierarchy.", "Explain DMA and interrupt-driven I/O."],
    "Operating Systems": ["Explain process states and process scheduling.", "Explain semaphores and the critical-section problem.", "Compare paging and segmentation.", "Explain page-replacement algorithms.", "Explain deadlock prevention, avoidance and recovery."],
    "Information Systems": ["Explain MIS and its role in management decisions.", "Compare MIS, DSS and ESS.", "Explain knowledge management and knowledge repositories.", "Explain SCM and CRM.", "Discuss information-system security and control."],
    "Cybersecurity Fundamentals": ["Explain the CIA triad with examples.", "Differentiate viruses, worms, Trojans and ransomware.", "Explain phishing and social engineering.", "Compare symmetric and asymmetric encryption.", "Discuss cybercrime, privacy and IT Act topics in your syllabus."],
    "Data Structures & File Processing Lab": ["Write a C program for linear and binary search.", "Implement a stack using an array.", "Implement a queue using a linked list.", "Write tree traversal algorithms.", "Explain quick sort and merge sort with examples."],
}

def load_progress():
    try:
        if DATA_FILE.exists():
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
    except (OSError, json.JSONDecodeError):
        pass
    return {"topic_checks": {}, "notes": {}, "daily_hours": {}, "scores": {}, "done_dates": []}

def save_progress(data):
    try:
        DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return True
    except OSError:
        return False

progress = load_progress()
for key, default in {"topic_checks": {}, "notes": {}, "daily_hours": {}, "scores": {}, "done_dates": []}.items():
    if not isinstance(progress.get(key), type(default)):
        progress[key] = default

st.title("📚 BCA Exam Buddy")
st.write("**Your all-in-one study companion** · Exams start 18 November 2026 · Five subjects · Four hours/day")
today = date.today()
days_left = max(0, (EXAM_START - today).days)
a, b, c = st.columns(3)
a.metric("Exam starts", "18 Nov 2026")
b.metric("Days remaining", days_left)
c.metric("Study target", "4 hours/day")

with st.sidebar:
    st.header("Your subjects")
    for subject in SUBJECTS:
        st.write("• " + subject)
    st.divider()
    st.caption("Daily target: 60 + 60 + 45 + 35 + 40 minutes = 4 hours.")

tabs = st.tabs(["🏠 Today", "🗓️ Timetable", "📚 Syllabus", "📄 GNDU papers", "📈 Progress", "✍️ Practice"])

with tabs[0]:
    st.subheader("Today's study")
    chosen = st.date_input("Choose a study date", value=max(START, min(today, EXAM_START - timedelta(days=1))), min_value=START, max_value=EXAM_START - timedelta(days=1))
    row = next((x for x in PLAN if x[0] == chosen.isoformat()), None)
    if row:
        tasks = [(SUBJECTS[0], row[1], 60), (SUBJECTS[1], row[2], 60), (SUBJECTS[2], row[3], 45), (SUBJECTS[3], row[4], 35), (SUBJECTS[4], row[5], 40)]
        for idx, (subject, topic, minutes) in enumerate(tasks):
            k = f"{chosen.isoformat()}::{subject}"
            progress["topic_checks"][k] = st.checkbox(f"{subject} — {topic} ({minutes} min)", value=bool(progress["topic_checks"].get(k, False)), key=f"daily_{chosen.isoformat()}_{idx}")
        note_key = chosen.isoformat()
        progress["notes"][note_key] = st.text_area("Mistakes / revision notes", value=progress["notes"].get(note_key, ""), key=f"note_{note_key}")
        if st.button("Save today's progress", type="primary"):
            st.success("Progress saved." if save_progress(progress) else "Could not save. Please check app storage.")

with tabs[1]:
    st.subheader("Day-wise combined timetable")
    st.info("Use this as a guide and verify topics against your latest college syllabus.")
    for item in PLAN:
        d = date.fromisoformat(item[0])
        with st.expander(d.strftime("%A, %d %B %Y")):
            for label, topic in zip(SUBJECTS, item[1:]):
                st.write(f"**{label}:** {topic}")
            is_done = st.checkbox("Mark day complete", value=item[0] in progress["done_dates"], key=f"day_{item[0]}")
            if is_done and item[0] not in progress["done_dates"]:
                progress["done_dates"].append(item[0])
            if not is_done and item[0] in progress["done_dates"]:
                progress["done_dates"].remove(item[0])
    if st.button("Save timetable progress"):
        st.success("Progress saved." if save_progress(progress) else "Could not save progress.")

with tabs[2]:
    st.subheader("Subject-wise syllabus checklist")
    for subject, topics in SUBJECT_GUIDES.items():
        with st.expander(subject):
            for i, topic in enumerate(topics):
                k = f"syllabus::{subject}::{i}"
                progress["topic_checks"][k] = st.checkbox(topic, value=bool(progress["topic_checks"].get(k, False)), key=f"syll_{i}")
    if st.button("Save syllabus checklist"):
        st.success("Checklist saved." if save_progress(progress) else "Could not save progress.")

with tabs[3]:
    st.subheader("GNDU previous-paper references")
    st.warning("These links are external references, not embedded PDFs. The paper collection is third-party. Verify subject, semester, paper code and syllabus year.")
    for label, url in PAPER_LINKS:
        st.markdown(f"- [{label}]({url})")
    st.write("Attempt a paper with a timer, check answers, and revise mistakes. Past papers are practice—not a guarantee of repeated questions.")

with tabs[4]:
    st.subheader("Study-hours tracker")
    d = st.date_input("Date to log", value=today, key="hours_date")
    hrs = st.slider("Hours studied", 0.0, 8.0, float(progress["daily_hours"].get(d.isoformat(), 0.0)), 0.5)
    confidence = st.select_slider("Self-test confidence", options=["Not tested", "Needs revision", "Okay", "Good", "Excellent"])
    if st.button("Save tracker entry"):
        progress["daily_hours"][d.isoformat()] = hrs
        progress["scores"][d.isoformat()] = confidence
        st.success("Tracker saved." if save_progress(progress) else "Could not save tracker.")
    done = len(set(progress["done_dates"]))
    st.write(f"**Days completed:** {done} / {len(PLAN)}")
    st.progress(min(1.0, done / len(PLAN)))
    if progress["daily_hours"]:
        st.markdown("**Recent entries**")
        for day in sorted(progress["daily_hours"], reverse=True)[:7]:
            st.write(f"- {day}: {progress['daily_hours'][day]} hours · {progress['scores'].get(day, 'Not tested')}")

with tabs[5]:
    st.subheader("Practice questions")
    subject = st.selectbox("Choose subject", SUBJECTS)
    st.caption("Try answering from memory first; then check your notes.")
    for i, q in enumerate(PRACTICE_QUESTIONS[subject], 1):
        st.markdown(f"**{i}. {q}**")
        st.text_area("Your answer / key points", key=f"answer_{subject}_{i}", height=80)
    st.info("Practice prompts are not guaranteed exam questions. Use your official syllabus and date sheet.")

st.divider()
st.caption("BCA Exam Buddy · Study aid only · Follow your official date sheet and latest syllabus.")
