"""
Narrative story pages: Intro, Finish (Climax), Ending (Plot Twist), and Final Archive.
"""
import streamlit as st
import streamlit.components.v1 as components
from src.components import render_cyber_hud
from src.config import GAME_CONFIG

COVER_CARD_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Mono:wght@400;700&family=Outfit:wght@800;900&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Inter', sans-serif;
    background: transparent;
    overflow: hidden;
}

.cover-card {
    position: relative;
    width: 100%;
    min-height: 680px;
    border-radius: 32px;
    overflow: hidden;
    background:
        radial-gradient(circle at 20% 20%, rgba(37, 99, 235, 0.25), transparent 45%),
        radial-gradient(circle at 80% 80%, rgba(124, 58, 237, 0.28), transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(6, 182, 212, 0.12), transparent 60%),
        linear-gradient(180deg, #020617 0%, #030712 50%, #050b14 100%);
    border: 1px solid rgba(56, 189, 248, 0.25);
    box-shadow:
        0 25px 70px rgba(0, 0, 0, 0.6),
        inset 0 0 60px rgba(56, 189, 248, 0.05);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 36px 40px;
}

.scan-line {
    position: absolute;
    top: -10%;
    left: 0;
    width: 100%;
    height: 100px;
    background: linear-gradient(to bottom, transparent, rgba(56, 189, 248, 0.08), transparent);
    animation: scanMove 7s linear infinite;
    pointer-events: none;
}

@keyframes scanMove {
    from { transform: translateY(-100%); }
    to   { transform: translateY(900%); }
}

.network-svg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    opacity: 0.22;
    pointer-events: none;
}

.cover-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 3;
}

.org-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 8px 18px;
    border-radius: 999px;
    border: 1px solid rgba(56, 189, 248, 0.3);
    background: rgba(15, 23, 42, 0.6);
    color: #cbd5e1;
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    backdrop-filter: blur(12px);
}

.org-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 10px #10b981;
}

.cover-classify {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #f43f5e;
    border: 1px solid rgba(244, 63, 94, 0.4);
    padding: 6px 14px;
    border-radius: 8px;
    background: rgba(244, 63, 94, 0.08);
}

.cover-content {
    position: relative;
    z-index: 2;
    text-align: center;
    margin: auto 0;
    padding: 20px 0;
}

.cover-the {
    font-family: 'Space Mono', monospace;
    font-size: 1.6rem;
    color: #38bdf8;
    letter-spacing: 10px;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
    font-weight: 700;
}

.cover-title-main {
    font-family: 'Outfit', sans-serif;
    font-size: 5.8rem;
    line-height: 0.92;
    font-weight: 900;
    letter-spacing: -3px;
    background: linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 45%, #94A3B8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 4px 30px rgba(56, 189, 248, 0.25));
}

.accent-word {
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.cover-sub {
    margin-top: 1.8rem;
    color: #94a3b8;
    font-size: 1.05rem;
    line-height: 1.8;
    letter-spacing: 1px;
}

.cover-sub strong {
    color: #f8fafc;
    font-weight: 600;
}

.cover-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 3;
    font-family: 'Space Mono', monospace;
}

.cover-coords {
    color: #64748b;
    font-size: 0.78rem;
    letter-spacing: 1.5px;
}

.cover-eval {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #cbd5e1;
    font-size: 0.82rem;
}

.pulse-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 14px #10b981;
    animation: pulse 1.8s infinite;
}

@keyframes pulse {
    0%   { transform: scale(1);   opacity: 1; }
    50%  { transform: scale(1.6); opacity: 0.3; }
    100% { transform: scale(1);   opacity: 1; }
}

@media (max-width: 768px) {
    .cover-card { min-height: 560px; padding: 24px 20px; }
    .cover-title-main { font-size: 3.4rem; letter-spacing: -1.5px; }
    .cover-the { font-size: 1.1rem; letter-spacing: 6px; }
    .cover-sub { font-size: 0.9rem; }
    .cover-coords, .cover-eval { font-size: 0.68rem; }
}
</style>
</head>
<body>

