"""Generate the public CV. Requires reportlab; run from the repository root."""
from pathlib import Path
from shutil import copyfile
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/Curriculo_Randy_Gomes_dev.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=colors.HexColor('#153f38'), spaceAfter=4),
    'subtitle': ParagraphStyle('subtitle', fontName='Helvetica-Bold', fontSize=10, leading=14, spaceAfter=5),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10, leading=13.5, spaceAfter=5),
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
p('Sou desenvolvedor Full Stack e estudante de Engenharia de Software. Mais de dez anos em gestão de operações me ensinaram a observar como as equipes trabalham e identificar tarefas que podem ser automatizadas. Aplico essa experiência no Setoriza, que evoluiu de projeto de portfólio para um SaaS em produção com clientes recorrentes, e no Easypet, que cresceu para reunir agendamento, prontuários e gestão de parceiros.')
p('STACK TÉCNICA', 'section')
p('<b>Frontend:</b> Angular 21, React 19, TypeScript, JavaScript, RxJS, Vite, HTML, CSS, Tailwind CSS e daisyUI.<br/><b>Backend e dados:</b> Node.js, NestJS, Java, Spring Boot, APIs REST, WebSocket, microsserviços, PostgreSQL, MySQL, Redis e RabbitMQ.<br/><b>Entrega e qualidade:</b> Git, GitHub, Docker, Docker Compose, GitHub Actions, CI/CD, Vercel, Postman, Vitest e Playwright.')
p('PROJETOS INDEPENDENTES', 'section')
p('Setoriza | SaaS de gestão de operações e atendimento via WhatsApp', 'item')
p('Evoluí o Setoriza de um projeto de portfólio em Java e React para um SaaS em produção com Angular 21 e NestJS, usado por clientes de assinatura recorrente. Atuo em recursos como caixa de entrada compartilhada, distribuição de conversas por setor e triagem automatizada, conciliando novas entregas com a estabilidade do atendimento. <link href="https://setoriza.online">setoriza.online</link>')
p('Easypet | Plataforma de cuidados pet', 'item')
p('Desenvolvo fluxos de agendamento online e acompanhamento da saúde dos pets para tutores e um painel para clínicas e pet shops gerenciarem horários, profissionais e atendimentos. A aplicação usa React 19, Vite e APIs em Java 21 com Spring Boot. <link href="https://easypet.innker.com.br/">easypet.innker.com.br</link>')
p('Innker | Site de apresentação dos projetos', 'item')
p('Desenvolvi um <link href="https://www.innker.com.br">site em Angular e Tailwind CSS</link> para apresentar Setoriza e Easypet, com uma demonstração navegável do Easypet e um guia digital de identidade visual.')
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
