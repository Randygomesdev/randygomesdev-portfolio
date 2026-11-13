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
      description: 'Plataforma de cuidados pet que conecta tutores a clínicas, petshops e outros parceiros. Reúne agendamento online, prontuário dos pets e gestão dos estabelecimentos, com uma demonstração pública navegável.',
      tags: ['React 19', 'Vite', 'Tailwind CSS', 'Java 21', 'Spring Boot', 'PostgreSQL', 'Docker'],
      githubUrl: 'https://github.com/Randygomesdev/Easypet',
      liveUrl: 'https://www.innker.com.br/easypet',
      featured: true
    },
    {
      id: '2',
      title: 'Setoriza',
      description: 'SaaS em produção para gestão de operações e atendimento integrado ao WhatsApp, com clientes de assinatura recorrente. Centraliza conversas, setores e automações em uma arquitetura de microsserviços. A versão atual utiliza Angular e NestJS.',
      tags: ['Angular 21', 'TypeScript', 'NestJS', 'Node.js', 'PostgreSQL', 'RabbitMQ', 'Docker'],
      liveUrl: 'https://setoriza.online',
      featured: true
    },
    {
      id: '3',
      title: 'Innker Tecnologia',
      description: 'Site institucional da Innker, com apresentação de serviços e produtos, demonstração do Easypet e manual de identidade visual. Interface responsiva com rotas carregadas sob demanda e identidade visual consistente.',
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
