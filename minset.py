import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="🌱 Growth Mindset Challenge", layout='wide')
st.markdown("""
    <style>
        body { background-color: #f4f4f4; }
        .main { background-color: white; padding: 20px; border-radius: 10px; }
        .sidebar .stTextInput, .sidebar .stTextArea, .sidebar .stSelectbox, .sidebar .stRadio {
            background-color: #e3f2fd;
            border-radius: 5px;
            padding: 8px;
        }
        .stButton>button { 
            background-color: #0078ff; 
            color: white; 
            font-weight: bold; 
            border-radius: 8px; 
            padding: 10px;
        }
        .stButton>button:hover { 
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

st.title('🌱 Growth Mindset Challenge')
st.write("Track your progress, embrace challenges, and grow every day! 🚀")

# Sidebar for user details
st.sidebar.header("👤 Your Profile")
name = st.sidebar.text_input("Enter your name:")
current_date = datetime.now().strftime('%Y-%m-%d')

# Motivational Quote Section
quotes = [
    "“Success is not an accident, success is a choice.” – Stephen Curry",
    "“Failure is success in progress.” – Albert Einstein",
    "“The only way to do great work is to love what you do.” – Steve Jobs",
    "“Don’t let what you cannot do interfere with what you can do.” – John Wooden",
    "“Challenges make life interesting; overcoming them makes it meaningful.”",
    "“Believe you can and you’re halfway there.” – Theodore Roosevelt",
    "“Hardships often prepare ordinary people for extraordinary destinies.” – C.S. Lewis",
]
st.sidebar.success(f"💡 *{random.choice(quotes)}*")

# Challenge of the Day
st.subheader("🚀 Challenge of the Day")
challenge_list = [
    "Learn something completely new today!",
    "Embrace failure and reflect on your lessons.",
    "Step outside your comfort zone and tackle a tough task.",
    "Ask for constructive feedback and apply it.",
    "Teach someone a concept you're mastering.",
    "Turn a negative thought into a positive one!",
    "Write three things you're grateful for today.",
    "Spend 15 minutes meditating or reflecting on your goals.",
    "Challenge yourself to avoid distractions and focus deeply.",
]
selected_challenge = st.selectbox("Choose a challenge to focus on today:", challenge_list)

# Progress Tracker
st.subheader("📊 Track Your Progress")
progress_options = ["Not Started", "In Progress", "Completed"]
progress = st.radio("How far along are you?", progress_options, index=0)

# Reflection Section
st.subheader("✍️ Reflection Journal")
reflection = st.text_area("Write about your experience today:")

# Initialize session state for progress tracking
if "progress_data" not in st.session_state:
    st.session_state.progress_data = {"Not Started": 0, "In Progress": 0, "Completed": 0}

# Save Progress
if st.button("💾 Save Progress"):
    st.session_state.progress_data[progress] += 1  # Update progress counts
    
    data = pd.DataFrame({
        "Name": [name if name else "Anonymous"],
        "Date": [current_date],
        "Challenge": [selected_challenge],
        "Progress": [progress],
        "Reflection": [reflection if reflection else "No reflection provided."]
    })
    
    st.success("✅ Progress saved! Keep growing! 🌟")
    st.dataframe(data)
    
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Your Progress",
        data=csv,
        file_name=f"growth_mindset_{name}_{current_date}.csv",
        mime="text/csv",
    )

# Clear Progress Button
if st.button("🗑 Clear Progress"):
    st.session_state.progress_data = {"Not Started": 0, "In Progress": 0, "Completed": 0}
    st.warning("Progress cleared! Fresh start! 💪")

# Progress Visualization (Dynamic)
st.subheader("📈 Growth Mindset Progress Chart")
progress_chart_data = pd.DataFrame(
    {"Stage": list(st.session_state.progress_data.keys()), 
     "Count": list(st.session_state.progress_data.values())}
)
st.bar_chart(progress_chart_data)

# Dark Mode Toggle
dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
        body { background-color: #1E1E1E; color: white; }
        .main { background-color: #333; }
        .stTextInput, .stTextArea, .stSelectbox, .stRadio { background-color: #444; color: white; }
        .stButton>button { background-color: #444; color: white; }
        .stButton>button:hover { background-color: #555; }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.sidebar.info("💡 Growth happens outside your comfort zone! Keep pushing forward! 🚀")
