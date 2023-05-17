#!/usr/bin/env bash

mkdir -p .github/workflows
touch requirements.txt

project_name=$(basename $(pwd))

cat  > ".github/workflows/main.yml" << EOF
# .github/workflows/**main.yml**
name: ${project_name} workflow

on: [push]

jobs:
  tests:
    # «Раннер» — создание изолированного окружения с последней версией Ubuntu
    runs-on: ubuntu-latest

    steps:
    # Запуск actions checkout — готового скрипта
    # для клонирования репозитория
    - uses: actions/checkout@v2
    - name: Set up Python
      # Запуск actions setup-python — готового скрипта
      # для развёртывания окружения Python
      uses: actions/setup-python@v2
      with:
        # Выбор версии Python
        python-version: 3.9

    - name: Install dependencies
      run: |
        # обновление pip
        python -m pip install --upgrade pip
        # установка flake8 и его плагинов
        pip install flake8 pep8-naming flake8-broken-line flake8-return flake8-isort
        # установка зависимостей
        pip install -r requirements.txt

    - name: Test with flake8 and django tests
      run: |
        # запуск проверки проекта по flake8
        python -m flake8
EOF

cat > "setup.cfg" << EOF
[flake8]
ignore =
    W503,
    F811,
    R504
exclude =
    tests/,
    */migrations/,
    venv/,
    env/
per-file-ignores =
    */settings.py:E501
max-complexity = 10 
EOF

git add . && git commit -m "GitActionsScript $(\date)" && git push
