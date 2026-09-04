from django.db import migrations


def fix_content(apps, schema_editor):
    CompanyValue = apps.get_model("landing", "CompanyValue")
    OrganizationRole = apps.get_model("landing", "OrganizationRole")

    # Use a Bootstrap Icons glyph that is reliably available.
    CompanyValue.objects.filter(title="Keberlanjutan").update(icon="tree-fill")

    founder = OrganizationRole.objects.filter(title__iexact="Founder").order_by("id").first()
    if not founder:
        founder = OrganizationRole.objects.create(
            title="Founder",
            description="Memimpin strategi bisnis, pengembangan perusahaan, dan inovasi teknologi.",
            icon="person-badge", order=0, is_active=True,
        )

    manager = OrganizationRole.objects.filter(title__iexact="Manajer Operasional").order_by("id").first()
    if not manager:
        manager = OrganizationRole.objects.create(
            title="Manajer Operasional",
            description="Bertanggung jawab atas perencanaan, pengawasan, dan evaluasi operasional tambak.",
            icon="gear", order=1, is_active=True, parent=founder,
        )
    else:
        manager.parent = founder
        manager.icon = "gear"
        manager.is_active = True
        manager.order = 1
        manager.save(update_fields=["parent", "icon", "is_active", "order"])

    technician = OrganizationRole.objects.filter(title__iexact="Teknisi").order_by("id").first()
    if not technician:
        technician = OrganizationRole.objects.create(
            title="Teknisi",
            description="Melakukan pemeliharaan peralatan, monitoring kualitas air, dan dukungan teknis.",
            icon="wrench-adjustable", order=2, is_active=True, parent=founder,
        )
    else:
        technician.parent = founder
        technician.icon = "wrench-adjustable"
        technician.is_active = True
        technician.order = 2
        technician.save(update_fields=["parent", "icon", "is_active", "order"])

    team = OrganizationRole.objects.filter(title__iexact="Tim Operasional").order_by("id").first()
    if not team:
        team = OrganizationRole.objects.create(
            title="Tim Operasional",
            description="Melaksanakan kegiatan harian tambak secara konsisten untuk produktivitas optimal.",
            icon="people", order=3, is_active=True, parent=manager,
        )
    else:
        team.parent = manager
        team.icon = "people"
        team.is_active = True
        team.order = 3
        team.save(update_fields=["parent", "icon", "is_active", "order"])


def reverse_content(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("landing", "0003_update_landing_content")]
    operations = [migrations.RunPython(fix_content, reverse_content)]
