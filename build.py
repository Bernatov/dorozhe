#!/usr/bin/env python3
"""Сборка самодостаточных лендингов: подставляет картинки base64 в шаблоны → dist/.

Ключ Web3Forms берётся из файла .web3forms_key (одна строка) рядом с build.py.
Если файла нет — в шаблоне остаётся плейсхолдер, и форма падает обратно на
mailto (сайт не ломается). Файл .web3forms_key НЕ коммитить (в .gitignore)."""
import base64, os, pathlib
ROOT = pathlib.Path(__file__).parent
def uri(p):
    return 'data:image/jpeg;base64,' + base64.b64encode((ROOT/'assets'/p).read_bytes()).decode()
H, M = uri('hero.jpg'), uri('massing.jpg')

key_file = ROOT/'.web3forms_key'
WEB3FORMS_KEY = key_file.read_text(encoding='utf-8').strip() if key_file.exists() else '{{WEB3FORMS_KEY}}'
if WEB3FORMS_KEY == '{{WEB3FORMS_KEY}}':
    print('ВНИМАНИЕ: .web3forms_key не найден — форма работает через mailto. '
          'Создай файл .web3forms_key с ключом Web3Forms и пересобери.')

for src, dst in [('index.template.html','index.html'), ('classic.template.html','classic.html'), ('developers.template.html','developers.html')]:
    tpl = (ROOT/'src'/src).read_text(encoding='utf-8')
    out = (tpl.replace('{{HERO_URI}}', H).replace('{{MASS_URI}}', M)
              .replace('{{WEB3FORMS_KEY}}', WEB3FORMS_KEY))
    assert '{{' not in out.replace('{{WEB3FORMS_KEY}}', ''), src
    (ROOT/'dist'/dst).write_text(out, encoding='utf-8')
    print(dst, os.path.getsize(ROOT/'dist'/dst), 'bytes')
