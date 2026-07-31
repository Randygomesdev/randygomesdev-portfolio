export interface Project {
    id: string;
    title: string;
    description: string;
    longDescription?: string;
    tags: string[];
    githubUrl?: string;
    liveUrl?: string;
    featured: boolean;
}

export interface Skill {
    category: string;
    items: string[]
}