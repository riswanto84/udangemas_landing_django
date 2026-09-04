from django.db import migrations


def update_landing_content(apps, schema_editor):
    CompanyValue = apps.get_model("landing", "CompanyValue")
    Facility = apps.get_model("landing", "Facility")

    # Pastikan nilai Keberlanjutan memiliki ikon Bootstrap Icons yang tampil.
    CompanyValue.objects.filter(title="Keberlanjutan").update(icon="leaf-fill")

    # Tambahkan fasilitas genset sebagai sumber listrik cadangan tambak.
    facility, _ = Facility.objects.get_or_create(
        title="Genset",
        defaults={
            "description": "Sumber listrik cadangan untuk menjaga operasional tambak",
            "icon": "lightning-charge-fill",
            "order": 7,
            "is_active": True,
        },
    )
    if facility.icon != "lightning-charge-fill" or facility.order != 7 or not facility.is_active:
        facility.icon = "lightning-charge-fill"
        facility.description = "Sumber listrik cadangan untuk menjaga operasional tambak"
        facility.order = 7
        facility.is_active = True
        facility.save(update_fields=["icon", "description", "order", "is_active"])


def reverse_landing_content(apps, schema_editor):
    Facility = apps.get_model("landing", "Facility")
    CompanyValue = apps.get_model("landing", "CompanyValue")
    Facility.objects.filter(title="Genset").delete()
    CompanyValue.objects.filter(title="Keberlanjutan").update(icon="leaf")


class Migration(migrations.Migration):
    dependencies = [
        ("landing", "0002_sectionsettings_alter_aboutsection_options_and_more"),
    ]

    operations = [
        migrations.RunPython(update_landing_content, reverse_landing_content),
    ]
