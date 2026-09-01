#!/usr/bin/env python3
"""Сборка самодостаточных лендингов: подставляет картинки base64 в шаблоны → dist/."""
import base64, os, pathlib
ROOT = pathlib.Path(__file__).parent
def uri(p):
    return 'data:image/jpeg;base64,' + base64.b64encode((ROOT/'assets'/p).read_bytes()).decode()
H, M = uri('hero.jpg'), uri('massing.jpg')
for src, dst in [('index.template.html','index.html'), ('classic.template.html','classic.html'), ('developers.template.html','developers.html')]:
    tpl = (ROOT/'src'/src).read_text(encoding='utf-8')
    out = tpl.replace('{{HERO_URI}}', H).replace('{{MASS_URI}}', M)
    assert '{{' not in out, src
    (ROOT/'dist'/dst).write_text(out, encoding='utf-8')
    print(dst, os.path.getsize(ROOT/'dist'/dst), 'bytes')
