#!/bin/bash

# 🌈 Цвета и эмоджи для красивого вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color
CHECK="✅"
ROCKET="🚀"
GEAR="⚙️"
HOURGLASS="⏳"
FOLDER="📂"
PACKAGE="📦"
DOCKER="🐳"
ERROR="❌"

# 🔍 Проверка прав администратора
# if [ "$(id -u)" -ne 0 ]; then
#   echo -e "${RED}${ERROR} Этот скрипт должен быть запущен с правами root или через sudo${NC}"
#   exit 1
# fi

echo -e "${BLUE}${ROCKET} Начинаем установку приложения! ${NC}"

# 🔄 Обновление пакетов и установка зависимостей
echo -e "${YELLOW}${HOURGLASS} Установка зависимостей... ${NC}"
uv add -r req.txt
echo -e "${GREEN}${CHECK} Зависимости успешно установлены! ${NC}"

# env

cat > .env <<EOF
DB_NAME=postgres
DB_USER=admin
DB_PASS=root
DB_PORT=5432
DB_HOST=127.0.0.1

RABBIT_USER=adminadmin
RABBIT_PASS=root
RABBIT_PORT=5672
RABBIT_HOST=127.0.0.1

REDIS_PORT=6379
REDIS_HOST=localhost
REDIS_DB=0

JWT_SECRET=mHK3zl/hZeSY6LyL
JWT_ALGORITHM=HS256

SESSION_SECRET=vNjv3JqYHPs3+VwD

API_HOST=0.0.0.0
API_PORT=8000
EOF

echo "${CHECK} Создан .env файл"

# 🐳 Запуск Docker Compose
echo -e "${BLUE}${DOCKER} Запуск docker-compose... ${NC}"
docker compose up -d --build
echo -e "${GREEN}${CHECK} Docker-контейнеры успешно запущены! ${NC}"

# 🎉 Завершение установки
echo -e "${GREEN}${ROCKET} Установка завершена успешно! ${NC}"
echo -e "${BLUE}Ваше приложение должно быть доступно. Приятного использования! ${NC}"
