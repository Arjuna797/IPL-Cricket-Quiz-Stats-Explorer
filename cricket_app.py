import streamlit as st
import pandas as pd
import random

def add_bg_and_styling():
    """
    Injects custom CSS to add an animated gradient background,
    a watermark, and frosted-glass styling for content blocks.
    """
    # 1. Find a reliable, transparent IPL logo URL (white or light-colored)
    # Using a white-text version for dark backgrounds
    LOGO_URL = "https://pluspng.com/img-png/ipl-logo-png-white-ipl-logo-white-png-1024.png"
    
    # 2. Define the CSS as a single string
    # We use f-string to inject the logo_url
    css = f"""
    <style>
        /* 1. Define the animated gradient keyframes */
        @keyframes gradientShift {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        /* 2. Style the main app container (stApp) */
        /* MODIFIED: Apply gradient to the whole body for robustness */
        body {{
            /* Animated Gradient Background */
            background: linear-gradient(-45deg, #0a004a, #002e8a, #d4003c, #fcae00);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            background-attachment: fixed; /* Keep gradient fixed */
        }}
        
        /* MODIFIED: Keep watermark on .stApp but make bg transparent */
        .stApp {{
            /* Watermark Logo */
            background-image: url("{LOGO_URL}");
            background-position: center 80px; /* Position it below the title */
            background-repeat: no-repeat;
            background-attachment: fixed; /* Keeps it in place on scroll */
            background-size: 50%; /* Adjust size as needed */
            background-blend-mode: overlay; /* Blend it nicely with the gradient */
            
            /* ADDED: Make .stApp transparent so body gradient shows through */
            background-color: transparent !important; 
        }}

        /* 3. Style the main content block (frosted glass) */
        /* MODIFIED: Use data-testid for a more robust selector */
        [data-testid="stBlockContainer"] {{ /* Was: .main .block-container */
            background-color: rgba(0, 0, 0, 0.4); /* Semi-transparent black */
            backdrop-filter: blur(10px); /* The frosted glass effect! */
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.1); /* Subtle border */
        }}

        /* 4. Style the sidebar (frosted glass) */
        /* MODIFIED: Replaced brittle class with stable data-testid selector */
        [data-testid="stSidebar"] {{ /* Was: .st-emotion-cache-16txtl3 */
            background-color: rgba(0, 0, 0, 0.6); /* Darker for contrast */
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }}

        /* 5. Improve text readability on the dark bg */
        /* Make all main text white */
        .stApp, .stMarkdown, .stSubheader, .stHeader, .stTitle, .stRadio > label {{
            color: #ffffff !important;
        }}

        /* 6. Style Buttons to match the theme */
        .stButton > button {{
            border: 2px solid #fcae00; /* IPL Gold */
            background-color: transparent;
            color: #ffffff !important;
            border-radius: 8px;
            transition: all 0.3s ease;
        }}
        .stButton > button:hover {{
            background-color: #fcae00;
            color: #0a004a !important; /* Dark blue text on hover */
            border-color: #fcae00;
        }}
        
        /* Style Primary buttons (like "Submit") */
        .stButton > button[kind="primary"] {{
            background-color: #d4003c; /* IPL Red */
            border-color: #d4003c;
        }}
        .stButton > button[kind="primary"]:hover {{
            background-color: #ffffff;
            color: #d4003c !important;
            border-color: #ffffff;
        }}

        /* 7. Hide the "Made with Streamlit" footer for a clean look */
        footer {{
            visibility: hidden;
        }}

    </style>
    """
    
    # 3. Inject the CSS into the Streamlit app
    st.markdown(css, unsafe_allow_html=True)

# --- Page Configuration ---
st.set_page_config(
    page_title="Cricket Quiz & Stats",
    page_icon="🏏",
    layout="wide"
)

# --- APPLY THE STYLING ---
# This is the line I added to activate your CSS
add_bg_and_styling()

