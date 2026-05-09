import streamlit as st
from streamlit_autorefresh import st_autorefresh
import boto3
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Akıllı Şehir Sıcaklık İzleme",
    page_icon="🌡️",
    layout="wide"
)

st_autorefresh(interval=5000, key="datarefresh")

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("TemperatureData")

response = table.scan()
items = response["Items"]
df = pd.DataFrame(items)

st.title("🌡️ Akıllı Şehir Sıcaklık İzleme Sistemi")
st.write("IoT sensörlerinden gelen sıcaklık verilerinin gerçek zamanlı izlenmesi.")

if not df.empty:
    df["temperature"] = df["temperature"].astype(float)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    latest = df.iloc[-1]
    avg_temp = df["temperature"].mean()
    max_temp = df["temperature"].max()
    min_temp = df["temperature"].min()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Son Sıcaklık", f"{latest['temperature']:.2f} °C")
    col2.metric("Ortalama", f"{avg_temp:.2f} °C")
    col3.metric("En Yüksek", f"{max_temp:.2f} °C")
    col4.metric("En Düşük", f"{min_temp:.2f} °C")

    st.divider()

    selected_location = st.selectbox(
        "Konum seç",
        ["Tümü"] + sorted(df["location"].unique().tolist())
    )

    if selected_location != "Tümü":
        filtered_df = df[df["location"] == selected_location]
    else:
        filtered_df = df

    st.subheader("📈 Sıcaklık Zaman Grafiği")

    fig = px.line(
        filtered_df,
        x="timestamp",
        y="temperature",
        color="location",
        markers=True,
        title="Konumlara Göre Sıcaklık Değişimi"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🔥 En Sıcak Bölge")

    hottest = df.loc[df["temperature"].idxmax()]

    st.info(
        f"En yüksek sıcaklık **{hottest['location']}** konumunda "
        f"**{hottest['temperature']:.2f} °C** olarak ölçüldü."
    )

    st.subheader("🚨 Sıcaklık Uyarıları")

    warning_df = df[df["temperature"] >= 35]

    if not warning_df.empty:
        st.error("35°C üzeri sıcaklık değerleri tespit edildi!")
        st.dataframe(warning_df.tail(10), use_container_width=True)
    else:
        st.success("Şu anda kritik sıcaklık değeri bulunmuyor.")

    st.subheader("📋 Son Veriler")
    st.dataframe(df.tail(20), use_container_width=True)

else:
    st.warning("Henüz veri bulunamadı.")