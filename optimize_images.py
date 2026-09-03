from pathlib import Path
from PIL import Image

MEDIA = Path("media")
OUTPUT = MEDIA / "optimized"

OUTPUT.mkdir(parents=True, exist_ok=True)

extensions = {".jpg", ".jpeg", ".png"}

for source in MEDIA.rglob("*"):
    if not source.is_file():
        continue

    if source.suffix.lower() not in extensions:
        continue

    # Jangan proses folder optimized
    if "optimized" in source.parts:
        continue

    try:
        with Image.open(source) as img:
            img = img.convert("RGB")

            # Maksimal 1600px pada sisi terpanjang
            img.thumbnail((1600, 1600), Image.Resampling.LANCZOS)

            # Pertahankan struktur folder
            relative = source.relative_to(MEDIA)
            output = OUTPUT / relative.with_suffix(".webp")

            output.parent.mkdir(parents=True, exist_ok=True)

            img.save(
                output,
                "WEBP",
                quality=80,
                method=6
            )

            print(
                f"{source} -> {output} "
                f"({output.stat().st_size / 1024:.0f} KB)"
            )

    except Exception as e:
        print(f"GAGAL: {source} -> {e}")
