import numpy as np
import streamlit as st
import plotly.graph_objects as go


def apply_theme():
    st.markdown(
        """
        <style>
        /* Hide Streamlit chrome */
        header[data-testid="stHeader"] { visibility: hidden; height: 0px; }
        div[data-testid="stToolbar"] { visibility: hidden; height: 0px; }
        section[data-testid="stSidebar"] { display: none; }

        /* Background */
        html, body, [data-testid="stAppViewContainer"]{
          background: radial-gradient(circle at 20% 10%,
                      #ffffff 0%,
                      #ffeaf3 32%,
                      #ffd2e6 68%,
                      #fff7fb 100%) !important;
        }
        [data-testid="stAppViewContainer"] > .main { background: transparent !important; }

        /* Layout */
        .block-container{
          max-width: 920px !important;
          padding-top: 0.7rem !important;
          padding-bottom: 0.9rem !important;
        }

        /* Remove weird extra blank "blocks" / separators */
        hr { display: none !important; }
        [data-testid="stVerticalBlockBorderWrapper"] { background: transparent !important; border: none !important; }
        [data-testid="stVerticalBlock"] { gap: 0.25rem !important; }
        .stMarkdown { margin-bottom: 0.2rem !important; }

        /* Typography */
        .center { text-align: center; }
        .title{
          font-size: 2.15rem;
          font-weight: 950;
          color: #7a1445;
          letter-spacing: -0.5px;
          margin: 0.35rem 0 0.25rem 0;
        }
        .sub{
          font-size: 1.05rem;
          font-weight: 650;
          color: rgba(92, 18, 52, 0.82);
          margin: 0.15rem 0 0.15rem 0;
        }
        .line{
          font-size: 1.06rem;
          font-weight: 850;
          color: #a01252;
          margin: 0.35rem 0 0.35rem 0;
        }

        /* Force KaTeX color darker */
        .katex, .katex * {
          color: rgba(100, 12, 46, 0.92) !important;
        }

        /* Rose appear animation (opacity only, WebGL-safe) */
        .reveal{
          opacity: 0;
          animation: fadeIn 850ms ease-out both;
        }
        @keyframes fadeIn{
          from { opacity: 0; }
          to   { opacity: 1; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


apply_theme()

# -------------------------------
# Rose math
# -------------------------------
def make_rose(n=130):
    A = 1.995653
    B = 1.27689
    C = 8

    r = np.linspace(0, 1, n)
    theta = np.linspace(-2, 20 * np.pi, n)
    R, THETA = np.meshgrid(r, theta, indexing="ij")

    petalNum = 3.6
    x = 1 - 0.5 * (((5/4) * (1 - (np.mod(petalNum*THETA, 2*np.pi) / np.pi))**2 - 1/4)**2)
    phi = (np.pi/2) * np.exp(-THETA/(C*np.pi))
    y = A*(R**2) * (B*R - 1)**2 * np.sin(phi)

    R2 = x * (R*np.sin(phi) + y*np.cos(phi))
    X = R2 * np.sin(THETA)
    Y = R2 * np.cos(THETA)
    Z = x * (R*np.cos(phi) - y*np.sin(phi))

    CData = 0.70*x + 0.30*(1 - R)
    return X, Y, Z, CData


def rose_figure(n=130):
    X, Y, Z, CData = make_rose(n=n)

    colorscale = [
        [0.0,  "rgb(255,220,238)"],
        [0.55, "rgb(255,170,214)"],
        [1.0,  "rgb(255,150,115)"],
    ]

    fig = go.Figure(
        data=[go.Surface(
            x=X, y=Y, z=Z,
            surfacecolor=CData,
            colorscale=colorscale,
            showscale=False,
            lighting=dict(ambient=0.95, diffuse=0.10, specular=0.08, roughness=0.9),
        )]
    )

    fig.update_layout(
        height=520,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0),
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor="rgba(0,0,0,0)",
            camera=dict(eye=dict(x=1.25, y=1.10, z=0.75)),
            aspectmode="data",
        ),
    )
    return fig


# -------------------------------
# UI
# -------------------------------
choice = st.session_state.get("choice", "YES")

st.markdown("<div class='center'>", unsafe_allow_html=True)
st.markdown("<div class='title'>This is your rose my fella 🌹</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sub'>You chose: <b>{choice}</b> 💞</div>", unsafe_allow_html=True)
st.markdown("<div class='line'>And... it is not linear algebra 😌</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.latex(r"""
\begin{aligned}
R(r,\theta) &= x(r,\theta)\,\big(r\sin\phi + y(r,\theta)\cos\phi\big) \\
X(r,\theta) &= R(r,\theta)\sin\theta \\
Y(r,\theta) &= R(r,\theta)\cos\theta \\
Z(r,\theta) &= x(r,\theta)\,\big(r\cos\phi - y(r,\theta)\sin\phi\big)
\end{aligned}
""")

st.markdown("<div class='reveal'>", unsafe_allow_html=True)
st.plotly_chart(rose_figure(130), use_container_width=True, config={"displayModeBar": False})
st.markdown("</div>", unsafe_allow_html=True)

