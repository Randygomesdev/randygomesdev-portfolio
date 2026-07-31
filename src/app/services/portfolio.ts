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
      description: 'Plataforma Marketplace que conecta tutores de pets a uma rede completa de prestadores de serviços parceiros, como clínicas veterinárias, petshops, banho & tosa e cuidadores.',
      tags: ['React', 'Vite', 'TailwindCSS', 'Java 21', 'Spring Boot', 'Docker'],
      githubUrl: 'https://github.com/Randygomesdev/Easypet',
      liveUrl: 'https://randygomesdev.dev/easypet',
      featured: true
    },
    {
      id: '2',
      title: 'Setoriza',
      description: 'CRM Automação de atendimento & Chat Multiatendente via WhatApp. Projeto Fullstack em Java (Microserviços) e React (Vite) rodando em Docker',
      tags: ['React', 'Vite', 'TailwindCSS', 'Java 21', 'Spring Boot', 'Docker'],
      githubUrl: 'https://github.com/Randygomesdev/Setoriza',
      liveUrl: 'https://randygomesdev.dev/Setoriza',
      featured: true
    }
  ])

  readonly skills = signal<Skill[]>([
    {
      category: 'Frontend & UI',
      items: ['Angular', 'React', 'TypeScript', 'Tailwind CSS', 'RxJS', 'HTML5/CSS3']
    },
    {
      category: 'Backend & APIs',
      items: ['Java', 'Spring Boot', 'REST APIs', 'Microserviços', 'PostgreSQL']
    },
    {
      category: 'DevOps & Ferramentas',
      items: ['Git', 'Docker', 'CI/CD Pipelines']
    }
  ])
}
