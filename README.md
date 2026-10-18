# Password Toolkit

[![DevSecOps Pipeline](https://github.com/DimarRenantheraRiyadi/devsecops-p5-0110225024/actions/workflows/devsecops.yml/badge.svg)](https://github.com/DimarRenantheraRiyadi/devsecops-p5-0110225024/actions/workflows/devsecops.yml)

Tugas Pertemuan Ke-5 mata kuliah DevSecOps, Teknik Informatika, STT Terpadu Nurul Fikri.

- Nama: Dimar Renanthera Riyadi
- NIM: 0110225024

## 1. Nama Aplikasi & Fungsinya

**Password Toolkit** adalah aplikasi command-line (CLI) untuk membantu keamanan password. Fitur:

| Menu | Fungsi | Modul |
|---|---|---|
| 1 | Mengecek kekuatan password (skor 0-6: Lemah / Sedang / Kuat) | `src/strength.py` |
| 2 | Membuat password acak yang aman (modul `secrets`) | `src/generator.py` |
| 3 | Meng-hash password dengan salt (PBKDF2-HMAC-SHA256) | `src/hasher.py` |
| 4 | Memverifikasi password terhadap hash yang tersimpan | `src/hasher.py` |

Modul pendukung: `src/validator.py` (validasi input) dan `src/main.py` (menu CLI).

## 2. Bahasa & Framework

- Bahasa: **Python 3.10+**
- Library: hanya standard library Python (`secrets`, `hashlib`, `hmac`, `re`, `getpass`)
- Unit test: **pytest**
- SAST tool: **Bandit**

## 3. Cara Menjalankan

```bash
# 1. Clone repository
git clone https://github.com/DimarRenantheraRiyadi/devsecops-p5-0110225024.git
cd devsecops-p5-0110225024

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan aplikasi
python -m src.main

# 4. Jalankan unit test
python -m pytest

# 5. Jalankan SAST scan secara lokal
bandit -r src
```

Catatan: di Windows, gunakan `py` sebagai pengganti `python` jika perintah `python` tidak dikenali.

## 4. Overview Pipeline CI/CD

Pipeline didefinisikan di `.github/workflows/devsecops.yml` dan berjalan di GitHub Actions
(runner `ubuntu-latest`).

**Trigger:** `push` ke branch `main` dan `pull_request` ke branch `main`.

| Job | Fungsi | Tahapan |
|---|---|---|
| `build` | Build & unit test | Checkout, setup Python 3.12, install dependencies, jalankan pytest |
| `sast-scan` | SAST scan dengan Bandit (`needs: build`) | Checkout, setup Python 3.12, install Bandit, scan folder `src` |

**Quality Gate:** job `sast-scan` hanya berjalan jika job `build` lulus. Bandit dikonfigurasi
dengan `--severity-level medium --confidence-level medium`. Jika ditemukan kerentanan
tingkat medium atau lebih tinggi, Bandit keluar dengan status gagal dan pipeline otomatis
ditandai merah.

## Struktur Repository

```
.
├── .github/workflows/devsecops.yml   # definisi pipeline
├── src/                              # source code aplikasi
├── tests/                            # unit test (pytest)
├── pytest.ini
├── requirements.txt
└── README.md
```