# --- Data Loading ---
# We use st.cache_data to load the data only once
@st.cache_data
def load_data():
    try:
        # Load the CSV file from the subfolder (using the correct file name 'matches.csv')
        df = pd.read_csv("IPL Matches 2008-2020.csv/matches.csv")
        # Drop rows with missing values in key columns to avoid errors
        df = df.dropna(subset=['venue', 'player_of_match', 'winner'])
        return df
    except FileNotFoundError:
        st.error(
            "Error: 'IPL Matches 2008-2020.csv/matches.csv' not found. "
            "Please make sure the 'matches.csv' file is inside the 'IPL Matches 2008-2020.csv' folder."
        )
        return None

df = load_data()

# --- Session State Initialization ---
# This is crucial for making the quiz interactive
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    # We use -1 to show the "Start" screen
    st.session_state.current_question = -1
if 'question_data' not in st.session_state:
    st.session_state.question_data = {}
if 'answer_submitted' not in st.session_state:
    st.session_state.answer_submitted = False
if 'user_choice' not in st.session_state:
    st.session_state.user_choice = None
if 'last_answer_correct' not in st.session_state:
    st.session_state.last_answer_correct = None


# --- Helper Function: Generate a New Question ---
def generate_question(data):
    """Generates a random quiz question from the DataFrame."""
    
    # Pick a random match
    sample = data.sample(1).iloc[0]
    
    # Pick a random question type
    question_type = random.choice(['stadium', 'player_of_match', 'winner'])
    
    # Get all unique values for wrong answers
    all_venues = data['venue'].unique()
    all_players = data['player_of_match'].unique()
    all_teams = data['winner'].unique()
    
    if question_type == 'stadium':
        question = f"In which stadium was the match between {sample['team1']} and {sample['team2']} on {sample['date']} played?"
        correct_answer = sample['venue']
        # Get 3 other random venues
        options = [correct_answer] + random.sample([v for v in all_venues if v != correct_answer], 3)
        hint = f"Hint: The 'Player of the Match' was {sample['player_of_match']}."
        
    elif question_type == 'player_of_match':
        question = f"Who was 'Player of the Match' in the {sample['team1']} vs {sample['team2']} game at {sample['venue']}?"
        correct_answer = sample['player_of_match']
        # Get 3 other random players
        options = [correct_answer] + random.sample([p for p in all_players if p != correct_answer], 3)
        hint = f"Hint: The match was won by {sample['winner']}."
        
    else: # winner
        question = f"Which team won the match between {sample['team1']} and {sample['team2']} at {sample['venue']} on {sample.date}?"
        correct_answer = sample['winner']
        # Get 3 other random teams
        options = [correct_answer] + random.sample([t for t in all_teams if t != correct_answer], 3)
        hint = f"Hint: {sample['toss_winner']} won the toss and chose to {sample['toss_decision']}."

    # Shuffle the options so the correct answer isn't always first
    random.shuffle(options)
    
    return {
        "question": question,
        "options": options,
        "answer": correct_answer,
        "hint": hint
    }

def reset_quiz():
    """Resets all session state variables for the quiz."""
    st.session_state.score = 0
    st.session_state.current_question = -1
    st.session_state.answer_submitted = False
    st.session_state.user_choice = None
    st.session_state.last_answer_correct = None
    st.session_state.question_data = {}


# --- App Navigation (Sidebar) ---
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Choose a page", ["Cricket Quiz 🏏", "IPL Stats Explorer 📊"])

if st.sidebar.button("Reset Quiz"):
    reset_quiz()
    st.rerun()

