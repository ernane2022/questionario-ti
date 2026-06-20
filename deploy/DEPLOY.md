# 🚀 Deploy – VPS Hostinger

## 1. Acesse o VPS via SSH
```bash
ssh root@IP_DO_SEU_VPS
```

## 2. Instale Docker e Docker Compose
```bash
apt update && apt upgrade -y
apt install -y docker.io docker-compose-plugin git curl

# Habilita Docker no boot
systemctl enable docker
systemctl start docker
```

## 3. Configure o subdomínio na Hostinger
No painel da Hostinger:
- Vá em **DNS / Zona DNS** do domínio `ernanecreative.com`
- Adicione um registro **A**:
  - Nome: `pesquisa`
  - Valor: `IP_DO_SEU_VPS`
  - TTL: 300

Aguarde até 10 minutos para propagar.

## 4. Clone o repositório no VPS
```bash
cd /var/www
git clone https://github.com/ernane2022/questionario-ti.git
cd questionario-ti
```

## 5. Configure o ambiente de produção
```bash
cp .env.production .env
nano .env
```

Preencha:
- `SECRET_KEY` → gere com `python3 -c "import secrets; print(secrets.token_urlsafe(50))"`
- `DB_PASSWORD` → senha forte e aleatória

## 6. Instale o Certbot (SSL gratuito)
```bash
apt install -y certbot

# Para o Nginx temporariamente se estiver rodando
docker compose down

# Gera o certificado
certbot certonly --standalone -d pesquisa.ernanecreative.com
```

## 7. Substitua o nginx.conf pelo de produção
```bash
cp nginx.conf nginx.conf.local
cp nginx.conf.production nginx.conf
```

## 8. Atualize o docker-compose.yml para montar o certificado
Adicione o volume do certbot no serviço nginx:
```yaml
nginx:
  volumes:
    - static_volume:/app/staticfiles
    - ./nginx.conf:/etc/nginx/conf.d/default.conf
    - /etc/letsencrypt:/etc/letsencrypt:ro
  ports:
    - "80:80"
    - "443:443"
```

## 9. Suba os containers
```bash
docker compose up --build -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py collectstatic --noinput
docker compose exec web python manage.py createsuperuser
```

## 10. Teste o acesso
Acesse `https://pesquisa.ernanecreative.com` no navegador.

## 11. Renovação automática do SSL
```bash
crontab -e
# Adicione:
0 3 * * * certbot renew --quiet && docker compose -f /var/www/questionario-ti/docker-compose.yml restart nginx
```

## 12. Deploy de atualizações futuras
```bash
cd /var/www/questionario-ti
./deploy.sh
```

---

## ✅ Checklist final
- [ ] Subdomínio apontando para o IP do VPS
- [ ] Certificado SSL gerado
- [ ] `.env` com `DEBUG=False` e `SECRET_KEY` forte
- [ ] Superusuário criado
- [ ] Backup automático configurado
- [ ] Site acessível em `https://pesquisa.ernanecreative.com`