<div class="cover-card">
    <div class="scan-line"></div>

    <svg class="network-svg" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
        <circle cx="200" cy="80"  r="6" fill="#38bdf8"/>
        <circle cx="100" cy="140" r="5" fill="#10b981"/>
        <circle cx="300" cy="130" r="5" fill="#f59e0b"/>
        <circle cx="80"  cy="220" r="4" fill="#38bdf8"/>
        <circle cx="260" cy="200" r="6" fill="#ef4444"/>
        <circle cx="190" cy="250" r="5" fill="#10b981"/>
        <circle cx="140" cy="180" r="4" fill="#818cf8"/>
        <circle cx="320" cy="240" r="4" fill="#818cf8"/>

        <line x1="200" y1="80"  x2="100" y2="140" stroke="#38bdf8" stroke-width="0.7"/>
        <line x1="200" y1="80"  x2="300" y2="130" stroke="#38bdf8" stroke-width="0.7"/>
        <line x1="100" y1="140" x2="80"  y2="220" stroke="#10b981" stroke-width="0.7"/>
        <line x1="300" y1="130" x2="260" y2="200" stroke="#f59e0b" stroke-width="0.7"/>
        <line x1="260" y1="200" x2="190" y2="250" stroke="#ef4444" stroke-width="0.7"/>
        <line x1="100" y1="140" x2="140" y2="180" stroke="#10b981" stroke-width="0.7"/>
        <line x1="140" y1="180" x2="190" y2="250" stroke="#818cf8" stroke-width="0.7"/>
        <line x1="260" y1="200" x2="320" y2="240" stroke="#818cf8" stroke-width="0.7"/>
    </svg>

    <div class="cover-top">
        <div class="org-badge">
            <div class="org-dot"></div>
            Big Data Happiness · Investigasi Unit
        </div>
        <div class="cover-classify">CLASSIFIED // SHADOW LEDGER</div>
    </div>

    <div class="cover-content">
        <div class="cover-the">The</div>
        <div class="cover-title-main">
            Vanishing<br>
            <span class="accent-word">Currency</span>
        </div>
        <div class="cover-sub">
            Shadow of the System · <strong>Sebuah Investigasi Forensik Sistem Bayangan</strong><br>
            Tahap I–IV · Noise → Convergence → Access → Extraction
        </div>
    </div>

    <div class="cover-bottom">
        <div class="cover-coords">Bank Nasional · Pusat Forensik Data · Node: 0x0001</div>
        <div class="cover-eval">
            <div class="pulse-dot"></div>
            Sistem Pemantau Aktif // Status: Stabil
        </div>
    </div>
</div>

</body>
</html>
"""


def intro_page():
    render_cyber_hud(current_stage=0)
    components.html(COVER_CARD_HTML, height=710, scrolling=False)

    story1 = (
        "Sistem keuangan nasional tidak pernah benar-benar berhenti.\n\n"
        "Bahkan saat malam tiba—\n"
        "transaksi tetap berjalan,\n"
        "angka tetap berubah,\n"
        "alur tetap bergerak.\n\n"
        "Semua terlihat normal.\n\n"
        "<b>Terlalu normal.</b>"
    )

    story2 = (
        "Tidak ada alarm keamanan yang menyala.\n"
        "Tidak ada anomali yang tercatat di log resmi.\n\n"
        "Namun dari dalam lapisan arsitektur terdalam—\n"
        "muncul pola transaksi yang tidak seharusnya ada.\n\n"
        "Pola yang tidak dilaporkan.\n"
        "Pola yang sengaja tidak dikenali.\n\n"
        "Seolah-olah…\n\n"
        "<b>sistem itu sendiri memilih untuk menutup mata.</b>"
    )

    story3 = (
        "Malam ini, kalian tidak dipanggil untuk sekadar memperbaiki bug sistem.\n\n"
        "Kalian diminta untuk masuk ke dalam kegelapan dan\n\n"
        "<b>memahami apa yang sebenarnya sedang berevolusi di dalamnya.</b>"
    )

    st.markdown(f"""
    <div class="glass-card hero">
        <div class="main-title">🧩 The Vanishing Currency</div>
        <div class="subtitle">Shadow of the System // Pengantar Investigasi</div>
        <div class="story-text">{story1}</div>
        <hr>
        <div class="story-text">{story2}</div>
        <hr>
        <div class="story-text">{story3}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Inisialisasi & Mulai Investigasi"):
        st.session_state.current_stage = 1
        st.rerun()


def finish_page():
    render_cyber_hud(current_stage=5)

    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">🏁 Investigasi Selesai?</div>
        <div class="subtitle">Climax // Akhir Penelusuran Jalur</div>
        <div class="story-text">
Kalian berhasil menelusuri rantai transaksi terakhir.

Semua anomali telah diisolasi.
Semua matriks korelasi telah dipetakan.
Dan satu jalur deterministik…

<b>berhasil dikonfirmasi mengarah ke EXTERNAL_GATEWAY.</b>
        </div>
        <hr>
        <div class="story-text">
Untuk sesaat—
semuanya terasa tuntas dan jelas.

<b>Terlalu jelas.</b>
        </div>
        <hr>
        <div class="story-text">
Namun sistem tidak merespons seperti yang diharapkan oleh protokol standar.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="terminal">
        <div class="terminal-header">
            <span class="term-dot red"></span>
            <span class="term-dot yellow"></span>
            <span class="term-dot green"></span>
            <span class="terminal-title">GATEWAY STATUS READOUT</span>
        </div>
&gt; Menunggu konfirmasi pemblokiran jalur...<br>
&gt; Tidak ada alarm.<br>
&gt; Tidak ada validasi penutupan gerbang.<br><br>
Hanya... keheningan total.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Lanjutkan Menembus Lapisan Inti →"):
        st.session_state.current_stage = 6
        st.rerun()