# --- Page 1: Cricket Quiz ---
if app_mode == "Cricket Quiz 🏏" and df is not None:
    st.title("IPL Cricket Quiz 🏏")
    
    # Check if we are on the start screen
    if st.session_state.current_question == -1:
        st.header(f"Welcome to the Cricket Quiz!")
        st.write("Click the button below to start.")
        
        if st.button("Start Quiz!", type="primary"):
            reset_quiz() # Use the reset function
            st.session_state.current_question = 0 # Start at question 0
            st.session_state.question_data = generate_question(df)
            st.rerun()
    
    else:
        # Quiz is active
        st.header(f"Score: {st.session_state.score}")
        st.subheader(f"Question {st.session_state.current_question + 1}")
        
        q_data = st.session_state.question_data
        
        # Display the question
        st.markdown(f"**{q_data['question']}**")
        
        # Determine if radio buttons should be disabled
        is_disabled = st.session_state.answer_submitted
        
        # Display the radio button options
        user_choice = st.radio(
            "Select your answer:",
            q_data['options'],
            # Set the index based on the user's stored choice, or default
            index=q_data['options'].index(st.session_state.user_choice) if st.session_state.user_choice else 0,
            key=f"q_{st.session_state.current_question}", # Unique key is important!
            disabled=is_disabled
        )
        
        # --- Columns for Buttons ---
        col1, col2, col3 = st.columns([1,1,3])
        
        if st.session_state.answer_submitted:
            # --- Show results and "Next" button ---
            if st.session_state.last_answer_correct:
                st.success("Correct! 🎉")
            else:
                st.error(f"Wrong! The correct answer was: {q_data['answer']}")
            
            with col1:
                if st.button("Next Question", type="primary"):
                    # Update score only when moving to next question
                    if st.session_state.last_answer_correct:
                        st.session_state.score += 1
                        
                    # Reset for next question
                    st.session_state.current_question += 1
                    st.session_state.question_data = generate_question(df)
                    st.session_state.answer_submitted = False
                    st.session_state.user_choice = None
                    st.session_state.last_answer_correct = None
                    st.rerun()
        
        else:
            # --- Show "Submit" and "Hint" buttons ---
            with col1:
                if st.button("Submit", type="primary"):
                    # Store the user's choice and check correctness
                    st.session_state.answer_submitted = True
                    st.session_state.user_choice = user_choice
                    if user_choice == q_data['answer']:
                        st.session_state.last_answer_correct = True
                    else:
                        st.session_state.last_answer_correct = False
                    st.rerun()

            with col2:
                # Hint Button
                if st.button("Show Hint 💡"):
                    st.info(q_data['hint'])

# --- Page 2: IPL Stats Explorer ---
elif app_mode == "IPL Stats Explorer 📊" and df is not None:
    st.title("IPL Stats Explorer 📊")
    st.write("Explore interesting stats from the IPL dataset (2008-2020).")
    
    # --- Graph 1: Top 10 Stadiums ---
    st.subheader("🏟️ Top 10 Most Used Stadiums")
    stadium_counts = df['venue'].value_counts().head(10)
    st.bar_chart(stadium_counts)
    
    # --- Graph 2: Top 10 Players ---
    st.subheader("🏆 Top 10 'Player of the Match' Winners")
    pom_counts = df['player_of_match'].value_counts().head(10)
    st.bar_chart(pom_counts)
    
    # --- Graph 3: Team Wins ---
    st.subheader("🏅 Total Wins per Team")
    # Fixed typo: value_contacts() -> value_counts()
    winner_counts = df['winner'].value_counts()
    st.bar_chart(winner_counts)
    
    # --- Data Filtering by Stadium ---
    st.subheader("Explore a Stadium")
    all_stadiums = df['venue'].unique()
    selected_stadium = st.selectbox("Select a stadium:", all_stadiums)
    
    if selected_stadium:
        stadium_data = df[df['venue'] == selected_stadium]
        st.write(f"Total matches played at {selected_stadium}: {len(stadium_data)}")
        
        # Show a filtered table
        st.dataframe(stadium_data[['date', 'team1', 'team2', 'winner', 'player_of_match']].tail(10))

elif df is None:
    st.info("Please download the dataset as instructed to use the app.")

