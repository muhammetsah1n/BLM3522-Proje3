# 🌡️ IoT Tabanlı Akıllı Şehir Sıcaklık İzleme Sistemi

Bu proje, AWS bulut servisleri ve IoT teknolojileri kullanılarak geliştirilmiş gerçek zamanlı sıcaklık izleme sistemidir.

Sistem üzerinden sanal sıcaklık sensörlerinden veri toplanmakta, AWS servisleri üzerinde işlenmekte ve dashboard üzerinden gerçek zamanlı olarak görselleştirilmektedir.

---

# Tanıtım Videosu
- [İzlemek İçin Tıklayınız.](https://www.youtube.com/watch?v=WAEJAXe61Io)

---
# 📌 Proje Özeti

Projede Python ile geliştirilmiş sanal IoT sensörleri kullanılmıştır. Sensörlerden elde edilen sıcaklık verileri MQTT protokolü ile AWS IoT Core servisine gönderilmektedir.

AWS IoT Core üzerinden gelen veriler AWS Lambda tarafından işlenmekte ve DynamoDB veritabanına kaydedilmektedir.

Son olarak Streamlit kullanılarak geliştirilen dashboard üzerinden sıcaklık verileri gerçek zamanlı olarak görüntülenmektedir.

---

# 🚀 Kullanılan Teknolojiler

- Python
- MQTT
- AWS IoT Core
- AWS Lambda
- DynamoDB
- Streamlit
- Plotly
- Boto3
- Paho MQTT

---

# 🏗️ Sistem Mimarisi

```text
Python Sensör Simülatörü
        ↓ MQTT
AWS IoT Core
        ↓ IoT Rule
AWS Lambda
        ↓
DynamoDB
        ↓
Streamlit Dashboard
```

---

# 📂 Proje Yapısı

```text
Proje3/
│
├── sensor_simulator/
│   └── publish_temperature.py
│
├── dashboard/
│   └── app.py
│
├── lambda/
│   └── lambda_function.py
│
├── certificates/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Kurulum

## 1. Repository Klonlama

```bash
git clone https://github.com/muhammetsah1n/BLM3522-Proje3.git
```

---

## 2. Sanal Ortam Oluşturma

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Gereksinimleri Kurma

```bash
pip install -r requirements.txt
```

---

# ☁️ AWS Yapılandırması

Projede aşağıdaki AWS servisleri kullanılmıştır:

- AWS IoT Core
- AWS Lambda
- DynamoDB
- IAM

AWS IoT Core üzerinde:
- Thing oluşturulmuştur
- Sertifikalar oluşturulmuştur
- MQTT erişim izinleri verilmiştir

DynamoDB üzerinde:
- `TemperatureData` isimli tablo oluşturulmuştur.

---

# 📡 Sensör Simülatörünü Çalıştırma

```bash
cd sensor_simulator
python publish_temperature.py
```

Sistem çalıştığında sıcaklık verileri AWS IoT Core’a gönderilecektir.

---

# 📊 Dashboard Çalıştırma

```bash
cd dashboard
streamlit run app.py
```

Dashboard adresi:

```text
http://localhost:8501
```

---

# 📷 Dashboard Özellikleri

Dashboard üzerinde:

- Gerçek zamanlı sıcaklık grafikleri
- Ortalama sıcaklık değerleri
- En yüksek sıcaklık bilgisi
- Kritik sıcaklık uyarıları
- Sensör veri tablosu

gösterilmektedir.

---

# 🔒 Güvenlik

AWS IoT Core bağlantılarında:

- Device Certificate
- Private Key
- Root CA

kullanılarak TLS tabanlı güvenli bağlantı sağlanmıştır.

---

# 🧪 Sistem Özellikleri

✅ Gerçek zamanlı veri akışı  
✅ MQTT protokolü kullanımı  
✅ AWS IoT Core entegrasyonu  
✅ Serverless mimari  
✅ DynamoDB veri saklama  
✅ Gerçek zamanlı dashboard  
✅ Otomatik veri güncelleme  
