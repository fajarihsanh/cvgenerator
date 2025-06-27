# CV Generator - Aplikasi Web Generator CV

Aplikasi Django untuk membuat dan mengelola CV pribadi dengan fitur OAuth login (Google & GitHub) dan editor WYSIWYG.

## 🚀 Fitur Utama

- ✅ Login/Logout menggunakan OAuth 2.0 (Google dan GitHub)
- ✅ Form CV dengan CKEditor (WYSIWYG)
- ✅ Dashboard CV user (buat, edit, tampilkan)
- ✅ Autentikasi dan proteksi data per user
- ✅ UI/UX modern dengan Bootstrap 5
- ✅ Responsive design

## 🛠️ Teknologi yang Digunakan

- **Backend**: Python 3, Django 5.2.3
- **Frontend**: Bootstrap 5, Font Awesome
- **Editor**: CKEditor 4
- **OAuth**: social-auth-app-django
- **Database**: SQLite3 (development)
- **Hosting**: PythonAnywhere

## 📁 Struktur Proyek

```
cvgen/
├── env/                          # Virtual environment
├── cvgen_project/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── resume/                      # Main app
│   ├── models.py               # CV model
│   ├── views.py                # Views
│   ├── forms.py                # Forms
│   ├── urls.py                 # URL patterns
│   └── admin.py                # Admin interface
├── templates/                   # HTML templates
│   ├── base.html
│   └── resume/
│       ├── login.html
│       ├── dashboard.html
│       └── edit_cv.html
├── media/                       # Uploaded files
├── static/                      # Static files
├── requirements.txt             # Dependencies
├── manage.py                    # Django management
└── README.md                    # This file
```

## 🚀 Instalasi & Setup Lokal

### 1. Clone Repository
```bash
git clone <repository-url>
cd cvgen
```

### 2. Setup Virtual Environment
```bash
python3 -m venv env
source env/bin/activate  # Linux/Mac
# atau
env\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
```bash
# Google OAuth
export GOOGLE_CLIENT_ID="your_google_client_id"
export GOOGLE_CLIENT_SECRET="your_google_client_secret"

# GitHub OAuth
export GITHUB_CLIENT_ID="your_github_client_id"
export GITHUB_CLIENT_SECRET="your_github_client_secret"
```

### 5. Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Akses aplikasi di: http://localhost:8000

## 🔐 Setup OAuth

### Google OAuth Setup
1. Buka [Google Cloud Console](https://console.cloud.google.com/)
2. Buat project baru atau pilih yang ada
3. Aktifkan "Google+ API" dan "Google OAuth2 API"
4. Buat OAuth 2.0 Client ID
5. Authorized redirect URI: `http://localhost:8000/auth/complete/google-oauth2/`
6. Simpan Client ID dan Client Secret

### GitHub OAuth Setup
1. Buka [GitHub Developer Settings](https://github.com/settings/developers)
2. Klik "New OAuth App"
3. Authorization callback URL: `http://localhost:8000/auth/complete/github/`
4. Simpan Client ID dan Client Secret

## 🌐 Deployment ke PythonAnywhere

### 1. Buat Akun PythonAnywhere
- Daftar di [pythonanywhere.com](https://www.pythonanywhere.com/)

### 2. Clone Repository
```bash
git clone <repository-url>
cd cvgen
```

### 3. Setup Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.9 cvgen-env
pip install -r requirements.txt
```

### 4. Konfigurasi Environment Variables
- Di dashboard PythonAnywhere, masuk ke "Web" > "Environment Variables"
- Tambahkan:
  - `GOOGLE_CLIENT_ID`
  - `GOOGLE_CLIENT_SECRET`
  - `GITHUB_CLIENT_ID`
  - `GITHUB_CLIENT_SECRET`

### 5. Konfigurasi WSGI
Edit file WSGI di dashboard PythonAnywhere:
```python
import os
import sys
path = '/home/username/cvgen'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'cvgen_project.settings'
```

### 6. Setup Static & Media Files
- Di dashboard PythonAnywhere, atur static files:
  - URL: `/static/` → path: `/home/username/cvgen/static/`
  - URL: `/media/` → path: `/home/username/cvgen/media/`

### 7. Database & Static Files
```bash
python manage.py migrate
python manage.py collectstatic
```

### 8. Reload Web App
- Klik "Reload" di dashboard PythonAnywhere

## 📝 Penggunaan

### 1. Login
- Akses aplikasi
- Pilih login dengan Google atau GitHub
- Authorize aplikasi

### 2. Buat/Edit CV
- Klik "Edit CV" di dashboard
- Isi informasi:
  - Nama lengkap
  - Jabatan/Posisi
  - Tentang saya (deskripsi)
  - Pengalaman kerja
  - Pendidikan
  - Keahlian
- Gunakan CKEditor untuk formatting
- Klik "Simpan CV"

### 3. Lihat CV
- CV akan ditampilkan di dashboard
- Format yang rapi dan profesional

## 🔧 Admin Panel

Akses admin panel di: http://localhost:8000/admin/
- Username: admin
- Password: (yang dibuat saat setup)

## 📋 Requirements

Lihat `requirements.txt` untuk daftar lengkap dependencies.

## 🤝 Contributing

1. Fork repository
2. Buat feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 License

Proyek ini dibuat untuk keperluan UAS. Silakan gunakan sesuai kebutuhan.

## 🆘 Troubleshooting

### Error OAuth
- Pastikan Client ID dan Secret sudah benar
- Periksa redirect URI di provider OAuth
- Pastikan environment variables sudah diset

### Error Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Error Static Files
```bash
python manage.py collectstatic
```

## 📞 Support

Jika ada pertanyaan atau masalah, silakan buat issue di repository ini. 