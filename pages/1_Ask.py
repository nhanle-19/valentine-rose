import streamlit as st
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
GIF_PATH = HERE / "Cutecat.gif"


def apply_theme():
    st.markdown(
        """
        <style>
        /* Hide Streamlit chrome */
        header[data-testid="stHeader"] { visibility: hidden; height: 0px; }
        div[data-testid="stToolbar"] { visibility: hidden; height: 0px; }
        section[data-testid="stSidebar"] { display: none; }

        /* Full-page background (cooler + lighter than rose) */
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

        /* Center helper */
        .center { text-align: center; }

        .big-title {
            font-size: 2.35rem;
            font-weight: 900;
            color: #ff2f7a;
            margin: 0.4rem 0 0.1rem 0;
            letter-spacing: -0.5px;
        }
        .sub {
            font-size: 1.05rem;
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
st.markdown("<div class='big-title'>Will you be my valentine? 💗</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>(Two correct answers 😌)</div>", unsafe_allow_html=True)

# Big animated GIF
if GIF_PATH.exists():
    st.image(GIF_PATH.read_bytes(), width="stretch")

else:
    st.warning(f"Could not find GIF at: {GIF_PATH}")

st.write("")
c1, c2 = st.columns(2, gap="large")

with c1:
    if st.button("yes", width="stretch"):
        st.session_state["choice"] = "yes"
        st.switch_page("pages/2_Reveal.py")

with c2:
    if st.button("YES, but big!", width="stretch"):
        st.session_state["choice"] = "YES"
        st.switch_page("pages/2_Reveal.py")

st.markdown("</div>", unsafe_allow_html=True)
