"""Generate the public CV. Requires reportlab; run from the repository root."""
from pathlib import Path
from shutil import copyfile
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/Curriculo_Randy_Gomes.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=colors.HexColor('#153f38'), spaceAfter=4),
    'subtitle': ParagraphStyle('subtitle', fontName='Helvetica-Bold', fontSize=10, leading=14, spaceAfter=5),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=12, spaceAfter=4),
    'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=colors.HexColor('#153f38'), spaceBefore=9, spaceAfter=5),
    'item': ParagraphStyle('item', fontName='Helvetica-Bold', fontSize=9, leading=12, spaceBefore=3, spaceAfter=3),
}
story = []
def p(text, style='body'):
    story.append(Paragraph(text, styles[style]))

p('Randy Gomes Cavalcante', 'name')
p('DESENVOLVEDOR FULL STACK | Angular · React · NestJS · Spring Boot', 'subtitle')
p('Florianópolis, SC · (48) 99836-0776 · <link href="mailto:contato@innker.com.br">contato@innker.com.br</link>')
p('<link href="https://randygomes.dev.br">randygomes.dev.br</link> · <link href="https://linkedin.com/in/randygomesdev">linkedin.com/in/randygomesdev</link> · <link href="https://github.com/randygomesdev">github.com/randygomesdev</link>')
p('RESUMO PROFISSIONAL', 'section')
p('Estudante de Engenharia de Software com atuação em desenvolvimento Full Stack, de interfaces responsivas a APIs e microsserviços. Desenvolvo produtos com Angular, React, NestJS e Spring Boot, incluindo o Setoriza, SaaS em produção com clientes de assinatura recorrente. Mais de 10 anos de experiência em gestão e administração de negócios, com visão de produto, análise de processos e resolução de problemas.')
p('STACK TÉCNICA', 'section')
p('<b>Frontend:</b> Angular 21, React 19, TypeScript, JavaScript, RxJS, Vite, HTML, CSS, Tailwind CSS e daisyUI.<br/><b>Backend e dados:</b> Node.js, NestJS, Java, Spring Boot, APIs REST, WebSocket, microsserviços, PostgreSQL, MySQL, Redis e RabbitMQ.<br/><b>Entrega e qualidade:</b> Git, GitHub, Docker, Docker Compose, GitHub Actions, CI/CD, Vercel, Postman, Vitest e Playwright.')
p('PROJETOS', 'section')
p('Setoriza | SaaS de gestão de operações e atendimento via WhatsApp', 'item')
p('Produto Full Stack em produção, com assinaturas recorrentes e código atual privado. Centraliza atendimento, setores e automações. Evolução da versão inicial em Java e React para Angular 21 e NestJS, com PostgreSQL, RabbitMQ e Docker. <link href="https://setoriza.online">setoriza.online</link>')
p('Easypet | Plataforma de cuidados pet', 'item')
p('Projeto de estudo com React 19, Vite, Tailwind CSS e microsserviços em Java 21 / Spring Boot. Conecta tutores e parceiros com agendamento, prontuários e gestão dos estabelecimentos. PostgreSQL, Redis e Docker na infraestrutura. Demonstração: <link href="https://www.innker.com.br/easypet">innker.com.br/easypet</link>')
p('Innker Tecnologia | Site institucional', 'item')
p('Desenvolvimento do site com Angular 21, TypeScript e Tailwind CSS, publicado na Vercel. Apresentação de serviços e produtos, demonstração do Easypet e manual de identidade visual, com interface responsiva e carregamento de rotas sob demanda. <link href="https://www.innker.com.br">innker.com.br</link>')
p('EXPERIÊNCIA PROFISSIONAL', 'section')
p('Juiz de Fora - Segurança | Auxiliar Administrativo | Mar. 2023 - Mai. 2026', 'item')
p('Florianópolis, SC. Identificação de gargalos no fluxo logístico de mais de 230 funcionários entre aeroportos e matriz. Estruturação das regras de negócio e orquestração, com apoio de IA, de uma solução para leitura de relatórios de ponto e notificações de pendências via WhatsApp, reduzindo trabalho manual.')
p('Isso é Massa Delivery | Cofundador e Gestor de Operações | Jul. 2018 - Fev. 2023', 'item')
p('Florianópolis, SC. Gestão do negócio e liderança de equipe, com foco na experiência do cliente e decisões orientadas por dados operacionais. Vivência empreendedora aplicada ao entendimento das necessidades dos usuários de software.')
p('FORMAÇÃO E CURSOS', 'section')
p('Bacharelado em Engenharia de Software - UNIASSELVI (conclusão prevista: 2029)<br/>Formação Back-End Java - Programa ONE (Oracle / Alura)<br/>Técnico em Tecnologia da Informação - SENAI/SC<br/>Graduação em Administração - Faculdade IES<br/><b>Inglês:</b> técnico, com leitura de documentação de software.')
SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=38, leftMargin=38, topMargin=32, bottomMargin=30, title='Randy Gomes Cavalcante - Currículo', author='Randy Gomes Cavalcante').build(story)
copyfile(OUT, ROOT / 'public/cv.pdf')
print(OUT)
