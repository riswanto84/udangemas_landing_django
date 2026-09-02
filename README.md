# Landing Page Udang Emas Nusantara — Django

Landing page mobile-first bernuansa hijau dan emas, terinspirasi pola halaman perusahaan aquaculture modern tanpa menyalin identitas visual pihak lain.

## Konten yang dapat dikelola dari Admin

- Identitas perusahaan, tagline, logo udang, favicon, warna tema
- Gambar hero, judul, deskripsi, dan tombol hero
- Tentang Kami, gambar/video, visi dan misi
- Keunggulan, statistik tambak, nilai perusahaan
- Struktur organisasi: Founder, Manajer Operasional, Teknisi, Tim Operasional
- Nama/foto personel organisasi
- Fasilitas beserta gambar
- Galeri tambak
- Nomor WhatsApp, email, alamat, media sosial, CTA dan SEO

## Instalasi

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_landing
python manage.py createsuperuser
python manage.py runserver
```

Website: `http://127.0.0.1:8000/`  
Admin: `http://127.0.0.1:8000/admin/`

## Unggah gambar

Format yang disarankan: JPG, PNG, atau WebP. Gambar disimpan dalam folder `media/`. Pastikan server produksi memiliki izin tulis ke folder tersebut.

## Produksi

Sebelum dipasang di VPS, ubah `SECRET_KEY`, matikan `DEBUG`, isi `ALLOWED_HOSTS`, jalankan `collectstatic`, lalu gunakan Gunicorn dan Nginx.
# udangemas_landing_django
