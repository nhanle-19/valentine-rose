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

        /* Full-page background */
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

        /* Make columns content centered */
        div[data-testid="column"] {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Base button style */
        div.stButton > button {
            border-radius: 999px !important;
            font-weight: 900 !important;
            border: 0 !important;
            box-shadow: 0 14px 30px rgba(255, 47, 122, 0.18) !important;
            transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease !important;
            transform-origin: center !important;
            will-change: transform !important;
        }

        /* YES button (bigger) — first button on the page */
        div.stButton:nth-of-type(1) > button {
            font-size: 1.55rem !important;
            padding: 1.25rem 1.2rem !important;
            background: linear-gradient(135deg, #ff1e6e, #ff5fa2) !important;
            color: white !important;
        }
        div.stButton:nth-of-type(1) > button:hover {
            transform: scale(1.10) !important;
            box-shadow: 0 26px 60px rgba(255, 30, 110, 0.45) !important;
            filter: brightness(1.03) !important;
        }

        /* NO button (smaller) — second button on the page */
        div.stButton:nth-of-type(2) > button {
            font-size: 1.05rem !important;
            padding: 0.75rem 1.1rem !important;
            background: rgba(255, 255, 255, 0.70) !important;
            color: #a01952 !important;
            box-shadow: 0 10px 24px rgba(255, 47, 122, 0.12) !important;
        }
        div.stButton:nth-of-type(2) > button:hover {
            transform: scale(1.04) !important;
            box-shadow: 0 16px 36px rgba(255, 47, 122, 0.20) !important;
            filter: brightness(1.02) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


apply_theme()

st.markdown("<div class='center'>", unsafe_allow_html=True)
st.markdown("<div class='big-title'>Will you be my valentine? 💗</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>(Choose wisely 😌)</div>", unsafe_allow_html=True)

# Centered GIF (no stretch)
col_l, col_m, col_r = st.columns([1, 2, 1], gap="large")
with col_m:
    if GIF_PATH.exists():
        st.image(GIF_PATH.read_bytes(), width=520)
    else:
        st.warning(f"Could not find GIF at: {GIF_PATH}")

st.write("")

# Buttons centered in middle area
col_l2, col_m2, col_r2 = st.columns([1, 2, 1], gap="large")
with col_m2:
    c1, c2 = st.columns(2, gap="large")

    with c1:
        if st.button("Yes ✅", use_container_width=True):
            st.session_state["choice"] = "yes"
            st.switch_page("pages/3_Reveal.py")

    with c2:
        if st.button("No ❌", use_container_width=True):
            st.session_state["choice"] = "no"
            st.switch_page("pages/2_No.py")

st.markdown("</div>", unsafe_allow_html=True)





