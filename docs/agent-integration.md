# Agent Integration Guide

## Overview

This guide explains how to integrate Claude Builder agents into your development workflow.

## Agent Types

### Core Development Agents
- **backend-architect**: API design and backend systems
- **frontend-developer**: UI implementation and user experience
- **fullstack-developer**: Complete application development

### Specialized Agents
- **data-scientist**: Data analysis and machine learning
- **devops-engineer**: Infrastructure and deployment
- **security-auditor**: Security analysis and compliance

## Integration Patterns

### Sequential Workflows
```
backend-architect → frontend-developer → test-writer-fixer → devops-automator
```

### Parallel Development
```
backend-architect + frontend-developer → integration-specialist → deployment
```

### Quality Assurance Chain
```
Any Agent → test-writer-fixer → security-auditor → performance-benchmarker
```

## Natural Language Triggers

### Development
- "build api" → backend-architect + api-designer
- "create frontend" → frontend-developer + ui-designer
- "implement feature" → appropriate specialist agents

### Quality & Testing
- "add tests" → test-writer-fixer
- "security audit" → security-auditor
- "optimize performance" → performance-benchmarker

### Deployment
- "deploy application" → devops-automator
- "setup infrastructure" → infrastructure-engineer
- "configure monitoring" → sre-engineer