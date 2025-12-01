# 🤖 Python Telegram Chatbot Projesi

Bu proje, temel Python programlama, asenkron programlama ve dış API entegrasyonu becerilerini sergilemek amacıyla geliştirilmiş basit bir Telegram botudur. 

## ✨ Özellikler

Bot, kullanıcı etkileşimlerini işlemek için `python-telegram-bot` kütüphanesini kullanır ve aşağıdaki komutları destekler:

* `/start`: Botu başlatır.
* `/yardim`: Desteklenen tüm komutları listeler.
* `/topla <sayi1> <sayi2>`: Kullanıcıdan gelen iki sayıyı toplar (Temel Hata Yönetimi içerir).
* `/bilgi`: Harici bir API'dan rastgele bir bilimsel gerçeği çeker (`requests` kütüphanesi ile API entegrasyonu örneği).
* **Echo Fonksiyonu**: "selam" ve "hava" gibi anahtar kelimelere basit cevaplar verir.

## ⚙️ Kullanılan Teknolojiler

* **Dil**: Python 3.x
* **Telegram API**: `python-telegram-bot` (En güncel `ApplicationBuilder` yapısı ile uyumlu)
* **Harici Veri Çekme**: `requests`
* **Güvenlik**: `python-dotenv` (Token gizleme)

## 🚀 Kurulum ve Çalıştırma

Bu projeyi yerel ortamınızda çalıştırmak için:

### 1. Kütüphaneleri Yükleme
Projenin bağımlılıklarını yükleyin:
```bash
pip install -r requirements.txt
