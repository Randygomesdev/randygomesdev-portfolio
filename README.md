# 💼 Randy Gomes | Portfolio

Este é o repositório do meu portfólio profissional, desenvolvido para apresentar minhas habilidades, projetos e trajetória como Engenheiro de Software.

🔗 **Acesse o site oficial:** [randygomes.dev.br](https://randygomes.dev.br)

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as tecnologias mais modernas do ecossistema web:

* **Framework:** [Angular 21](https://angular.dev/) (Componentes Standalone, Deferrable Views para otimização de performance)
* **Estilização:** [Tailwind CSS v4](https://tailwindcss.com/) (Design Responsivo, Variáveis de Tema Nativas, PostCSS)
* **Ícones:** [Lucide Angular](https://lucide.dev/guide/angular) & SVGs Customizados
* **Linguagem:** [TypeScript](https://www.typescriptlang.org/)
* **CI/CD:** [GitHub Actions](https://github.com/features/actions) (Integração e entrega contínuas automatizadas)
* **Hospedagem:** [Vercel](https://vercel.com/)

---

## 🚀 Recursos do Portfólio

* **Design Premium & Responsivo:** Layout adaptável e otimizado para celulares, tablets e computadores, com foco em estética minimalista e dark mode.
* **Componentes Dinâmicos & Micro-Animações:** 
  * Card de código com efeito hover de alinhamento tridimensional.
  * Âncoras inteligentes de navegação com rolagem suave (`scroll-behavior: smooth`).
  * Links internos dinâmicos direcionando citações de texto direto para a seção de projetos.
  * Botões de ação integrados com efeitos hover e sombras brilhantes.
* **Integração de Downloads:** Botão dedicado e configurado para download automático de currículo em PDF.
* **Otimização de Performance:** Uso de `@defer` (Defferable Views) do Angular para carregamento tardio de componentes pesados à medida que entram na tela.
* **Pipeline de Deploy Automatizado:** Fluxo de CI/CD que testa o build da aplicação no GitHub Actions a cada PR e publica automaticamente na Vercel ao mesclar na `main`.

---

## 💻 Como Executar Localmente

### Pré-requisitos
Certifique-se de ter o **Node.js** instalado (versão recomendada: >= 20.x).

1. Clone o repositório:
   ```bash
   git clone https://github.com/Randygomesdev/randygomesdev-portfolio.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd randygomesdev-portfolio
   ```
3. Instale as dependências:
   ```bash
   npm install
   ```
4. Inicie o servidor de desenvolvimento:
   ```bash
   npm run start
   ```
5. Open browser at [http://localhost:4200](http://localhost:4200).

---

## ⚙️ Estrutura de CI/CD

A pipeline está dividida em duas etapas principais no arquivo `.github/workflows/ci-cd.yml`:

1. **CI (Integração Contínua):** Roda em qualquer push ou Pull Request para verificar a integridade da compilação da aplicação (`npm run build`).
2. **CD (Entrega Contínua):** Roda exclusivamente em pushes para a branch principal, gerando o build produtivo e enviando as alterações diretamente para a Vercel de forma automática usando tokens de acesso seguros.
