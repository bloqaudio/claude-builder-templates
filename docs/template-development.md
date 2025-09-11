# Template Development Guide

## Creating Templates

### Template Structure
```
template-name/
├── CLAUDE.md              # Project documentation
├── AGENTS.md               # Agent configuration
├── coordination/           # Workflow patterns
├── triggers/              # Natural language triggers
└── metadata.json          # Template metadata
```

### Metadata Format
```json
{
  "name": "template-name",
  "version": "1.0.0",
  "description": "Template description",
  "languages": ["python", "javascript"],
  "frameworks": ["fastapi", "react"],
  "complexity": "moderate",
  "agents": ["backend-architect", "frontend-developer"],
  "domains": ["backend", "frontend"]
}
```

### Quality Requirements
- Complete agent team definition
- Natural language triggers
- Coordination patterns
- Comprehensive documentation
- Working examples

## Best Practices

### Agent Selection
- Choose agents that complement each other
- Include both specialists and generalists
- Consider the full development lifecycle

### Coordination Patterns
- Define clear handoff points
- Specify context transfer requirements
- Include validation criteria

### Natural Language Triggers
- Use intuitive, conversational phrases
- Cover common development tasks
- Avoid ambiguous terms