#!/bin/bash
# Script de deploy – Pesquisa em Computação
# Uso: ./deploy.sh

set -e

echo "🚀 Iniciando deploy..."

# Atualiza o código
git pull origin master

# Rebuild e restart
docker compose down
docker compose up --build -d

# Aguarda o banco subir
echo "⏳ Aguardando banco de dados..."
sleep 10

# Migrations e static
docker compose exec web python manage.py migrate --noinput
docker compose exec web python manage.py collectstatic --noinput

# Backup do banco
mkdir -p backups
docker compose exec db pg_dump -U $DB_USER $DB_NAME > backups/backup_$(date +%Y%m%d_%H%M%S).sql
echo "✅ Backup salvo em backups/"

echo "✅ Deploy concluído! Acesse https://pesquisa.ernanecreative.com"