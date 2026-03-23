# Claude Builder Official Templates

This repository contains the official template collection for [Claude Builder](https://github.com/bloqaudio/claude_builder) - the Universal Claude Code Environment Generator.

## 🎯 Purpose

Claude Builder transforms any project into an optimized Claude Code development environment with:
- **Intelligent Agent Teams** - Project-specific agent configurations
- **Natural Language Triggers** - Conversational development workflows  
- **Coordination Patterns** - Proven agent collaboration workflows
- **Complete Environments** - Both CLAUDE.md documentation and AGENTS.md orchestration

## 📦 Available Templates

### Production-Ready Stacks

- **`python-fastapi-production`** - Enterprise FastAPI backend with comprehensive agent team
- **`react-typescript-frontend`** - Modern React TypeScript frontend with UI/UX specialists
- **`rust-axum-performance`** - High-performance Rust web services
- **`python-django-fullstack`** - Complete Django application development

### Specialized Environments

- **`devops-infrastructure`** - Infrastructure automation and deployment
- **`mlops-data-pipeline`** - ML engineering and data pipeline development
- **`mobile-app-development`** - Cross-platform mobile development
- **`microservices-architecture`** - Distributed systems and service mesh

## 🤖 Agent Orchestration

Each template includes:

### Agent Team Configuration
- **Primary Development Team** - Core specialists for the technology stack
- **Support Specialists** - Quality, testing, and deployment experts
- **Domain Experts** - Specialized knowledge for specific use cases

### Natural Language Triggers
- **Development Workflows** - "build api" → backend-architect + api-tester activation
- **Quality Assurance** - "add comprehensive tests" → test-writer-fixer coordination
- **Deployment Operations** - "deploy to production" → devops-automator workflow

### Coordination Patterns
- **Sequential Workflows** - Step-by-step agent handoffs
- **Parallel Processing** - Concurrent agent collaboration
- **Context Preservation** - Seamless knowledge transfer between agents

## 🔧 Usage with Claude Builder

```bash
# Analyze project and generate environment
claude-builder ./my-project

# Use specific template
claude-builder ./my-project --template python-fastapi-production

# Generate only agent configuration
claude-builder ./my-project --agents-only

# List available templates
claude-builder --list-templates
```

## 📋 Template Structure

Each template bundle contains:

```
template-name/
├── CLAUDE.md                 # Project documentation template
├── AGENTS.md                 # Agent orchestration configuration
├── coordination/             # Agent workflow patterns
│   ├── development.yaml
│   └── deployment.yaml
├── triggers/                 # Natural language patterns
│   └── natural-triggers.yaml
└── metadata.json            # Template information
```

## 🌟 Template Features

### Documentation Templates (CLAUDE.md)
- Project-specific development guidelines
- Framework best practices and patterns
- Architecture decisions and rationale
- Development commands and workflows

### Agent Orchestration (AGENTS.md)  
- Optimal agent team for the project type
- Natural language trigger patterns
- Agent coordination workflows
- Context-aware handoff patterns

### Coordination Patterns
- Proven agent collaboration workflows
- Technology-specific optimization patterns
- Quality assurance and testing workflows
- Deployment and operations coordination

## 🔄 Template Updates

Templates are continuously updated with:
- New agent capabilities and specializations
- Improved coordination patterns
- Enhanced natural language triggers
- Community feedback and optimizations

## 🤝 Contributing

While this is the official repository, community contributions are welcome through:
- [Community Templates Repository](https://github.com/bloqaudio/claude-builder-community)
- Feature requests and suggestions
- Agent effectiveness feedback
- Coordination pattern improvements

## 📖 Documentation

- [Claude Builder Documentation](https://github.com/bloqaudio/claude_builder#readme)
- [Agent Orchestration Guide](https://github.com/bloqaudio/claude_builder/blob/main/docs/agent-orchestration.md)
- [Template Development Guide](https://github.com/bloqaudio/claude_builder/blob/main/docs/template-development.md)

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

---

**Transform your development workflow with intelligent agent orchestration.**  
*Generated environments adapt to your project's needs and complexity.*