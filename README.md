| **Fitur**           | **Deskripsi**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| **Info**            | Menampilkan informasi tentang bot dan fitur-fitur yang tersedia.                |
| **Create Repo**     | Membuat repositori baru di GitHub dengan nama yang diberikan.                    |
| **List Repos**      | Menampilkan daftar repositori GitHub yang dimiliki oleh pengguna.                |
| **Delete Repo**     | Menghapus repositori dari GitHub dengan nama yang diberikan.                     |
| **Edit File**       | Mengedit konten file di repositori GitHub yang ditentukan.                        |
| **Repo Link**       | Menampilkan link ke repositori GitHub yang ditentukan.                           |
| **List Local Folders** | Menampilkan daftar folder dan file di direktori lokal yang telah ditentukan.   |
| **Upload File**     | Mengunggah file dari folder lokal ke repositori GitHub yang dipilih.              |
| **Upload Folder**   | Mengunggah seluruh folder dari folder lokal ke repositori GitHub yang dipilih.    |
| **Delete Folder**   | Menghapus folder dari direktori lokal yang ditentukan.                            |
| **Handle File**     | Mengunggah file yang dikirim melalui Telegram ke repositori GitHub default.      |


| Langkah | Deskripsi |
|---------|-----------|
| **1.**  | **Install Python**: Unduh dan instal Python dari [python.org](https://www.python.org/downloads/). |
| **2.**  | **Buat Virtual Environment**: Jalankan `python -m venv env` untuk membuat lingkungan virtual. |
| **3.**  | **Aktifkan Virtual Environment**: <br> Windows: `env\Scripts\activate` <br> macOS/Linux: `source env/bin/activate` |
| **4.**  | **Install Dependencies**: Jalankan `pip install python-telegram-bot[async] PyGithub requests` untuk menginstal library yang diperlukan. |
| **5.**  | **Set Token dan API Key**: Masukkan token bot Telegram dan GitHub ke dalam variabel `TELEGRAM_BOT_TOKEN` dan `GITHUB_ACCESS_TOKEN` di kode bot. |
| **6.**  | **Siapkan Direktori Kerja**: Pastikan direktori lokal sesuai dengan `LOCAL_DIRECTORY` di kode bot. |
| **7.**  | **Jalankan Bot**: Simpan kode bot sebagai `bot.py` dan jalankan dengan `python bot.py`. |
| **8.**  | **Verifikasi**: Kirim perintah `/start` ke bot di Telegram untuk memastikan bot berjalan dengan baik. |


Jangan lupa untuk join [telegram](https://t.me/allabout_internet)
