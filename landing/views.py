from django.shortcuts import render
from .models import (SiteSettings, AboutSection, SectionSettings, Feature, Mission, PondStat, CompanyValue, OrganizationRole, Facility, GalleryImage)

def home(request):
    site = SiteSettings.load()
    about = AboutSection.load()
    sections = SectionSettings.load()
    roles = OrganizationRole.objects.filter(is_active=True).select_related("parent")
    return render(request, "landing/home.html", {
        "site": site, "about": about, "sections": sections,
        "features": Feature.objects.filter(is_active=True),
        "missions": Mission.objects.filter(is_active=True),
        "stats": PondStat.objects.filter(is_active=True),
        "values": CompanyValue.objects.filter(is_active=True),
        "founders": roles.filter(parent__isnull=True),
        "team_roles": roles.filter(parent__isnull=False),
        "facilities": Facility.objects.filter(is_active=True),
        "gallery": GalleryImage.objects.filter(is_active=True),
    })
