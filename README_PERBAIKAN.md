# Udang Emas Nusantara — Landing Page Hijau Premium

## Perbaikan versi ini
- Foto drone tambak pengguna dipasang sebagai background hero/header.
- Header desktop dan mobile dibuat lebih profesional.
- Hero menggunakan overlay hijau gelap agar teks tetap terbaca.
- Statistik tambak menggunakan foto background dan panel premium.
- Nilai perusahaan menggunakan kartu berikon dengan efek hover.
- Struktur organisasi diperbaiki menjadi alur Founder → Manajer Operasional/Teknisi/Tim Operasional.
- Tampilan tetap mobile-first dan responsif di desktop.
- Seluruh konten dan gambar tetap dapat dikelola melalui Django Admin.
- Animasi masuk ringan saat bagian halaman terlihat.

## Menjalankan
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Website: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

## Mengganti foto header melalui admin
Masuk ke **Pengaturan Situs** lalu ubah field **Gambar utama/hero**.

## Perbaikan 4 September 2026
- Menambahkan ikon **Keberlanjutan** (`leaf-fill`) pada bagian Nilai-Nilai Kami.
- Menata ulang Struktur Organisasi agar **Tim Operasional** berada di bawah **Manajer Operasional** berdasarkan relasi atasan-bawahan.
- Menambahkan fasilitas **Genset** dengan ikon `lightning-charge-fill`.
- Menambahkan migration `0003_update_landing_content.py` agar perubahan konten ikut diterapkan pada instalasi baru.
