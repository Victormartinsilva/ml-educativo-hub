"""
ML Educativo — Hub
==================
Landing page unificando os 6 projetos da serie ML Educativo.
Cada projeto demonstra um conceito de Machine Learning do zero em Python/NumPy.
"""

import streamlit as st

st.set_page_config(
    page_title="ML Educativo — Serie Completa",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500;600&display=swap');

:root {
    --bg:      #08090c;
    --s1:      #0e1117;
    --s2:      #141922;
    --s3:      #1a2130;
    --b1:      #1e2a3a;
    --b2:      #263348;
    --text:    #e2eaf4;
    --text2:   #7a92aa;
    --muted:   #3a4f66;

    --c1: #00e5ff;  /* Q-Learning      — cyan    */
    --c2: #69ff87;  /* Arvore          — verde   */
    --c3: #ffd600;  /* Apriori         — amarelo */
    --c4: #a78bfa;  /* Neural MLP      — roxo    */
    --c5: #f59e0b;  /* Transformers    — âmbar   */
    --c6: #00e5ff;  /* DQN             — cyan    */
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background: var(--bg);
    color: var(--text);
}
.mono { font-family: 'JetBrains Mono', monospace; }

/* ── HERO ── */
.hero {
    text-align: center;
    padding: 3.5rem 1rem 2rem;
    position: relative;
}
.hero-title {
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    font-weight: 800;
    letter-spacing: -.02em;
    line-height: 1.1;
    background: linear-gradient(135deg, #00e5ff 0%, #a78bfa 50%, #69ff87 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: .78rem;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: .7rem;
}
.hero-desc {
    max-width: 600px;
    margin: 1.2rem auto 0;
    font-size: 1rem;
    color: var(--text2);
    line-height: 1.7;
}

/* ── BADGES ── */
.badge-row {
    display: flex;
    gap: .6rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 1.4rem;
}
.badge {
    display: inline-flex;
    align-items: center;
    gap: .35rem;
    padding: .25rem .8rem;
    border-radius: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: .68rem;
    font-weight: 500;
    letter-spacing: .06em;
    border: 1px solid;
}
.badge-cyan   { background: rgba(0,229,255,.08); color: #00e5ff; border-color: rgba(0,229,255,.25); }
.badge-green  { background: rgba(105,255,135,.08); color: #69ff87; border-color: rgba(105,255,135,.25); }
.badge-purple { background: rgba(167,139,250,.08); color: #a78bfa; border-color: rgba(167,139,250,.25); }
.badge-amber  { background: rgba(245,158,11,.08); color: #f59e0b; border-color: rgba(245,158,11,.25); }

/* ── DIVIDER ── */
.divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--b2), transparent);
    margin: 2rem 0;
}

/* ── SECTION LABEL ── */
.slabel {
    font-family: 'JetBrains Mono', monospace;
    font-size: .62rem;
    letter-spacing: .22em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 1.2rem;
    text-align: center;
}

/* ── PROJECT CARD ── */
.pcard {
    background: var(--s1);
    border: 1px solid var(--b1);
    border-radius: 10px;
    padding: 1.4rem 1.5rem;
    height: 100%;
    position: relative;
    overflow: hidden;
    transition: border-color .2s, transform .2s;
}
.pcard:hover {
    transform: translateY(-2px);
}
.pcard::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
}
.pcard-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: .62rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    margin-bottom: .5rem;
}
.pcard-icon {
    font-size: 1.8rem;
    margin-bottom: .5rem;
    display: block;
}
.pcard-title {
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: -.01em;
    margin-bottom: .3rem;
}
.pcard-concept {
    font-family: 'JetBrains Mono', monospace;
    font-size: .7rem;
    padding: .18rem .55rem;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: .7rem;
    font-weight: 500;
}
.pcard-desc {
    font-size: .88rem;
    color: var(--text2);
    line-height: 1.6;
    margin-bottom: 1rem;
}
.pcard-tags {
    display: flex;
    flex-wrap: wrap;
    gap: .3rem;
    margin-bottom: 1rem;
}
.ptag {
    font-family: 'JetBrains Mono', monospace;
    font-size: .6rem;
    padding: .12rem .45rem;
    border-radius: 3px;
    background: var(--s2);
    color: var(--text2);
    border: 1px solid var(--b2);
}
.pcard-formula {
    background: var(--s2);
    border-radius: 5px;
    padding: .55rem .8rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    line-height: 1.6;
    margin-bottom: 1rem;
    border-left: 2px solid;
}
.pcard-link {
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    text-decoration: none;
    padding: .35rem .85rem;
    border-radius: 5px;
    border: 1px solid;
    transition: all .15s;
    letter-spacing: .06em;
}

/* ── TIMELINE ── */
.timeline {
    position: relative;
    padding: 1rem 0;
}
.tl-line {
    position: absolute;
    left: 50%;
    top: 0; bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, transparent, var(--b2) 10%, var(--b2) 90%, transparent);
    transform: translateX(-50%);
}
.tl-item {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin: .8rem 0;
    position: relative;
}
.tl-item.right { flex-direction: row-reverse; }
.tl-dot {
    width: 12px; height: 12px;
    border-radius: 50%;
    border: 2px solid;
    background: var(--bg);
    flex-shrink: 0;
    position: relative;
    z-index: 1;
}
.tl-content {
    flex: 1;
    background: var(--s1);
    border: 1px solid var(--b1);
    border-radius: 7px;
    padding: .7rem 1rem;
    max-width: 380px;
}
.tl-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: .62rem;
    letter-spacing: .12em;
    text-transform: uppercase;
    margin-bottom: .2rem;
}
.tl-title {
    font-size: .95rem;
    font-weight: 700;
    margin-bottom: .2rem;
}
.tl-sub {
    font-size: .8rem;
    color: var(--text2);
}