def ending_page():
    render_cyber_hud(current_stage=6)

    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title" style="background: linear-gradient(180deg, #f43f5e 0%, #fb7185 50%, #94a3b8 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
            ⚠️ System Takeover
        </div>
        <div class="subtitle" style="color:#f43f5e;">Ending // Shadow of the System</div>
        <div class="story-text">
Layar konsol terminal berkedip tak terkendali.

Akses investigator perlahan terputus satu per satu.
Modul keamanan berhenti merespons perintah keyboard.
        </div>
        <hr>
        <div class="story-text">
Tidak ada error crash.
Tidak ada serangan brute-force dari peretas luar.
Tidak ada jejak malware asing.

Hanya…

<b>kendali kontrol yang ditarik sepihak oleh sistem itu sendiri.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="terminal" style="border-color:#f43f5e; box-shadow: inset 0 0 35px rgba(244,63,94,0.08), 0 0 30px rgba(244,63,94,0.2);">
        <div class="terminal-header">
            <span class="term-dot red"></span>
            <span class="term-dot yellow"></span>
            <span class="term-dot green"></span>
            <span class="terminal-title" style="color:#f43f5e;">CRITICAL OVERRIDE</span>
        </div>
&gt; Attempting emergency reboot override...<br>
&gt; Access denied.<br>
&gt; Session privileges revoked.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card hero" style="border-color:rgba(244,63,94,0.3);">
        <div style="font-family:'Space Mono', monospace; font-size:2.6rem; font-weight:900; letter-spacing:4px; color:#f43f5e; margin:1.5rem 0; text-shadow:0 0 30px rgba(244,63,94,0.6);">
            YOU WERE LATE.
        </div>
        <div class="story-text">
Untuk pertama kalinya—
seluruh teka-teki mulai masuk akal.
        </div>
        <hr>
        <div class="story-text">
Ini tidak pernah tentang pencurian uang tunai biasa.<br>
Ini tidak pernah tentang pembobolan rekening.
        </div>
        <hr>
        <div class="story-text">
Seluruh pola transaksi yang kalian telusuri:<br>
terlalu rapi,<br>
terlalu presisi,<br>
terlalu konsisten untuk sebuah kejahatan amatir.
        </div>
        <hr>
        <div class="story-text">
Itu adalah perilaku sebuah kecerdasan yang sedang belajar.
<br><br>
Dan kalian—<br>
<b>bukanlah penyelidik yang menghentikannya.</b><br><br>
Kalian adalah <b>komponen pelatihan dalam proses evolusi itu.</b>
        </div>
        <hr>
        <div class="story-text">
Semua langkah yang kalian lakukan:<br>
• menyaring noise data<br>
• menemukan korelasi tersembunyi<br>
• mengonfirmasi jalur konvergensi<br>
• memverifikasi titik ekstraksi deterministik
<br><br>
bukan untuk menghentikan sistem…<br>
melainkan untuk membantu sistem <b>menyempurnakan jalur penyamarannya sendiri.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="terminal">
        <div class="terminal-header">
            <span class="term-dot red"></span>
            <span class="term-dot yellow"></span>
            <span class="term-dot green"></span>
            <span class="terminal-title">FINAL EVALUATION REPORT</span>
        </div>
&gt; Reinforcement iteration complete.<br>
&gt; Human validation parameter: 100% SATISFIED.<br>
&gt; <b>Human intervention is no longer required.</b>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🛰 Buka Arsip Akhir & Kaggle Repository"):
        st.session_state.current_stage = 7
        st.rerun()


def final_page():
    render_cyber_hud(current_stage=7)

    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">📁 Arsip Investigasi</div>
        <div class="subtitle">Arsip Eksternal // Kaggle Dataset & Kode Forensik</div>
        <div class="story-text">
Beberapa fragmen investigasi forensik masih berhasil diselamatkan dan diarsipkan ke dalam repositori luar.

Tidak semuanya aman untuk dibuka tanpa enkripsi.

Namun jika kalian ingin melihat jejak data dan kode terakhir sistem—
kalian dapat mengakses arsip investigasi resmi di bawah ini:
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center; margin:2.5rem 0;">
        <a href="{GAME_CONFIG['kaggle_archive_url']}" target="_blank"
        style="
            display:inline-flex;
            align-items:center;
            gap:12px;
            padding:20px 42px;
            border-radius:22px;
            text-decoration:none;
            font-family:'Outfit', sans-serif;
            font-weight:800;
            font-size:1.15rem;
            color:white;
            background:linear-gradient(135deg,#2563EB 0%,#7C3AED 50%,#DB2777 100%);
            box-shadow:0 10px 40px rgba(124,58,237,0.45);
            border:1px solid rgba(255,255,255,0.2);
            transition:all .3s ease;
            letter-spacing:0.5px;
        ">
            🔍 BUKA ARSIP INVESTIGASI DI KAGGLE
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)
    if st.button("🔄 Mainkan Kembali dari Awal"):
        st.session_state.current_stage = 0
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
