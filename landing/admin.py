from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings, AboutSection, SectionSettings, Feature, Mission, PondStat,
    CompanyValue, OrganizationRole, Facility, GalleryImage,
)

admin.site.site_header = "Admin Udang Emas Nusantara"
admin.site.site_title = "UEN Admin"
admin.site.index_title = "Kelola seluruh konten dan gambar website"


class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False


def preview(image):
    if image:
        return format_html('<img src="{}" style="width:110px;height:72px;object-fit:cover;border-radius:10px;border:1px solid #ddd" />', image.url)
    return "—"


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonAdmin):
    fieldsets = (
        ("Identitas & branding", {"fields": ("company_name", "tagline", "logo", "favicon", "primary_color", "secondary_color", "accent_color")}),
        ("Hero / bagian paling atas", {"fields": ("hero_image", "hero_badge", "hero_title_line_1", "hero_title_highlight", "hero_description", "primary_button_text", "primary_button_url", "secondary_button_text", "secondary_button_url")}),
        ("Kontak & media sosial", {"fields": ("whatsapp_number", "email", "address", "instagram_url", "youtube_url", "tiktok_url")}),
        ("CTA & SEO", {"fields": ("footer_title", "footer_text", "meta_description")}),
    )


@admin.register(AboutSection)
class AboutSectionAdmin(SingletonAdmin):
    fieldsets = (("Tentang Kami", {"fields": ("label", "title", "body", "image", "video_url")}), ("Visi", {"fields": ("vision",)}))


@admin.register(SectionSettings)
class SectionSettingsAdmin(SingletonAdmin):
    pass


class OrderedAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("order",)


@admin.register(Feature)
class FeatureAdmin(OrderedAdmin): pass
@admin.register(Mission)
class MissionAdmin(OrderedAdmin): pass
@admin.register(PondStat)
class PondStatAdmin(OrderedAdmin):
    list_display = ("title", "value", "order", "is_active")
@admin.register(CompanyValue)
class CompanyValueAdmin(OrderedAdmin): pass


@admin.register(OrganizationRole)
class OrganizationRoleAdmin(OrderedAdmin):
    list_display = ("title", "person_name", "parent", "photo_preview", "order", "is_active")
    list_editable = ("order", "is_active")
    autocomplete_fields = ("parent",)
    def photo_preview(self, obj): return preview(obj.photo)
    photo_preview.short_description = "Foto"


@admin.register(Facility)
class FacilityAdmin(OrderedAdmin):
    list_display = ("title", "image_preview", "order", "is_active")
    list_editable = ("order", "is_active")
    def image_preview(self, obj): return preview(obj.image)
    image_preview.short_description = "Gambar"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "caption")
    ordering = ("order",)
    def image_preview(self, obj): return preview(obj.image)
    image_preview.short_description = "Pratinjau"
