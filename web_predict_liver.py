from unicodedata import name
import streamlit as st
import joblib
import numpy as np

# 1. Load model yang sudah kita simpan di Langkah 2
try:
    model = joblib.load('model_liver_gk.pkl')
except:
    st.error("File 'model_liver_gk.pkl' tidak ditemukan! Jalankan Langkah 2 terlebih dahulu.")

# 2. Tampilan Web App
st.markdown("## <center> 🏥 Website Prediksi Penderita Liver 🏥 </center>", unsafe_allow_html=True)
st.write("Masukkan data pasien untuk melakukan pengecekan risiko liver.")

# 3. Form Input Data Medis Pasien
st.write("### Data Klinis")
nama = st.text_input("Nama Pasien", value="...")
age = st.number_input("Usia Pasien (Tahun)", min_value=0, max_value=100, value=0)
gender = st.selectbox("Jenis Kelamin", options=[("laki-laki"), ("Perempuan")])
if gender == "laki-laki":
    gender = 0
else:
    gender = 1
tinggi_badan = st.number_input("Tinggi Badan (cm)", value=0.0)
total_bilirubin = st.number_input("Total Bilirubin (mg/dL)", value=0.0)
direct_bilirubin = st.number_input("Direct Bilirubin (mg/dL)", value=0.0)
alkphos = st.number_input("Alkaline Phosphotase (U/L)", value=0.0)
sgpt = st.number_input("SGPT / Alamine Aminotransferase (U/L)", value=0.0)
sgot = st.number_input("SGOT / Aspartate Aminotransferase (U/L)", value=0.0)
proteins = st.number_input("Total Proteins (g/dL)", value=0.0)
albumin = st.number_input("Albumin (g/dL)", value=0.0)
ag_ratio = st.number_input("Albumin and Globulin Ratio", value=0.0)

# 4. Logika Tombol Prediksi
if st.button("Mulai Diagnosa"):
    # Susun data input menjadi format yang dipahami AI
    data_pasien = np.array([[age, gender, total_bilirubin, direct_bilirubin, alkphos, sgpt, sgot, proteins, albumin, ag_ratio]])
    
    # Lakukan Prediksi
    hasil_prediksi = model.predict(data_pasien)
    
    st.subheader("Hasil Analisis:")
    if hasil_prediksi[0] == 1:
        st.error("⚠️ Hasil: Pasien Terprediksi SAKIT LIVER. Disarankan pemeriksaan klinis lebih lanjut.")
    else:
        st.success("✅ Hasil: Pasien Terprediksi SEHAT / NON-LIVER.")
    
st.write("---")
st.caption("📢 **Catatan/Disclaimer:** Aplikasi ini menggunakan kecerdasan buatan dengan akurasi model sebesar % untuk keperluan skrining awal akademis. Hasil prediksi sistem bukan merupakan diagnosis final medis resmi. Harap selalu konsultasikan hasil laboratorium Anda kepada dokter atau tenaga medis ahli.")