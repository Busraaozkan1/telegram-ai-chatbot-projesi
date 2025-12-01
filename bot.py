import requests  # İnternetten veri çekmek için ekledim
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
from telegram.ext import filters as MessageFilters, ContextTypes

# Botun gizli anahtarı. Burayı kimse görmemeli!
TOKEN = "8323548162:AAEs6nLLThNAdjDfqeuL-GwF1_adcG-P--w"


# FONKSİYONLAR (BOTUN YAPABİLDİKLERİ)

# 1. /start komutuna cevap verir
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Asenkron çalışması gerektiği için 'await' kullanıyoruz.
    await update.message.reply_text("Merhaba! Python AI Chatbot çalışmaya hazır!")


# 2. /yardim komutuna cevap verir (Tüm komutları listeler)
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    yardim_mesaji = (
        "🤖 Botun Bildiği Şeyler:\n"
        "/start - Botu yeniden başlatır.\n"
        "/yardim - Bu listeyi görürsün.\n"
        "/topla <sayi1> <sayi2> - İki sayıyı toplar.\n"
        "/bilgi - İnternetten rastgele bir bilgi çeker. (YENİ!)\n"
        "Ayrıca 'selam' ve 'hava' kelimelerine de bakıyorum."
    )
    await update.message.reply_text(yardim_mesaji)


# 3. /topla komutunu işler (Basit Hesap Makinesi)
async def topla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args  # Komuttan sonra yazılan her şeyi yakalar

    if len(args) != 2:
        await update.message.reply_text("Lütfen sadece 2 sayı girin. Örnek: /topla 5 3")
        return

    try:
        # Gelen metinleri sayıya çevirmeye çalış
        sayi1 = float(args[0])
        sayi2 = float(args[1])

        sonuc = sayi1 + sayi2

        await update.message.reply_text(f"Sonuç: {sonuc}")

    except ValueError:
        # Sayısal olmayan bir giriş gelirse hatayı yakalarız
        await update.message.reply_text("Toplama için geçerli sayılar kullandığından emin ol.")


# 4. /bilgi komutunu işler (İnternetten API ile veri çeker)
async def bilgi_getir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Dış bir API'ya HTTP GET isteği gönderiyorum.
        api_url = "https://uselessfacts.jsph.pl/random.json?language=en"
        yanit = requests.get(api_url)

        # İstek başarısız olursa (örn. sunucu hatası) istisna fırlat.
        yanit.raise_for_status()

        # Gelen JSON cevabını Python'da kullanılabilir hale getir.
        veri = yanit.json()

        # Çektiğimiz JSON verisinden sadece 'text' alanını alıyorum.
        rastgele_bilgi = veri.get("text")

        await update.message.reply_text(f"🧠 Rastgele Bilgi: {rastgele_bilgi}")

    except requests.exceptions.RequestException as e:
        # İnternet bağlantısı veya API'dan kaynaklı sorunları kullanıcıya bildiririm.
        print(f"API'ya erişimde sorun: {e}")
        await update.message.reply_text("Üzgünüm, şu an internetten bilgi çekemiyorum.")


# 5. Normal Mesajları İşleyici (Komut olmayan her şeyi yakalar)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mesaj = update.message.text.lower()

    if "selam" in mesaj:
        await update.message.reply_text("Selam! Nasılsın?")
    elif "hava" in mesaj:
        await update.message.reply_text("Benim için hava hep güneşli! 😎")
    else:
        await update.message.reply_text(f"Bunu anlayamadım: {mesaj}")


# ANA PROGRAM AKIŞI

def main():
    # Botun ana uygulamasını (Application) token ile kuruyoruz.
    application = ApplicationBuilder().token(TOKEN).build()

    # Handler'ları (İşleyicileri) botun uygulamasına ekliyorum:

    # Komut Handler'ları
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("yardim", help_command))
    application.add_handler(CommandHandler("topla", topla))
    application.add_handler(CommandHandler("bilgi", bilgi_getir))  # YENİ HANDLER

    # Mesaj Handler'ı
    # Metin mesajlarını yakalar ve komut olanları hariç tutar (echo fonksiyonu için).
    application.add_handler(MessageHandler(MessageFilters.TEXT & ~MessageFilters.COMMAND, echo))

    # Botu başlat ve gelen mesajları sürekli dinle.
    application.run_polling()


if __name__ == "__main__":
    main()