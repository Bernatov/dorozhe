# Дороже — лендинги
Сайт: https://bernatov.github.io/dorozhe/ (тёмная версия) · [classic.html](https://bernatov.github.io/dorozhe/classic.html) (светлая).

Правки: `src/*.template.html` → `python3 build.py` → готовые файлы в `dist/`.
Публикация: скопировать `dist/index.html` и `dist/classic.html` в корень
(`cp dist/*.html .`), закоммитить и запушить в main — GitHub Pages отдаёт сайт
из корня ветки main.
