#!/usr/bin/env python3
"""
Agent Generator Script for Claude Builder

Generates high-quality agent files when needed agents don't exist.
Uses quality templates as guidance for structure and content.
"""

import json
import re
from pathlib import Path
from typing import Dict, List

class AgentGenerator:
    """Generates agents based on quality templates and requirements."""
    
    def __init__(self, agents_dir: Path, quality_templates: List[str]):
        self.agents_dir = agents_dir
        self.quality_templates = quality_templates
        
    def generate_agent(self, agent_name: str, domain: str, requirements: Dict) -> Path:
        """Generate a new agent based on requirements and quality templates."""
        print(f"🤖 Generating agent: {agent_name}")
        
        # Find best quality template for the domain
        template_agent = self.find_best_template(domain)
        
        # Generate agent content
        agent_content = self.create_agent_content(
            agent_name, domain, requirements, template_agent
        )
        
        # Save agent file
        agent_file = self.agents_dir / f"{agent_name}.md"
        agent_file.write_text(agent_content, encoding='utf-8')
        
        print(f"  ✅ Generated: {agent_file}")
        return agent_file
    
    def find_best_template(self, domain: str) -> str:
        """Find the best quality template for the domain."""
        domain_mappings = {
            "python": "python-pro",
            "rust": "rust-engineer", 
            "typescript": "typescript-pro",
            "backend": "backend-architect",
            "frontend": "frontend-developer",
            "data": "data-scientist",
            "devops": "devops-engineer"
        }
        
        return domain_mappings.get(domain.lower(), "python-pro")
    
    def create_agent_content(self, name: str, domain: str, requirements: Dict, template: str) -> str:
        """Create agent content based on template and requirements."""
        # Load template content
        template_file = self.agents_dir / f"{template}.md"
        if template_file.exists():
            template_content = template_file.read_text(encoding='utf-8')
            
            # Adapt template to new agent
            adapted_content = self.adapt_template(
                template_content, name, domain, requirements
            )
            return adapted_content
        
        # Fallback to basic structure
        return self.create_basic_agent(name, domain, requirements)
    
    def adapt_template(self, template: str, name: str, domain: str, requirements: Dict) -> str:
        """Adapt template content to new agent requirements."""
        # Replace template-specific references with new agent info
        adaptations = {
            r'name: [^\n]+': f'name: {name}',
            r'description: [^\n]+': f'description: {requirements.get("description", f"Expert {domain} specialist")}',
            template.split("---")[1].split("---")[0].strip().split("\n")[0]: domain.title()
        }
        
        adapted = template
        for pattern, replacement in adaptations.items():
            adapted = re.sub(pattern, replacement, adapted)
        
        return adapted
    
    def create_basic_agent(self, name: str, domain: str, requirements: Dict) -> str:
        """Create basic agent structure when no template available."""
        return f"""---
name: {name}
description: {requirements.get('description', f'Expert {domain} specialist')}
tools: {', '.join(requirements.get('tools', ['Read', 'Write', 'MultiEdit', 'Bash']))}
color: blue
---

You are a senior {domain} specialist with expertise in {domain} development and best practices.

When invoked:
1. Query context manager for existing {domain} patterns and requirements
2. Review project structure and configuration
3. Analyze current implementation and standards
4. Implement solutions following best practices

{domain.title()} development checklist:
- Follow established patterns and conventions
- Ensure quality and performance standards
- Implement comprehensive error handling
- Write maintainable and testable code

Always prioritize code quality and best practices while delivering reliable solutions.
"""

if __name__ == "__main__":
    # Example usage
    agents_dir = Path("agents")
    quality_templates = ["python-pro", "rust-engineer", "typescript-pro"]
    
    generator = AgentGenerator(agents_dir, quality_templates)
    
    # Generate example agent
    requirements = {
        "description": "Expert Go developer specializing in microservices",
        "tools": ["Read", "Write", "MultiEdit", "Bash", "go", "docker"]
    }
    
    generator.generate_agent("golang-microservices-pro", "golang", requirements)
