import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("dataset/day.csv")
hour_df = pd.read_csv("dataset/hour.csv")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
merged_df = pd.merge(day_df, hour_df, on='dteday')
merged_df['month'] = merged_df['dteday'].dt.month

st.set_page_config(
    page_title="Dashboard Analisis Penggunaan Sepeda",
    page_icon="🚲",
    layout="wide"
)

st.sidebar.title("Navigasi Dashboard")
option = st.sidebar.selectbox("Pilih Visualisasi", 
                              ["Pola Bulanan", 
                               "Frekuensi Hari Kerja vs Hari Libur", 
                               "Pengaruh Cuaca", 
                               "Pengaruh Suhu"])

st.markdown("""
    <div style="background-color:#4CAF50;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Dashboard Analisis Penggunaan Sepeda</h1>
    </div>
    <br>
    """, unsafe_allow_html=True)

st.markdown("""
    **Selamat datang!** Dashboard ini berfungsi untuk menganalisis data penggunaan sepeda berdasarkan berbagai faktor seperti cuaca, suhu, dan hari kerja.
    Pilih salah satu analisis dari menu di sidebar untuk melihat detail visualisasi data.
""")

if option == "Pola Bulanan":
    st.subheader("Pola Perubahan Jumlah Pengguna Sepeda per Bulan")
    
    monthly_total = merged_df.groupby('month')['cnt_x'].sum()
    
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_total.index, monthly_total.values, marker='o', linestyle='-', color='#FF6347')
    plt.title('Tren Penggunaan Sepeda per Bulan', fontsize=16)
    plt.xlabel('Bulan', fontsize=12)
    plt.ylabel('Total Penggunaan Sepeda', fontsize=12)
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
    plt.grid(True)
    st.pyplot(plt)

elif option == "Frekuensi Hari Kerja vs Hari Libur":
    st.subheader("Perbandingan Penggunaan Sepeda antara Hari Kerja dan Hari Libur")
    
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='workingday_x', y='cnt_x', data=merged_df, palette="Set2")
    plt.title('Perbedaan Penggunaan Sepeda antara Hari Kerja dan Hari Libur', fontsize=16)
    plt.xlabel('Hari Kerja (0: Hari Libur, 1: Hari Kerja)', fontsize=12)
    plt.ylabel('Total Penggunaan Sepeda', fontsize=12)
    plt.grid(True)
    st.pyplot(plt)

elif option == "Pengaruh Cuaca":
    st.subheader("Pengaruh Cuaca terhadap Penggunaan Sepeda")
    
    weather_condition = merged_df.groupby('weathersit_x')['cnt_x'].sum()
    
    plt.figure(figsize=(8, 6))
    weather_condition.plot(kind='bar', color='#87CEEB')
    plt.title('Penggunaan Sepeda berdasarkan Kondisi Cuaca', fontsize=16)
    plt.xlabel('Kondisi Cuaca', fontsize=12)
    plt.ylabel('Total Penggunaan Sepeda', fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    
    for i, val in enumerate(weather_condition.values):
        plt.text(i, val + 20, str(val), ha='center', va='bottom')
    
    st.pyplot(plt)

elif option == "Pengaruh Suhu":
    st.subheader("Pengaruh Suhu terhadap Penggunaan Sepeda")
    
    suhu_penggunaan = merged_df.groupby('temp_x')['cnt_x'].sum()
    
    plt.figure(figsize=(8, 6))
    suhu_penggunaan.plot(kind='line', color='#32CD32')
    plt.title('Pengaruh Suhu terhadap Penggunaan Sepeda', fontsize=16)
    plt.xlabel('Suhu (Normalized)', fontsize=12)
    plt.ylabel('Total Penggunaan Sepeda', fontsize=12)
    plt.grid(True)
    st.pyplot(plt)

st.markdown("""
    <br>
    <div style="text-align:center; color:gray;">
    Dibuat oleh Muhammad Habibi Ramadhan | Data Analysis Project
    </div>
""", unsafe_allow_html=True)