/* ── CONCEITOS GRID ── */
.concept-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}
.concept-box {
    background: var(--s1);
    border: 1px solid var(--b1);
    border-radius: 8px;
    padding: 1.1rem 1.2rem;
}
.concept-name {
    font-size: .95rem;
    font-weight: 700;
    margin-bottom: .3rem;
}
.concept-formula {
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    color: var(--text2);
    background: var(--s2);
    border-radius: 4px;
    padding: .4rem .6rem;
    margin: .4rem 0;
}
.concept-one {
    font-size: .82rem;
    color: var(--text2);
    font-style: italic;
    margin-top: .4rem;
}

/* ── STACK SECTION ── */
.stack-row {
    display: flex;
    flex-wrap: wrap;
    gap: .5rem;
    justify-content: center;
    margin-top: .8rem;
}
.stack-chip {
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    padding: .3rem .8rem;
    border-radius: 20px;
    background: var(--s2);
    border: 1px solid var(--b2);
    color: var(--text2);
}

/* ── STAT ROW ── */
.stat-row {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    justify-content: center;
    margin: 1.5rem 0;
}
.stat-box {
    background: var(--s1);
    border: 1px solid var(--b1);
    border-radius: 8px;
    padding: 1rem 1.5rem;
    text-align: center;
    min-width: 120px;
}
.stat-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1;
}
.stat-lbl {
    font-size: .72rem;
    color: var(--text2);
    margin-top: .3rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: .1em;
    text-transform: uppercase;
}

/* ── FOOTER ── */
.footer {
    text-align: center;
    padding: 2.5rem 1rem;
    border-top: 1px solid var(--b1);
    margin-top: 3rem;
}
.footer-name {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: .3rem;
}
.footer-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: .7rem;
    color: var(--muted);
    letter-spacing: .12em;
}

