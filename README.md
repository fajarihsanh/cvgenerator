# CV Generator - Aplikasi Web Pembuat CV Otomatis

Proyek Django ini adalah aplikasi web untuk membuat, mengedit, dan mengelola Curriculum Vitae (CV) secara personal. Mendukung login menggunakan OAuth (Google dan GitHub), dilengkapi dengan editor WYSIWYG berbasis CKEditor untuk kemudahan pengisian konten CV.

---

## 🚀 Fitur Unggulan

* 🔐 Autentikasi menggunakan OAuth 2.0 (Google & GitHub)
* 📝 Editor CV berbasis CKEditor (WYSIWYG)
* 📋 CRUD CV: buat, tampilkan, edit, hapus, dan unduh PDF
* 🖼️ Upload foto profil ke dalam CV
* 🔐 Keamanan data per user
* 💻 UI/UX modern dan responsive menggunakan Bootstrap 5

---

## 🛠️ Teknologi yang Digunakan

* **Backend**: Python 3 + Django 5.2.x
* **Frontend**: Bootstrap 5, Font Awesome, Google Fonts
* **Editor**: CKEditor (via django-ckeditor)
* **OAuth**: social-auth-app-django
* **Export PDF**: WeasyPrint
* **Database**: SQLite3 (untuk pengembangan lokal)
* **Deployment**: PythonAnywhere

---

## 📚 Library Python

* `django` — Framework utama
* `social-auth-app-django` — OAuth login
* `django-ckeditor` — WYSIWYG editor
* `weasyprint` — Export ke PDF
* `pillow` — Upload gambar
* `python-dotenv` — Load file .env
* `requests` — Client HTTP (OAuth)

---

## 🌐 API Eksternal

* **Google OAuth 2.0 API** — Login Google
* **GitHub OAuth API** — Login GitHub
* **Google Fonts API** — Font Inter
* **Bootstrap CDN & FontAwesome** — Tampilan frontend

---

## 📁 Struktur Folder

```
cvgen/
├── env/                      # Virtual environment
├── cvgen_project/           # Pengaturan proyek Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── resume/                  # App utama
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   ├── base.html
│   └── resume/
│       ├── login.html
│       ├── dashboard.html
│       └── edit_cv.html
├── media/                   # Upload user
├── static/                  # File statis (ikon, CSS, dsb)
├── requirements.txt         # Daftar dependensi
├── manage.py                # Entrypoint Django
└── README.md                # Dokumentasi
```

---

## 🚀 Instalasi Lokal

### 1. Clone Project

```bash
git clone <repository-url>
cd cvgen
```

### 2. Setup Virtual Environment

```bash
python3 -m venv env
source env/bin/activate  # Linux/macOS
# atau untuk Windows:
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment

Buat file `.env` dan isi:

```env
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_client_id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_client_secret
SOCIAL_AUTH_GITHUB_KEY=your_github_client_id
SOCIAL_AUTH_GITHUB_SECRET=your_github_client_secret
```

### 5. Migrasi Database

```bash
python manage.py migrate
```

### 6. Buat Superuser (opsional)

```bash
python manage.py createsuperuser
```

### 7. Jalankan Server

```bash
python manage.py runserver
```

Akses di: [http://localhost:8000](http://localhost:8000)

---

## 🔐 Konfigurasi OAuth

### Google

1. Akses [Google Cloud Console](https://console.cloud.google.com/)
2. Buat project baru
3. Aktifkan "OAuth 2.0 API"
4. Buat OAuth 2.0 Client ID
5. Redirect URI:

   * `http://localhost:8000/auth/complete/google-oauth2/`
   * `https://<username>.pythonanywhere.com/auth/complete/google-oauth2/`

### GitHub

1. Buka [Developer Settings GitHub](https://github.com/settings/developers)
2. Buat aplikasi baru
3. Callback URL:

   * `http://localhost:8000/auth/complete/github/`
   * `https://<username>.pythonanywhere.com/auth/complete/github/`

---

## 🚀 Deployment di PythonAnywhere

### 1. Setup

```bash
git clone <repository-url>
cd cvgen
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 2. Set Environment Variables di dashboard PythonAnywhere

### 3. Edit WSGI Configuration

```python
import os
import sys
from dotenv import load_dotenv

path = '/home/username/cvgen'
if path not in sys.path:
    sys.path.append(path)
load_dotenv(os.path.join(path, '.env'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'cvgen_project.settings'
```

### 4. Konfigurasi Static & Media Files

* `/static/` → `/home/username/cvgen/static/`
* `/media/` → `/home/username/cvgen/media/`

### 5. Migrasi & Collect Static

```bash
python manage.py migrate
python manage.py collectstatic
```

### 6. Reload Web App dari Dashboard

---

## 🧑‍💻 Cara Pakai

### Login

* Pilih Google atau GitHub untuk login

### Buat/Edit CV

* Isi form: nama, deskripsi, pengalaman, pendidikan, keahlian
* Gunakan editor WYSIWYG
* Simpan CV

### Lihat/Unduh CV

* CV tampil di dashboard
* Bisa diunduh dalam format PDF

---

## 🔧 Admin Panel

Akses: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 🤝 Kontribusi

1. Fork repo
2. Buat branch: `git checkout -b fitur/fiturBaru`
3. Commit: `git commit -m 'Menambahkan fitur'`
4. Push: `git push origin fitur/fiturBaru`
5. Buat Pull Request

---

## 📄 Lisensi

MIT License

---

## 🆘 Troubleshooting

* **OAuth Error**: periksa Client ID, Secret, dan URI redirect
* **Error database**:

```bash
python manage.py migrate
```

* **Error static file**:

```bash
python manage.py collectstatic
```

---

## 📞 Support

Kalau ada masalah, silakan buka issue di repo GitHub proyek ini.
