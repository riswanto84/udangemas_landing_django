from django.shortcuts import render
from .models import (SiteSettings, AboutSection, SectionSettings, Feature, Mission, PondStat, CompanyValue, OrganizationRole, Facility, GalleryImage)

def home(request):
    site = SiteSettings.load()
    about = AboutSection.load()
    sections = SectionSettings.load()
    roles = OrganizationRole.objects.filter(is_active=True).select_related("parent").order_by("order", "id")

    # Ambil Founder sebagai akar. Jika data lama belum memiliki relasi parent
    # yang benar, gunakan judul sebagai fallback agar struktur tetap tampil.
    founders = list(roles.filter(parent__isnull=True))
    if not founders:
        founder = roles.filter(title__iexact="Founder").first()
        founders = [founder] if founder else []

    # Bangun struktur langsung di bawah Founder. Tim Operasional harus menjadi
    # anak Manajer Operasional, sedangkan Teknisi berada di bawah Founder.
    team_groups = []
    if founders:
        founder = founders[0]
        direct_roles = list(roles.filter(parent=founder))
        for role in direct_roles:
            team_groups.append({
                "role": role,
                "children": list(roles.filter(parent=role)),
            })

    # Fallback tampilan untuk database lama yang parent-nya belum tersinkron.
    if founders and not team_groups:
        manager = roles.filter(title__iexact="Manajer Operasional").first()
        technician = roles.filter(title__iexact="Teknisi").first()
        team = roles.filter(title__iexact="Tim Operasional").first()
        if manager:
            team_groups.append({"role": manager, "children": [team] if team else []})
        if technician:
            team_groups.append({"role": technician, "children": []})

    return render(request, "landing/home.html", {
        "site": site, "about": about, "sections": sections,
        "features": Feature.objects.filter(is_active=True),
        "missions": Mission.objects.filter(is_active=True),
        "stats": PondStat.objects.filter(is_active=True),
        "values": CompanyValue.objects.filter(is_active=True),
        "founders": founders,
        "team_groups": team_groups,
        "facilities": Facility.objects.filter(is_active=True),
        "gallery": GalleryImage.objects.filter(is_active=True),
    })
