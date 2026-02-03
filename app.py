import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
import plotly.graph_objects as go # <-- Library Grafik
import json
import re

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(page_title="AI HRD Screener", page_icon="👔", layout="wide")
st.title("👔 AI Resume Screener & Optimizer")

# CSS Biar tampilan agak rapi
st.markdown("""
<style>
    .stButton>button {width: 100%; border-radius: 10px; height: 3em;}
    .reportview-container {background: #f0f2f6;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SETUP API KEY
# ==========================================
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-flash-latest')
else:
    st.error("⚠️ API Key belum disetting!")
    st.stop()

# ==========================================
# 3. FUNGSI BANTUAN
# ==========================================
def baca_pdf(uploaded_file):
    text = ""
    try:
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text()
    except: st.error("PDF Rusak")
    return text

def buat_gauge_chart(persen):
    """Bikin Grafik Spidometer"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = persen,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Kecocokan (Match Rate)"},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#2ecc71"}, # Warna Ijo
            'steps' : [
                {'range': [0, 50], 'color': "#e74c3c"}, # Merah
                {'range': [50, 75], 'color': "#f1c40f"}, # Kuning
                {'range': [75, 100], 'color': "#d5f5e3"} # Hijau Muda
            ],
        }
    ))
    return fig

def analisa_cv(cv_text, job_desc):
    # Prompt kita paksa output JSON biar gampang diambil angkanya
    prompt = f"""
    Act as an expert Resume Screener.
    Compare the RESUME with the JOB DESCRIPTION.
    
    RESUME: {cv_text}
    JOB DESCRIPTION: {job_desc}
    
    OUTPUT FORMAT (Must be valid JSON string):
    {{
        "match_percentage": (integer 0-100),
        "missing_keywords": ["keyword1", "keyword2", ...],
        "summary": "Brief analysis of the candidate",
        "improvement_tips": ["tip1", "tip2", ...]
    }}
    Do not output markdown code blocks (```json), just the raw JSON string.
    """
    response = model.generate_content(prompt)
    
    # Bersihkan kalau Gemini ngasih ```json di awal
    clean_text = response.text.replace("```json", "").replace("```", "").strip()
    return clean_text

# ==========================================
# 4. UI UTAMA
# ==========================================
col1, col2 = st.columns([1, 1.5]) # Kolom kanan lebih lebar dikit

with col1:
    st.markdown("### 📂 Data Pelamar")
    file_cv = st.file_uploader("Upload CV (PDF)", type=["pdf"])
    job_desc = st.text_area("📋 Paste Job Description", height=250, placeholder="Contoh: Dicari Python Developer berpengalaman...")
    
    tombol = st.button("🚀 Analisa Kecocokan")

with col2:
    st.markdown("### 📊 Hasil Screening")
    
    if tombol and file_cv and job_desc:
        with st.spinner("🤖 AI sedang membaca CV Masbro..."):
            teks_cv = baca_pdf(file_cv)
            json_str = analisa_cv(teks_cv, job_desc)
            
            try:
                # Ubah teks AI jadi Data JSON (Dictionary)
                data = json.loads(json_str)
                
                # 1. Tampilkan Spidometer
                st.plotly_chart(buat_gauge_chart(data['match_percentage']), use_container_width=True)
                
                # 2. Tampilkan Missing Keywords (Pake Chips/Tombol merah)
                st.subheader("⚠️ Missing Keywords")
                if data['missing_keywords']:
                    cols = st.columns(len(data['missing_keywords']))
                    # Tampilkan max 5 keyword biar gak penuh
                    for i, keyword in enumerate(data['missing_keywords'][:5]):
                        st.error(f"❌ {keyword}")
                else:
                    st.success("✅ Semua keyword terpenuhi!")
                
                # 3. Analisa & Tips
                with st.expander("📝 Analisa Detail", expanded=True):
                    st.write(f"**Ringkasan:** {data['summary']}")
                    st.divider()
                    st.write("**💡 Saran Perbaikan:**")
                    for tip in data['improvement_tips']:
                        st.info(f"• {tip}")
                        
            except Exception as e:
                st.error(f"Gagal memproses data JSON: {e}")
                st.write(json_str) # Tampilkan mentahannya kalau error
    
    elif tombol:
        st.warning("Upload CV & Isi Job Desc dulu ya!")
    else:
        st.info("👈 Masukkan data di sebelah kiri untuk melihat hasil.")