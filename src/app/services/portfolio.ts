import { Injectable, signal } from '@angular/core';
import { Project, Skill } from '../models/portfolio.model';

@Injectable({
  providedIn: 'root',
})
export class PortfolioService {

  readonly projects = signal<Project[]>([
    {
      id: '1',
      title: 'EasyPet',
      description: 'Plataforma que conecta tutores a clínicas e pet shops. Os tutores podem agendar serviços online e acompanhar os registros de saúde dos pets, enquanto os estabelecimentos gerenciam horários, profissionais e atendimentos.',
      tags: ['React 19', 'Vite', 'Tailwind CSS', 'Java 21', 'Spring Boot', 'PostgreSQL', 'Docker'],
      githubUrl: 'https://github.com/Randygomesdev/Easypet',
      liveUrl: 'https://easypet.innker.com.br/',
      featured: true
    },
    {
      id: '2',
      title: 'Setoriza',
      description: 'SaaS em produção, com clientes de assinatura recorrente. Equipes atendem pelo WhatsApp em uma caixa de entrada compartilhada, encaminham conversas para o setor responsável e automatizam a triagem e outras etapas do atendimento.',
      tags: ['Angular 21', 'TypeScript', 'NestJS', 'Node.js', 'PostgreSQL', 'RabbitMQ', 'Docker'],
      liveUrl: 'https://setoriza.online',
      featured: true
    },
    {
      id: '3',
      title: 'Innker Tecnologia',
      description: 'Site institucional da software house Innker, onde visitantes podem conhecer os serviços, explorar os produtos e entrar em contato. O projeto também inclui uma demonstração navegável do Easypet e um guia digital de identidade visual com exemplos de cores, tipografia e componentes.',
      tags: ['Angular 21', 'TypeScript', 'Tailwind CSS', 'RxJS', 'Vercel'],
      liveUrl: 'https://www.innker.com.br',
      featured: true
    }
  ])

  readonly skills = signal<Skill[]>([
    {
      category: 'Frontend & UI',
      items: ['Angular 21', 'React 19 / Vite', 'TypeScript / JavaScript', 'Tailwind CSS / daisyUI', 'RxJS', 'HTML5 / CSS3']
    },
    {
      category: 'Backend & APIs',
      items: ['Node.js / NestJS', 'Java / Spring Boot', 'APIs REST / WebSocket', 'Microsserviços', 'PostgreSQL / MySQL', 'Redis / RabbitMQ']
    },
    {
      category: 'DevOps & Ferramentas',
      items: ['Git / GitHub', 'Docker / Docker Compose', 'GitHub Actions / CI/CD', 'Vercel', 'Vitest / Playwright', 'Postman']
    }
  ])
}
