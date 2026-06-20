# 📊 Questionário TI – Pesquisa Interdisciplinar em Computação

Aplicação web desenvolvida com **Django + Docker** para coleta e análise de dados sobre profissões, competências e percepções na área de Computação.

Projeto desenvolvido no contexto do **Projeto Interdisciplinar I** do curso de Computação.

---

## 🎯 Objetivo

Investigar profissões, competências, trajetórias e percepções relacionadas à área de Computação por meio de um questionário estruturado aplicado a três perfis distintos de participantes.

---

## 👥 Perfis de Participantes

| Perfil | Descrição |
|--------|-----------|
| 💼 **Profissional de TI** | Atua ou já atuou profissionalmente na área de tecnologia |
| 🎓 **Estudante de TI** | Cursa graduação em Computação, Sistemas, Engenharia ou área afim |
| 🌐 **Público Geral** | Não trabalha nem estuda em TI, mas usa tecnologia no cotidiano |

---

## 🗂️ Estrutura do Questionário

Cada perfil possui um formulário com **4 blocos**:

| Bloco | Tipo | Conteúdo |
|-------|------|----------|
| I – Perfil | Fechado | Faixa etária, gênero, escolaridade, localização |
| II – Mercado | Fechado | Percepção do mercado de TI |
| III – Específico | Fechado/Múltipla escolha | Varia por perfil (atuação, formação ou uso de tecnologia) |
| IV – Aberto | Aberto | Dificuldades, conselhos, percepções e expectativas |

---

## 🚀 Tecnologias Utilizadas

- **Backend:** Python 3.12 + Django 5.0
- **Banco de dados:** PostgreSQL 16
- **Frontend:** Bootstrap 5.3 + Chart.js 4.4
- **Servidor:** Gunicorn + Nginx
- **Containerização:** Docker + Docker Compose
- **Exportação:** openpyxl (Excel .xlsx)

---

## ⚙️ Como Executar

### Pré-requisitos
- Docker e Docker Compose instalados

### 1. Clone o repositório
```bash
git clone https://github.com/ernane2022/questionario-ti.git
cd questionario-ti
```

### 2. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o .env e defina uma SECRET_KEY segura
```

### 3. Suba os containers
```bash
docker compose up --build -d
```

### 4. Crie o superusuário (admin)
```bash
docker compose exec web python manage.py createsuperuser
```

### 5. Acesse a aplicação

| URL | Descrição |
|-----|-----------|
| `http://localhost:8080/` | Página inicial – escolha do perfil |
| `http://localhost:8080/formulario/profissional/` | Formulário para Profissionais |
| `http://localhost:8080/formulario/estudante/` | Formulário para Estudantes |
| `http://localhost:8080/formulario/publico/` | Formulário para Público Geral |
| `http://localhost:8080/dashboard/` | Dashboard com gráficos (admin) |
| `http://localhost:8080/exportar/` | Exportar dados em Excel (admin) |
| `http://localhost:8080/admin/` | Painel administrativo Django |

---

## 📊 Dashboard Administrativo

Acessível apenas para usuários staff, o dashboard apresenta:

- **KPIs** com total de respostas por perfil
- **Abas separadas** por perfil (Geral, Profissionais, Estudantes, Público)
- **Gráficos interativos** (área de atuação, competências, motivos, frequência de uso)
- **Tabelas** com as últimas respostas de cada perfil
- **Exportação** para planilha Excel com 3 abas

---

## 📁 Estrutura do Projeto

```
questionario-ti/
├── core/                  # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pesquisa/              # App principal
│   ├── models.py          # 3 modelos (Profissional, Estudante, Público)
│   ├── forms.py           # 3 formulários específicos por perfil
│   ├── views.py           # Views (formulário, dashboard, exportação)
│   ├── admin.py           # Painel admin customizado
│   ├── export.py          # Exportação Excel
│   ├── templates/         # Templates HTML
│   └── static/            # CSS
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
└── .env.example
```

---

## 🔒 Segurança

- Dashboard e exportação protegidos por `@staff_member_required`
- Variáveis sensíveis via arquivo `.env` (não versionado)
- CSRF habilitado em todos os formulários

---

## 📄 Licença

Projeto acadêmico – Projeto Interdisciplinar I – Computação © 2026