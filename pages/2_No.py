import streamlit as st
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
NO_GIF_PATH = HERE / "cryingcat.gif"   # you can change name later


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



        /* BIG final yes button (only inside .big-yes wrapper) */
       .big-yes div.stButton > button {
            font-size: 2rem !important;
            padding: 2rem 3rem !important;
            background: linear-gradient(135deg, #ff1e6e, #ff5fa2) !important;
            color: white !important;
            border-radius: 999px !important;
            box-shadow: 0 30px 70px rgba(255, 30, 110, 0.45) !important;
            transform: scale(1.18);
            transition: all 0.25s ease-in-out;
        }
        
        .big-yes div.stButton > button:hover {
            transform: scale(1.28);
            box-shadow: 0 40px 90px rgba(255, 30, 110, 0.6) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


apply_theme()

st.markdown("<div class='center'>", unsafe_allow_html=True)
st.markdown("<div class='big-title'>Hmm… you sure 🥺? Pick again!</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>(PLEASE THINK CAREFULLY!)</div>", unsafe_allow_html=True)

# GIF (smaller than full stretch)
col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    if NO_GIF_PATH.exists():
        st.image(NO_GIF_PATH.read_bytes(), width=520)
    else:
        st.info(f"Add your GIF later at: {NO_GIF_PATH.name}")

st.write("")

# Big YES button (no stretch; uses container width)
st.markdown("<div class='big-yes'>", unsafe_allow_html=True)
if st.button("Yes ✅", use_container_width=True):
    st.session_state["choice"] = "yes"
    st.switch_page("pages/3_Reveal.py")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)




