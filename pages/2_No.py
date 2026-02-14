import streamlit as st
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
NO_GIF_PATH = HERE / "No.gif"   # you can change name later


def apply_theme():
    st.markdown(
        """
        <style>
        /* Hide Streamlit chrome */
        header[data-testid="stHeader"] { visibility: hidden; height: 0px; }
        div[data-testid="stToolbar"] { visibility: hidden; height: 0px; }
        section[data-testid="stSidebar"] { display: none; }

        /* Full-page background (match Ask page) */
        html, body, [data-testid="stAppViewContainer"] {
            background: radial-gradient(circle at 18% 12%, #ffffff 0%,
                                       #ffe3ee 35%,
                                       #ffc8df 65%,
                                       #fff3f8 100%) !important;
        }
        [data-testid="stAppViewContainer"] > .main { background: transparent !important; }

        /* Layout */
        .block-container {
            padding-top: 0.9rem !important;
            padding-bottom: 1.2rem !important;
            max-width: 980px !important;
        }

        .center { text-align: center; }

        .big-title {
            font-size: 2.15rem;
            font-weight: 900;
            color: #ff2f7a;
            margin: 0.4rem 0 0.2rem 0;
            letter-spacing: -0.5px;
        }
        .sub {
            font-size: 1.0rem;
            color: rgba(150, 30, 80, 0.85);
            margin: 0 0 1.0rem 0;
        }

        /* Buttons */
        div.stButton > button {
            border-radius: 999px !important;
            padding: 0.9rem 1.1rem !important;
            font-weight: 850 !important;
            border: 0 !important;
            box-shadow: 0 14px 30px rgba(255, 47, 122, 0.18) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


apply_theme()

st.markdown("<div class='center'>", unsafe_allow_html=True)
st.markdown("<div class='big-title'>Hmm… try again 🥺</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>(There is only one button now.)</div>", unsafe_allow_html=True)

# GIF placeholder for later
if NO_GIF_PATH.exists():
    st.image(NO_GIF_PATH.read_bytes(), width="stretch")
else:
    st.info(f"Add your GIF later at: {NO_GIF_PATH.name}")

st.write("")
if st.button("Yes ✅", width="stretch"):
    st.session_state["choice"] = "yes"
    st.switch_page("pages/2_Reveal.py")

st.markdown("</div>", unsafe_allow_html=True)