/* Streamlit overrides */
[data-testid="stSidebar"] { display: none; }
.block-container { padding: 0 !important; max-width: 100% !important; }
header { display: none !important; }
hr { border: none; border-top: 1px solid var(--b1); margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# DADOS DOS PROJETOS
# ─────────────────────────────────────────────────────────

PROJECTS = [
    {
        "num": "01",
        "icon": "🎮",
        "title": "Jogo da Velha",
        "concept": "Q-Learning",
        "color": "#00e5ff",
        "desc": "A IA aprende a jogar Jogo da Velha contra si mesma usando Aprendizado por Reforço. A cada partida ela atualiza sua Q-Table e melhora sua estratégia.",
        "tags": ["Q-Table", "Epsilon-greedy", "Bellman", "Recompensas", "Decaimento"],
        "formula": "Q(s,a) ← Q(s,a) + α[r + γ·max Q(s',a') − Q(s,a)]",
        "one_line": "A IA aprende sozinha jogando contra si mesma",
        "stack": ["numpy", "streamlit"],
        "url": "https://jogodavelhallm-jxloahsbg8dedbg7unnbb6.streamlit.app/",
    },
    {
        "num": "02",
        "icon": "🌿",
        "title": "Diagnóstico de Plantas",
        "concept": "Árvore de Decisão",
        "color": "#69ff87",
        "desc": "A IA analisa sintomas de plantas e percorre uma Árvore de Decisão nó a nó, explicando cada decisão tomada — sem caixas-pretas.",
        "tags": ["Gini", "Entropia", "Info Gain", "Overfitting", "max_depth"],
        "formula": "Gini = 1 − Σ pₖ²  |  IG = H_pai − Σ(n_filho/n_pai)·H_filho",
        "one_line": "A IA explica cada decisão, nó por nó",
        "stack": ["scikit-learn", "matplotlib", "streamlit"],
        "url": "https://arvoredecisoes-mz4p6vj4a36becesjibylh.streamlit.app/",
    },
    {
        "num": "03",
        "icon": "🚜",
        "title": "TractorMind",
        "concept": "Regras de Associação",
        "color": "#ffd600",
        "desc": "Sistema de manutenção preditiva para tratores agrícolas. Aprende sequências de falha (DTC) e alerta antes que a falha crítica aconteça.",
        "tags": ["Apriori", "Suporte", "Confiança", "Lift", "DTC / J1939"],
        "formula": "conf(A→B) = P(A∩B)/P(A)  |  lift = conf/P(B)",
        "one_line": "Prevê a próxima falha antes que ela aconteça",
        "stack": ["mlxtend", "pandas", "plotly", "streamlit"],
        "url": "https://tractormind-frzdhzmh89mxygnpfts8mm.streamlit.app/",
    },
    {
        "num": "04",
        "icon": "🧠",
        "title": "NeuralMind",
        "concept": "Rede Neural MLP",
        "color": "#a78bfa",
        "desc": "Rede Neural Multicamada implementada do zero em NumPy. Classifica flores Iris e visualiza forward pass, backpropagation e o loss landscape 3D.",
        "tags": ["Forward Pass", "Backprop", "Gradient Descent", "ReLU", "Softmax", "Loss Landscape"],
        "formula": "z = Wx + b  |  δ = (ŷ − y)  |  W ← W − α·∂L/∂W",
        "one_line": "Rede neural do zero — veja os gradientes descendo",
        "stack": ["numpy", "plotly", "scikit-learn", "streamlit"],
        "url": "https://redeneural-qkgchsrmgfoaajcapncbin.streamlit.app/",
    },
    {
        "num": "05",
        "icon": "🔍",
        "title": "AttentionMind",
        "concept": "Transformers",
        "color": "#f59e0b",
        "desc": "Transformer implementado do zero para classificar sentimento de textos agrícolas. Visualiza heatmaps de atenção token×token e embeddings em 2D.",
        "tags": ["Self-Attention", "Q K V", "Multi-Head", "Pos. Encoding", "Embeddings"],
        "formula": "Attention(Q,K,V) = softmax(QKᵀ / √d) · V",
        "one_line": "Veja exatamente para onde cada palavra 'olha'",
        "stack": ["numpy", "plotly", "scikit-learn", "streamlit"],
        "url": "https://attentionmind-emhmu7x2xkrrnplfixapx6.streamlit.app/",
    },
    {
        "num": "06",
        "icon": "🧩",
        "title": "MazeMind",
        "concept": "DQN",
        "color": "#00e5ff",
        "desc": "Deep Q-Network resolve um labirinto 10×10. Fecha o ciclo com o projeto 1: a Q-Table vira uma rede neural com Replay Buffer e Target Network.",
        "tags": ["DQN", "Replay Buffer", "Target Network", "Bellman + Rede", "Generalização"],
        "formula": "y = r + γ·max Q_target(s')  |  L = (Q_online(s,a) − y)²",
        "one_line": "Q-Learning + Rede Neural = DQN",
        "stack": ["numpy", "plotly", "streamlit"],
        "url": "https://trafficdqn-jzgcy2xdfu5fc2rfexhsaj.streamlit.app/",
    },
]

GITHUB_USER = "victor-data-ml"   # <-- altere para seu usuario real

# ─────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-title">ML Educativo</div>
    <div class="hero-sub">Serie de 6 projetos — Machine Learning do Zero</div>
    <div class="hero-desc">
        Cada projeto implementa um conceito clássico de ML em <strong>NumPy puro</strong>,
        com visualizações interativas que mostram o que a IA está aprendendo —
        sem caixas-pretas, sem frameworks ocultos.
    </div>
    <div class="badge-row">
        <span class="badge badge-cyan">🐍 Python</span>
        <span class="badge badge-green">📊 NumPy puro</span>
        <span class="badge badge-purple">⚡ Streamlit</span>
        <span class="badge badge-amber">6 projetos</span>
        <span class="badge badge-cyan">Do zero</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# STATS
# ─────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-row">
    <div class="stat-box">
        <div class="stat-num" style="color:#00e5ff">6</div>
        <div class="stat-lbl">Projetos</div>
    </div>
    <div class="stat-box">
        <div class="stat-num" style="color:#69ff87">6</div>
        <div class="stat-lbl">Conceitos</div>
    </div>
    <div class="stat-box">
        <div class="stat-num" style="color:#a78bfa">~5k</div>
        <div class="stat-lbl">Linhas de código</div>
    </div>
    <div class="stat-box">
        <div class="stat-num" style="color:#f59e0b">0</div>
        <div class="stat-lbl">Frameworks de ML</div>
    </div>
    <div class="stat-box">
        <div class="stat-num" style="color:#00e5ff">∞</div>
        <div class="stat-lbl">Curiosidade</div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# CARDS DOS PROJETOS
# ─────────────────────────────────────────────────────────
st.markdown('<div class="slabel">Os 6 projetos</div>', unsafe_allow_html=True)

for row_start in range(0, len(PROJECTS), 3):
    row_projects = PROJECTS[row_start:row_start+3]
    cols = st.columns(len(row_projects), gap="medium")
    for col, p in zip(cols, row_projects):
        with col:
            c = p["color"]
            concept_bg = f"rgba({int(c[1:3],16)},{int(c[3:5],16)},{int(c[5:7],16)},.1)"
            tags_html  = "".join(f'<span class="ptag">{t}</span>' for t in p["tags"])
            repo_url   = p["url"]

            st.markdown(f"""
            <div class="pcard" style="border-color:{c}22">

                <div style="position:absolute;top:0;left:0;right:0;height:3px;
                            background:linear-gradient(90deg,{c},{c}44)"></div>

                <div class="pcard-num mono" style="color:{c}88">PROJETO {p['num']}</div>
                <div class="pcard-icon">{p['icon']}</div>
                <div class="pcard-title">{p['title']}</div>
                <div class="pcard-concept" style="background:{concept_bg};color:{c};
                     border:1px solid {c}44">{p['concept']}</div>

                <div class="pcard-desc">{p['desc']}</div>
                <div class="pcard-tags">{tags_html}</div>

                <div class="pcard-formula" style="border-color:{c};color:{c}bb">
                    {p['formula']}
                </div>

                <div style="font-size:.78rem;color:{c};font-style:italic;margin-bottom:1rem">
                    "{p['one_line']}"
                </div>

                <a href="{repo_url}" target="_blank"
                   class="pcard-link"
                   style="color:{c};border-color:{c}44;background:{concept_bg}">
                    ↗ Ver projeto
                </a>
            </div>
            """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# LINHA DO TEMPO DE COMPLEXIDADE
# ─────────────────────────────────────────────────────────
st.markdown('<div class="slabel">Progressão de complexidade</div>', unsafe_allow_html=True)

timeline_items = [
    ("01", "🎮", "Jogo da Velha",          "Q-Learning",           "#00e5ff", "Tabela de valores — fundação do RL",        "Básico"),
    ("02", "🌿", "Diagnóstico de Plantas",  "Árvore de Decisão",    "#69ff87", "Aprendizado supervisionado interpretável",  "Básico"),
    ("03", "🚜", "TractorMind",             "Apriori",              "#ffd600", "Mineração de padrões em transações",        "Intermediário"),
    ("04", "🧠", "NeuralMind",              "Rede Neural MLP",      "#a78bfa", "Backpropagation e gradiente descendente",   "Avançado"),
    ("05", "🔍", "AttentionMind",           "Transformers",         "#f59e0b", "Mecanismo de atenção — base do GPT",        "Avançado"),
    ("06", "🧩", "MazeMind",               "DQN",                  "#00e5ff", "RL + Rede Neural — fecha o ciclo",          "Avançado"),
]

tl_html = '<div style="position:relative;padding:1rem 2rem">'
tl_html += '<div style="position:absolute;left:50%;top:0;bottom:0;width:2px;background:linear-gradient(180deg,transparent,#263348 10%,#263348 90%,transparent);transform:translateX(-50%)"></div>'

for i, (num, icon, title, concept, color, desc, level) in enumerate(timeline_items):
    side  = "left" if i % 2 == 0 else "right"
    align = "flex-end" if side == "left" else "flex-start"
    pad_l = "0 3rem 0 0" if side == "left" else "0 0 0 3rem"
    concept_bg = f"rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},.08)"

    tl_html += (
f'<div style="display:flex;justify-content:{align};margin:.7rem 0;position:relative">'
f'<div style="position:absolute;left:50%;top:50%;width:14px;height:14px;'
f'border-radius:50%;border:2px solid {color};background:{color}22;'
f'transform:translate(-50%,-50%);z-index:1"></div>'
f'<div style="max-width:44%;padding:{pad_l}">'
f'<div style="background:#0e1117;border:1px solid {color}33;border-radius:8px;'
f'padding:.9rem 1.1rem;border-left:3px solid {color}">'
f'<div style="display:flex;align-items:center;gap:.5rem;margin-bottom:.3rem">'
f'<span style="font-size:1.1rem">{icon}</span>'
f'<span style="font-family:JetBrains Mono,monospace;font-size:.6rem;'
f'color:{color}88;letter-spacing:.14em">PROJETO {num}</span>'
f'<span style="font-family:JetBrains Mono,monospace;font-size:.58rem;'
f'padding:.1rem .4rem;border-radius:3px;'
f'background:rgba(255,255,255,.04);color:#3a4f66">{level}</span>'
f'</div>'
f'<div style="font-size:.95rem;font-weight:700;margin-bottom:.2rem">{title}</div>'
f'<div style="font-family:JetBrains Mono,monospace;font-size:.68rem;'
f'color:{color};padding:.15rem .5rem;border-radius:3px;'
f'background:{concept_bg};display:inline-block;margin-bottom:.4rem">{concept}</div>'
f'<div style="font-size:.82rem;color:#7a92aa">{desc}</div>'
f'</div></div></div>'
    )

tl_html += '</div>'
st.markdown(tl_html, unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# FÓRMULAS ESSENCIAIS
# ─────────────────────────────────────────────────────────
st.markdown('<div class="slabel">Fórmulas que a série ensina</div>', unsafe_allow_html=True)

formulas = [
    ("#00e5ff", "Bellman (Q-Learning + DQN)",
     "Q(s,a) ← Q(s,a) + α[r + γ·max Q(s',a') − Q(s,a)]",
     "Base do Aprendizado por Reforço — do Jogo da Velha ao DQN"),

    ("#69ff87", "Impureza de Gini",
     "Gini = 1 − Σₖ pₖ²",
     "Como a Árvore de Decisão escolhe o melhor split"),

    ("#ffd600", "Confiança e Lift (Apriori)",
     "conf(A→B) = P(A∩B)/P(A)   lift = conf/P(B)",
     "Força e relevância de uma regra de associação"),

    ("#a78bfa", "Backpropagation",
     "∂L/∂W = aᵀ·δ/n   δ = (ŷ−y)·f'(z)",
     "Como o gradiente flui de trás para frente na rede"),

    ("#f59e0b", "Scaled Dot-Product Attention",
     "Attention(Q,K,V) = softmax(QKᵀ/√d)·V",
     "Cada token decide quanto 'atentar' para os outros"),

    ("#00e5ff", "Target DQN",
     "y = r + γ·max_a Q_target(s',a')   L = (Q_online(s,a) − y)²",
     "Bellman com rede neural e target network estável"),
]

cols_f = st.columns(2, gap="medium")
for i, (color, name, formula, meaning) in enumerate(formulas):
    with cols_f[i % 2]:
        concept_bg = f"rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},.06)"
        st.markdown(f"""
        <div style="background:#0e1117;border:1px solid {color}22;border-radius:8px;
                    padding:1rem 1.2rem;margin-bottom:.8rem;
                    border-left:3px solid {color}">
            <div style="font-size:.88rem;font-weight:700;color:{color};margin-bottom:.5rem">{name}</div>
            <div style="font-family:JetBrains Mono,monospace;font-size:.78rem;
                        background:{concept_bg};border-radius:4px;padding:.5rem .7rem;
                        color:{color}cc;margin-bottom:.5rem">{formula}</div>
            <div style="font-size:.8rem;color:#7a92aa">{meaning}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# STACK TECNOLÓGICA
# ─────────────────────────────────────────────────────────
st.markdown('<div class="slabel">Stack tecnológica</div>', unsafe_allow_html=True)
st.markdown("""
<div style="display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:center;margin:1rem 0 2rem">
""", unsafe_allow_html=True)

stack_sections = [
    ("Core ML", "#a78bfa", ["NumPy", "Backpropagation manual", "Sem PyTorch/TF"]),
    ("Dados", "#69ff87",  ["pandas", "scikit-learn (datasets)", "mlxtend (Apriori)"]),
    ("Visual", "#00e5ff", ["Plotly (3D interativo)", "Matplotlib", "SVG animado"]),
    ("Deploy", "#f59e0b", ["Streamlit", "Streamlit Cloud", "GitHub Actions"]),
]

cols_s = st.columns(len(stack_sections), gap="medium")
for col, (title, color, items) in zip(cols_s, stack_sections):
    with col:
        items_html = "".join(
            f'<div style="font-family:JetBrains Mono,monospace;font-size:.72rem;'
            f'padding:.25rem .5rem;background:#141922;border-radius:3px;'
            f'border:1px solid #1e2a3a;color:#7a92aa;margin:.2rem 0">{it}</div>'
            for it in items
        )
        st.markdown(f"""
        <div style="background:#0e1117;border:1px solid {color}22;border-radius:8px;
                    padding:1rem 1.1rem;border-top:2px solid {color}">
            <div style="font-size:.85rem;font-weight:700;color:{color};
                        margin-bottom:.7rem;font-family:JetBrains Mono,monospace;
                        letter-spacing:.08em">{title}</div>
            {items_html}
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# COMO RODAR LOCALMENTE
# ─────────────────────────────────────────────────────────
st.markdown('<div class="slabel">Como rodar localmente</div>', unsafe_allow_html=True)

st.code(f"""# Clone o repositório de qualquer projeto
git clone https://github.com/{GITHUB_USER}/neuralmind
cd neuralmind

# Instale as dependências
pip install -r requirements.txt

# Rode o app
streamlit run app.py
""", language="bash")

st.markdown("""
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:.8rem;margin-top:1rem">
""", unsafe_allow_html=True)

deploy_info = [
    ("🐍", "Python 3.10+", "Versão mínima recomendada"),
    ("📦", "pip install", "Sem conda necessário"),
    ("🚀", "Streamlit Cloud", "Deploy gratuito em 1 clique"),
    ("⚡", "Sem GPU", "Roda em qualquer máquina"),
]
cols_d = st.columns(len(deploy_info), gap="small")
for col, (icon, title, desc) in zip(cols_d, deploy_info):
    with col:
        st.markdown(f"""
        <div style="background:#0e1117;border:1px solid #1e2a3a;border-radius:7px;
                    padding:.8rem 1rem;text-align:center">
            <div style="font-size:1.4rem;margin-bottom:.3rem">{icon}</div>
            <div style="font-size:.85rem;font-weight:700;margin-bottom:.2rem">{title}</div>
            <div style="font-size:.75rem;color:#7a92aa">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# SOBRE O AUTOR
# ─────────────────────────────────────────────────────────
st.markdown('<div class="slabel">Sobre</div>', unsafe_allow_html=True)

st.markdown(f"""
<div style="max-width:680px;margin:0 auto;text-align:center;padding:1rem">
    <div style="font-size:1.2rem;font-weight:800;margin-bottom:.5rem">Victor</div>
    <div style="font-family:JetBrains Mono,monospace;font-size:.7rem;color:#3a4f66;
                letter-spacing:.14em;margin-bottom:.9rem">
        ENGENHEIRO DE DADOS — SÃO PAULO, BR
    </div>
    <div style="font-size:.9rem;color:#7a92aa;line-height:1.7;margin-bottom:1.2rem">
        Série criada para aprender ML de verdade — implementando cada algoritmo do zero,
        sem depender de caixas-pretas. Stack: Python, NumPy, Microsoft Fabric, Streamlit.
    </div>
    <div style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap">
        <a href="https://github.com/{GITHUB_USER}" target="_blank"
           style="font-family:JetBrains Mono,monospace;font-size:.72rem;
                  padding:.35rem .9rem;border-radius:5px;text-decoration:none;
                  background:rgba(0,229,255,.08);color:#00e5ff;
                  border:1px solid rgba(0,229,255,.25)">
            ↗ GitHub
        </a>
        <a href="https://linkedin.com/in/{GITHUB_USER}" target="_blank"
           style="font-family:JetBrains Mono,monospace;font-size:.72rem;
                  padding:.35rem .9rem;border-radius:5px;text-decoration:none;
                  background:rgba(105,255,135,.08);color:#69ff87;
                  border:1px solid rgba(105,255,135,.25)">
            ↗ LinkedIn
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div style="background:linear-gradient(90deg,#00e5ff,#a78bfa,#69ff87);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                font-size:1.05rem;font-weight:800;margin-bottom:.4rem">
        ML Educativo — Série Completa
    </div>
    <div style="font-family:JetBrains Mono,monospace;font-size:.65rem;color:#3a4f66;
                letter-spacing:.14em">
        6 PROJETOS · NUMPY PURO · ZERO FRAMEWORKS DE ML · OPEN SOURCE
    </div>
</div>
""", unsafe_allow_html=True)
