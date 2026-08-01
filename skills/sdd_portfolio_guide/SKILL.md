---
name: sdd-portfolio-guide
description: Guia de desenvolvimento baseado em especificações (SDD) para o portfólio dinâmico do Randy Gomes.
---

# 📚 Guia de Desenvolvimento: Portfólio CMS Monolito Modular

Este guia define as regras arquiteturais, padrões de código e fluxos de trabalho que o Antigravity e seus subagentes devem seguir estritamente ao trabalhar neste projeto.

---

## ☕ 1. Padrões de Código Backend (Spring Boot & Java 21)

### 📁 Estrutura de Pacotes (Monolito Modular)
O backend deve ser dividido em módulos funcionais limpos sob `dev.randygomes.portfolio`:

```text
dev.randygomes.portfolio
├── core/             # Configurações transversais (Segurança, JWT, Handlers globais)
├── auth/             # Autenticação de Admin, Login e Token JWT
├── project/          # Módulo de Projetos (CRUD, Entidades, Repositórios)
├── skill/            # Módulo de Stacks/Habilidades (Categorias e Itens)
└── section/          # Módulo de Seções Customizadas (CRUD de páginas extras)
```

Cada módulo funcional deve conter suas próprias classes de:
* **Controller** (`*Controller.java`): Responsável pelas rotas REST e validações de input.
* **Service** (`*Service.java` e/ou `*ServiceImpl.java`): Regras de negócio.
* **Repository** (`*Repository.java`): Persistência usando Spring Data JPA.
* **Entity** (`*Entity.java` ou `*.java` anotado com `@Entity`): Mapeamento de tabelas.
* **DTO** (`*DTO.java` ou `*Request.java` / `*Response.java`): Objetos de transferência de dados.

### 🔐 Segurança & JWT
* Todas as rotas sob `/api/admin/**` devem exigir autenticação JWT ativa (`Bearer token`).
* As rotas públicas (`/api/projects`, `/api/skills`, `/api/sections`) devem ser liberadas.
* Senhas de administrador devem ser criptografadas usando `BCryptPasswordEncoder`.

---

## 🅰️ 2. Padrões de Código Frontend (Angular 21)

### 🌐 Consumo de APIs
* Todo o consumo de dados mockados deve ser substituído por chamadas HTTP reais (`HttpClient`) para o backend `/api/*`.
* Os dados carregados devem ser encapsulados em **Signals** do Angular para manter a reatividade da interface.
* Use **Interceptors** para interceptar requisições para `/api/admin/*` e injetar o token JWT automaticamente caso o administrador esteja logado.

---

## 📑 3. Regra de SDD (Spec Driven Development)
* **Contrato em Primeiro Lugar**: Qualquer modificação nos campos de retorno, novos atributos de projetos, seções ou rotas deve ser primeiramente atualizada e validada no arquivo [specs/openapi.yaml](file:///C:/Projects/portfolio/specs/openapi.yaml).
* **Consistência de Modelos**: Os modelos do TypeScript (`models/portfolio.model.ts`) e os DTOs do Java devem refletir com precisão absoluta as definições contidas na especificação OpenAPI.
