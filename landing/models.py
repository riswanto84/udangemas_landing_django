from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    company_name = models.CharField("Nama perusahaan", max_length=120, default="Udang Emas Nusantara")
    tagline = models.CharField("Tagline", max_length=180, default="Dari Tambak Nusantara untuk Kualitas Dunia")
    logo = models.ImageField("Logo udang tanpa tulisan", upload_to="branding/", blank=True)
    favicon = models.ImageField("Favicon", upload_to="branding/", blank=True)
    hero_image = models.ImageField("Gambar utama/hero", upload_to="hero/", blank=True)
    hero_badge = models.CharField("Label hero", max_length=80, default="Budidaya Udang Modern")
    hero_title_line_1 = models.CharField("Judul hero", max_length=120, default="Dari Tambak Nusantara untuk")
    hero_title_highlight = models.CharField("Teks sorotan", max_length=80, default="Kualitas Dunia")
    hero_description = models.TextField("Deskripsi hero", default="Udang berkualitas tinggi melalui budidaya modern, teknologi tepat guna, dan pengelolaan profesional yang berkelanjutan.")
    primary_button_text = models.CharField("Teks tombol utama", max_length=60, default="Kenali Kami Lebih Dekat")
    primary_button_url = models.CharField("URL tombol utama", max_length=255, default="#tentang")
    secondary_button_text = models.CharField("Teks tombol kedua", max_length=60, default="Tonton Video")
    secondary_button_url = models.CharField("URL tombol kedua", max_length=255, blank=True, default="#galeri")
    whatsapp_number = models.CharField("Nomor WhatsApp", max_length=30, blank=True, help_text="Contoh: 6281234567890")
    email = models.EmailField("Email", blank=True)
    address = models.CharField("Alamat", max_length=255, default="Muara Gembong, Kabupaten Bekasi")
    instagram_url = models.URLField("Instagram", blank=True)
    youtube_url = models.URLField("YouTube", blank=True)
    tiktok_url = models.URLField("TikTok", blank=True)
    footer_title = models.CharField("Judul CTA", max_length=100, default="Mari Bertumbuh Bersama")
    footer_text = models.CharField("Deskripsi CTA", max_length=180, default="Bersama kita wujudkan tambak Indonesia berkualitas dunia.")
    primary_color = models.CharField("Warna hijau utama", max_length=7, default="#075B37", help_text="Format HEX, contoh #075B37")
    secondary_color = models.CharField("Warna hijau gelap", max_length=7, default="#043C27")
    accent_color = models.CharField("Warna emas", max_length=7, default="#DDAA31")
    meta_description = models.CharField("Deskripsi SEO", max_length=160, blank=True)

    class Meta:
        verbose_name = "Pengaturan Situs"
        verbose_name_plural = "1. Pengaturan Situs"

    def __str__(self):
        return self.company_name


class AboutSection(SingletonModel):
    label = models.CharField(max_length=60, default="Tentang Kami")
    title = models.CharField(max_length=140, default="Budidaya Modern, Berkelanjutan & Terpercaya")
    body = models.TextField(default="Udang Emas Nusantara adalah unit usaha budidaya udang vaname modern di bawah CV Dua Satu Kreasi yang berlokasi di Muara Gembong, Kabupaten Bekasi. Kami menggabungkan pengalaman petambak, teknologi digital, dan manajemen budidaya berbasis data.")
    image = models.ImageField("Gambar tentang kami", upload_to="about/", blank=True)
    video_url = models.URLField("URL video", blank=True, help_text="Opsional: tautan YouTube atau video profil")
    vision = models.TextField(default="Menjadi perusahaan budidaya udang modern Indonesia yang terpercaya, berkelanjutan, dan berbasis teknologi untuk menghasilkan produk berkualitas dunia.")

    class Meta:
        verbose_name = "Tentang, Visi & Narasi"
        verbose_name_plural = "2. Tentang, Visi & Narasi"

    def __str__(self):
        return self.title


class SectionSettings(SingletonModel):
    stats_title = models.CharField(max_length=100, default="Tambak Kami dalam Angka")
    values_title = models.CharField(max_length=100, default="Nilai-Nilai Kami")
    organization_title = models.CharField(max_length=100, default="Struktur Organisasi")
    organization_subtitle = models.CharField(max_length=180, default="Kolaborasi tim yang solid untuk budidaya udang berkualitas tinggi.")
    facilities_title = models.CharField(max_length=100, default="Fasilitas Kami")
    gallery_title = models.CharField(max_length=100, default="Galeri Tambak")

    class Meta:
        verbose_name = "Judul Bagian"
        verbose_name_plural = "3. Judul Bagian"

    def __str__(self):
        return "Judul bagian landing page"


class OrderedContent(models.Model):
    title = models.CharField("Judul", max_length=100)
    description = models.TextField("Deskripsi", blank=True)
    icon = models.CharField("Ikon", max_length=40, blank=True, help_text="Nama Bootstrap Icons, contoh: shield-check, leaf, people")
    order = models.PositiveIntegerField("Urutan", default=0)
    is_active = models.BooleanField("Tampilkan", default=True)

    class Meta:
        abstract = True
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class Feature(OrderedContent):
    class Meta:
        verbose_name = "Keunggulan"
        verbose_name_plural = "4. Keunggulan"


class Mission(OrderedContent):
    class Meta:
        verbose_name = "Misi"
        verbose_name_plural = "5. Misi"


class PondStat(OrderedContent):
    value = models.CharField("Nilai", max_length=40)
    class Meta:
        verbose_name = "Statistik Tambak"
        verbose_name_plural = "6. Statistik Tambak"


class CompanyValue(OrderedContent):
    class Meta:
        verbose_name = "Nilai Perusahaan"
        verbose_name_plural = "7. Nilai Perusahaan"


class OrganizationRole(OrderedContent):
    parent = models.ForeignKey("self", verbose_name="Atasan", null=True, blank=True, on_delete=models.SET_NULL, related_name="children")
    photo = models.ImageField("Foto", upload_to="team/", blank=True)
    person_name = models.CharField("Nama personel", max_length=100, blank=True)
    class Meta:
        verbose_name = "Posisi Organisasi"
        verbose_name_plural = "8. Struktur Organisasi"


class Facility(OrderedContent):
    image = models.ImageField("Gambar fasilitas", upload_to="facilities/", blank=True)
    class Meta:
        verbose_name = "Fasilitas"
        verbose_name_plural = "9. Fasilitas"


class GalleryImage(models.Model):
    title = models.CharField("Judul", max_length=100)
    image = models.ImageField("Gambar", upload_to="gallery/")
    caption = models.CharField("Keterangan", max_length=180, blank=True)
    order = models.PositiveIntegerField("Urutan", default=0)
    is_active = models.BooleanField("Tampilkan", default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Foto Galeri"
        verbose_name_plural = "10. Galeri Tambak"

    def __str__(self):
        return self.title
