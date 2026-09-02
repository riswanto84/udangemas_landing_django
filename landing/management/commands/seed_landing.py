from django.core.management.base import BaseCommand
from landing.models import SiteSettings, AboutSection, Feature, Mission, PondStat, CompanyValue, OrganizationRole, Facility

class Command(BaseCommand):
    help = "Mengisi konten awal landing page"
    def handle(self, *args, **kwargs):
        SiteSettings.load(); AboutSection.load()
        data = {
            Feature: [
                ("Aman & Terpercaya","Budidaya sesuai standar dan diawasi tim berpengalaman","shield-check"),
                ("Pengawasan Berkala","Pemantauan rutin untuk menjaga kualitas dan kesehatan tambak","calendar-check"),
                ("Data Terintegrasi","Aktivitas tambak tercatat secara digital dan akurat","database"),
                ("Ramah Lingkungan","Budidaya berkelanjutan untuk masa depan perikanan Indonesia","leaf"),
            ],
            Mission: [
                ("Produksi premium","Menghasilkan udang vaname premium dengan standar budidaya terbaik","check-circle"),
                ("Tambak modern","Mengembangkan tambak modern berbasis teknologi digital","cpu"),
                ("Berkelanjutan","Menerapkan budidaya ramah lingkungan dan berkelanjutan","leaf"),
                ("Masyarakat pesisir","Meningkatkan kesejahteraan masyarakat pesisir","people"),
                ("Kemitraan","Menjadi mitra terpercaya bagi pembeli, distributor, dan investor","handshake"),
            ],
            CompanyValue: [
                ("Integritas","Kejujuran adalah dasar setiap langkah kami","shield-star"),
                ("Inovasi","Teknologi adalah kunci untuk masa depan","lightbulb"),
                ("Keberlanjutan","Menjaga keseimbangan produktivitas dan lingkungan","leaf"),
                ("Kualitas","Setiap panen harus memenuhi standar terbaik","award"),
                ("Kemitraan","Tumbuh bersama pelanggan, investor, dan masyarakat","handshake"),
            ],
            Facility: [
                ("6 Kolam Pembesaran","Kolam produksi udang vaname","water"),
                ("2 Kolam Tandon","Pengelolaan air budidaya","circle"),
                ("Gudang Pakan","Penyimpanan pakan terkontrol","house"),
                ("Sistem Aerasi Modern","Menjaga oksigen terlarut","wind"),
                ("CCTV Monitoring","Pengawasan keamanan area","camera-video"),
                ("Sensor Kualitas Air","Pengujian parameter air berkala","droplet"),
                ("Smart Shrimp Farm","Manajemen tambak berbasis data","display"),
            ],
        }
        for model, rows in data.items():
            if not model.objects.exists():
                for i,(title,desc,icon) in enumerate(rows): model.objects.create(title=title,description=desc,icon=icon,order=i)
        if not PondStat.objects.exists():
            for i,row in enumerate([("Luas Tambak","2,5 Ha","water"),("Kolam Pembesaran","6","circle"),("Kolam Tandon","2","circle"),("Pengawasan Berkala","Rutin","calendar-check"),("Pengawasan Keamanan","24/7","shield-check")]):
                PondStat.objects.create(title=row[0],value=row[1],icon=row[2],order=i)
        if not OrganizationRole.objects.exists():
            founder=OrganizationRole.objects.create(title="Founder",description="Memimpin strategi bisnis, pengembangan perusahaan, dan inovasi teknologi.",icon="person-badge",order=0)
            for i,row in enumerate([("Manajer Operasional","Bertanggung jawab atas perencanaan, pengawasan, dan evaluasi operasional tambak.","gear"),("Teknisi","Melakukan pemeliharaan peralatan, monitoring kualitas air, dan dukungan teknis.","wrench-adjustable"),("Tim Operasional","Melaksanakan kegiatan harian tambak secara konsisten untuk produktivitas optimal.","people")],1):
                OrganizationRole.objects.create(title=row[0],description=row[1],icon=row[2],parent=founder,order=i)
        self.stdout.write(self.style.SUCCESS("Konten awal berhasil dibuat."))
