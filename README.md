# 👔 AI Resume Screener & Optimizer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red)
![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini-green)

Aplikasi pintar berbasis AI untuk membantu HRD menyeleksi CV atau membantu pelamar kerja mengoptimalkan resume mereka agar lolos sistem ATS (Applicant Tracking System).

## 🌟 Fitur Utama

* **📄 Analisa PDF:** Membaca dan mengekstrak teks dari file CV (PDF) secara otomatis.
* **🤖 AI Matching:** Menggunakan **Google Gemini Pro** untuk membandingkan isi CV dengan Job Description.
* **📊 Skor Kecocokan:** Menampilkan persentase kecocokan dalam bentuk visual (Gauge Chart/Spidometer).
* **🔍 Missing Keywords:** Mendeteksi kata kunci penting yang hilang dari CV.
* **💡 Smart Tips:** Memberikan saran perbaikan spesifik untuk meningkatkan peluang diterima kerja.

## 🛠️ Teknologi yang Digunakan

* **Framework:** [Streamlit](https://streamlit.io/)
* **AI Model:** Google Gemini (Generative AI)
* **Data Visualization:** Plotly (untuk grafik spidometer)
* **PDF Processing:** PyPDF

## 🚀 Cara Menjalankan di Laptop (Local)

Ingin mencoba menjalankan aplikasi ini di komputer sendiri? Ikuti langkah berikut:

1.  **Clone Repository ini:**
    ```bash
    git clone [https://github.com/farhanputrabungamayang/ai-hrd-screener.git](https://github.com/farhanputrabungamayang/ai-hrd-screener.git)
    cd ai-hrd-screener
    ```

2.  **Install Library yang Dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup API Key:**
    * Buat folder `.streamlit` di dalam folder project.
    * Buat file `secrets.toml` di dalam folder tersebut.
    * Isi dengan API Key Google Gemini kamu:
        ```toml
        GOOGLE_API_KEY = "MASUKKAN_API_KEY_KAMU_DISINI"
        ```

4.  **Jalankan Aplikasi:**
    ```bash
    streamlit run app.py
    ```

## 📸 Preview Aplikasi

*<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/d6554428-ce67-4527-8ed0-8771b3175483" />
*

## ⚠️ Disclaimer

Aplikasi ini menggunakan API Pihak Ketiga (Google Gemini). Harap bijak dalam mengunggah data pribadi yang sensitif.

---
Dibuat dengan ❤️ oleh [Farhan Putra Bungamayang]
