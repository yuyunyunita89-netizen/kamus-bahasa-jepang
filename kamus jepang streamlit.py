# kamus_jepang_streamlit.py

import streamlit as st

# Data kamus
kamus = {
    "aku": "私 (わたし)",
    "kamu": "あなた",
    "dia (laki-laki)": "彼 (かれ)",
    "dia (perempuan)": "彼女 (かのじょ)",
    "kami": "私たち (わたしたち)",
    "kita": "私たち (わたしたち)",
    "mereka": "彼ら (かれら)",
    "ini": "これ",
    "itu": "それ",
    "apa": "何 (なに)",
    "siapa": "誰 (だれ)",
    "dimana": "どこ",
    "kapan": "いつ",
    "mengapa": "なぜ",
    "bagaimana": "どうやって",
    "ya": "はい",
    "tidak": "いいえ",
    "baik": "良い (よい) / いい",
    "buruk": "悪い (わるい)",
    "besar": "大きい (おおきい)",
    "kecil": "小さい (ちいさい)",
    "panjang": "長い (ながい)",
    "pendek": "短い (みじかい)",
    "tinggi": "高い (たかい)",
    "rendah": "低い (ひくい)",
    "cepat": "速い (はやい)",
    "lambat": "遅い (おそい)",
    "lama": "長い (ながい)",
    "baru": "新しい (あたらしい)",
    "tua": "年寄りの (としよりの)",
    "muda": "若い (わかい)",
    "cantik": "美しい (うつくしい)",
    "jelek": "醜い (みにくい)",
    "kaya": "裕福な (ゆうふくな)",
    "miskin": "貧しい (まずしい)",
    "senang": "嬉しい (うれしい)",
    "sedih": "悲しい (かなしい)",
    "marah": "怒る (おこる)",
    "takut": "怖い (こわい)",
    "kaget": "驚く (おどろく)",
    "luka": "傷 (きず)",
    "sehat": "健康な (けんこうな)",
    "sakit": "病気 (びょうき)",
    "air": "水 (みず)",
    "api": "火 (ひ)",
    "tanah": "土 (つち)",
    "udara": "空気 (くうき)",
    "langit": "空 (そら)",
    "matahari": "太陽 (たいよう)",
    "bulan": "月 (つき)",
    "bintang": "星 (ほし)",
    "hujan": "雨 (あめ)",
    "salju": "雪 (ゆき)",
    "angin": "風 (かぜ)",
    "awan": "雲 (くも)",
    "gunung": "山 (やま)",
    "laut": "海 (うみ)",
    "sungai": "川 (かわ)",
    "danau": "湖 (みずうみ)",
    "hutan": "森 (もり)",
    "kota": "町 (まち)",
    "desa": "村 (むら)",
    "rumah": "家 (いえ)",
    "sekolah": "学校 (がっこう)",
    "kantor": "事務所 (じむしょ)",
    "toko": "店 (みせ)",
    "rumah sakit": "病院 (びょういん)",
    "tempat": "場所 (ばしょ)",
    "jalan": "道 (みち)",
    "jembatan": "橋 (はし)",
    "kereta": "電車 (でんしゃ)",
    "mobil": "車 (くるま)",
    "bis": "バス",
    "motor": "バイク / オートバイ",
    "pesawat": "飛行機 (ひこうき)",
    "kapal": "船 (ふね)",
    "roda": "車輪 (しゃりん)",
    "tangga": "階段 (かいだん)",
    "pintu": "ドア / 扉 (とびら)",
    "jendela": "窓 (まど)",
    "kursi": "椅子 (いす)",
    "meja": "机 (つくえ)",
    "buku": "本 (ほん)",
    "pensil": "鉛筆 (えんぴつ)",
    "pena": "ペン",
    "kertas": "紙 (かみ)",
    "gambar": "絵 (え)",
    "kata": "言葉 (ことば)",
    "kalimat": "文 (ぶん)",
    "bahasa": "言語 (げんご) / 言葉 (ことば)",
    "belajar": "学ぶ (まなぶ)",
    "mengajar": "教える (おしえる)",
    "menulis": "書く (かく)",
    "membaca": "読む (よむ)",
    "berbicara": "話す (はなす)",
    "mendengar": "聞く (きく)",
    "melihat": "見る (みる)",
    "datang": "来る (くる)",
    "pergi": "行く (いく)",
    "tidur": "寝る (ねる)",
    "bangun": "起きる (おきる)",
    "bermain": "遊ぶ (あそぶ)",
    "kerja": "働く (はたらく)",
    "istirahat": "休む (やすむ)",
    "makan": "食べる (たべる)",
    "minum": "飲む (のむ)",
}

# Antarmuka Streamlit
st.title("📖 Kamus Indonesia ↔ Jepang")

menu = st.sidebar.selectbox("Pilih Menu", [
    "Cari arti (Indonesia → Jepang)",
    "Cari arti (Jepang → Indonesia)",
    "Tambah kata baru",
    "Tampilkan semua isi kamus"
])

if menu == "Cari arti (Indonesia → Jepang)":
    kata = st.text_input("Masukkan kata dalam Bahasa Indonesia").strip().lower()
    if kata:
        arti = kamus.get(kata)
        if arti:
            st.success(f"➡️ {kata} = {arti}")
        else:
            st.warning("Kata tidak ditemukan dalam kamus.")

elif menu == "Cari arti (Jepang → Indonesia)":
    kata = st.text_input("Masukkan kata dalam Bahasa Jepang").strip()
    if kata:
        hasil = []
        for indo, jepang in kamus.items():
            if jepang == kata or kata in jepang:
                hasil.append(f"{jepang} = {indo}")
        if hasil:
            st.success("Hasil pencarian:")
            for item in hasil:
                st.write(f"➡️ {item}")
        else:
            st.warning("Kata tidak ditemukan dalam kamus.")

elif menu == "Tambah kata baru":
    indo = st.text_input("Masukkan kata dalam Bahasa Indonesia").strip().lower()
    jepang = st.text_input("Masukkan arti dalam Bahasa Jepang").strip()

    if st.button("Tambah ke Kamus"):
        if indo in kamus:
            st.error("❌ Kata sudah ada dalam kamus.")
        elif not indo or not jepang:
            st.error("❌ Mohon isi kedua kolom.")
        else:
            kamus[indo] = jepang
            st.success(f"✅ Kata '{indo}' telah ditambahkan.")

elif menu == "Tampilkan semua isi kamus":
    st.subheader("📚 Isi Kamus (Indonesia → Jepang):")
    for indo in sorted(kamus.keys()):
        st.write(f"**{indo}** → {kamus[indo]}")
