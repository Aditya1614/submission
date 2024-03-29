# -*- coding: utf-8 -*-
"""dashboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tNW_PzmpWOfL0pz66qIz0lyq03lfXeTm
"""

# !pip install streamlit

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day_df = pd.read_csv("dashboard/main_data.csv")

st.title("Bike Sharing Dataset | Dashboard")

st.sidebar.title("Biodata:")
st.sidebar.markdown("**• Nama: Aditya Candra Gumilang**")
st.sidebar.markdown(
    "**• Email: adityairasandi@gmail.com**")
st.sidebar.markdown(
    "**• Id Dicoding: adityacandragumilang**")

cloudly = day_df[day_df['weathersit'] == 'Cloudy']
clear = day_df[day_df['weathersit'] == 'Clear']
rain = day_df[day_df['weathersit'] == 'Rain']

total_cloudly = f"{cloudly['cnt'].sum():,}"
total_clear = f"{clear['cnt'].sum():,}"
total_rain = f"{rain['cnt'].sum():,}"

st.subheader('Penggunaan sepeda berdasarkan cuaca')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Cloudy", value=total_cloudly)

with col2:
    st.metric("Clear", value=total_clear)

with col3:
    st.metric("Rain", value=total_rain)

st.subheader('Pengguna Sepeda berdasarkan Cuaca')

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    x='weathersit',
    y='cnt',
    data=day_df,
    errorbar=None)

plt.title('Pengguna Sepeda berdasarkan Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Pengguna Sepeda')

st.pyplot(fig)

day_df['dteday'] = pd.to_datetime(day_df['dteday'],format='%Y-%m-%d')

df_2012 = day_df[day_df['dteday'].dt.year == 2012]
df_2011 = day_df[day_df['dteday'].dt.year == 2011]

total_cnt_2012 = f"{df_2012['cnt'].sum():,}"
total_cnt_2011 = f"{df_2011['cnt'].sum():,}"

st.subheader('Perbadingan tiap tahun')

col1, col2 = st.columns(2)

with col1:
    st.metric("2011", value=total_cnt_2011)

with col2:
    st.metric("2012", value=total_cnt_2012)

monthly_counts = day_df.groupby(by=["mnth","yr"]).agg({
    "cnt": "sum"
}).reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(
    data=monthly_counts,
    x="mnth",
    y="cnt",
    hue="yr",
    palette="dark",
    marker="o")

plt.title("Jumlah pengguna sepeda berdasarkan Bulan dan tahun")
plt.xlabel(None)
plt.ylabel(None)
plt.legend(title="Tahun")
plt.xticks(range(1, 13))
plt.tight_layout()

st.pyplot(fig)

spring = day_df[day_df['season'] == 'Spring']
summer = day_df[day_df['season'] == 'Summer']
fall = day_df[day_df['season'] == 'Fall']
winter = day_df[day_df['season'] == 'Winter']

total_spring = f"{spring['cnt'].sum():,}"
total_summer = f"{summer['cnt'].sum():,}"
total_fall = f"{fall['cnt'].sum():,}"
total_winter = f"{winter['cnt'].sum():,}"

st.subheader('Penggunaan sepeda berdasarkan cuaca')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Spring", value=total_spring)

with col2:
    st.metric("Summer", value=total_summer)

with col3:
    st.metric("Fall", value=total_fall)

with col4:
    st.metric("Winter", value=total_winter)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=day_df, x="season", y="cnt", hue="season", errorbar=None)
st.pyplot(fig)

st.subheader("RFM Analysis")

tab1, tab2, tab3 = st.tabs(["Recency", "Frequency", "Monetary"])

with tab1:
    st.write("Recency (R): Mengevaluasi seberapa baru pelanggan terakhir kali melakukan aktivitas, seperti peminjaman sepeda. Semakin baru, semakin baik, karena pelanggan yang lebih baru mungkin lebih cenderung melakukan transaksi lagi.")
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.hist(day_df['Recency'], bins=30, edgecolor='k', alpha=0.7)
    plt.title('Recency Distribution')
    plt.xlabel('Recency (Days)')
    plt.ylabel('Frequency')
    st.pyplot(fig)

with tab2:
    st.write("Frequency (F): Mengukur seberapa sering pelanggan melakukan aktivitas tertentu, seperti peminjaman sepeda. Pelanggan yang sering melakukan aktivitas ini cenderung lebih berharga karena mereka dapat berkontribusi lebih banyak pendapatan.")
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.hist(day_df['Frequency'], bins=30, edgecolor='k', alpha=0.7)
    plt.title('Frequency Distribution')
    plt.xlabel('Frequency (Number of Days)')
    plt.ylabel('Frequency')
    st.pyplot(fig)

with tab3:
    st.write("Monetary (M): Menilai seberapa banyak uang yang dihabiskan oleh pelanggan dalam aktivitas tertentu. Pelanggan yang menghabiskan lebih banyak uang cenderung lebih berharga bagi bisnis.")
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.hist(day_df['Monetary'], bins=30, edgecolor='k', alpha=0.7)
    plt.title('Monetary Distribution')
    plt.xlabel('Monetary (Count of Bike Rentals)')
    plt.ylabel('Frequency')
    st.pyplot(fig)
