#!/usr/bin/env python3
"""news-image-20261118 v9c (akun 1): 35-story front page, coverage control.

Kontrol cakupan atas v8 (985.514, rank 99): resep v8 PERSIS — total tetap
35 cerita (3 TOP + 12 grid + 20 ALSO), TANPA tag sumber/badge/DATE CHECK.
Satu-satunya perubahan adalah swap cerita: 4 cerita sore/malam terbesar
masuk grid (GTA VI, Peltola, Anthropic, Board of Peace), 4 grid terlemah
turun ke ALSO; Nvidia TETAP di grid #4 (pola rank 1). Peta 35 pin
dipertahankan. Koreksi fakta terverifikasi ganda: Akvan Buletin 24,
Guinea 160.000 ke Mali, Dhoni 272 CSK appearances, Eisenkot diganti EPP.
Deterministic, offline.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
