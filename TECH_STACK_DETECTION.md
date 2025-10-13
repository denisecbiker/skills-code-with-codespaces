# Tech Stack Detection Guide

This guide helps you determine if your project uses Python, .NET, React, or a combination of these technologies.

## Quick Start

To detect which technologies your project uses, run:

```bash
python detect-tech-stack.py
```

Or make it executable and run directly:

```bash
chmod +x detect-tech-stack.py
./detect-tech-stack.py
```

## What Does It Detect?

### Python Detection

The tool looks for:
- **Python files** (`.py` extension)
- **Package management files**:
  - `requirements.txt` - pip dependencies
  - `Pipfile` / `Pipfile.lock` - pipenv dependencies
  - `pyproject.toml` - modern Python packaging
  - `setup.py` - Python package setup
  - `poetry.lock` - Poetry dependencies
- **Virtual environments** (`venv`, `.venv`, `virtualenv` directories)

### .NET Detection

The tool looks for:
- **.NET project files** (`.csproj` extension)
- **Solution files** (`.sln` extension)
- **C# source files** (`.cs` extension)
- **.NET version** detection (checks for .NET 6, 7, 8, or .NET Core)

### React Detection

The tool looks for:
- **package.json** files with React dependencies
- **React component files** (`.jsx`, `.tsx` extensions)

## Understanding the Results

### Scenario 1: .NET 6 API with React Frontend (No Python)

```
Python:  ❌ NO
.NET:    ✅ YES
React:   ✅ YES

💡 Your .NET 6 API with React frontend does NOT use Python.
```

This means your application is built with:
- Backend: .NET 6 API (C#)
- Frontend: React (JavaScript/TypeScript)
- No Python components

### Scenario 2: .NET 6 API with React Frontend + Python

```
Python:  ✅ YES
.NET:    ✅ YES
React:   ✅ YES

💡 Your .NET 6 API with React frontend DOES use Python!
```

This means your application uses all three technologies. Common integration patterns:
- Python microservices alongside .NET API
- Python scripts for data processing or ML
- Python backend services called by .NET API
- Build/deployment scripts in Python

### Scenario 3: Python Only

```
Python:  ✅ YES
.NET:    ❌ NO
React:   ❌ NO

💡 This project uses Python, but doesn't appear to have .NET or React.
```

This is a Python-only project (like the current repository).

## Manual Detection Methods

If you can't run the script, here are manual ways to check:

### Check for Python

1. Look for `.py` files:
   ```bash
   find . -name "*.py" -not -path "*/\.*" | head -10
   ```

2. Look for Python package files:
   ```bash
   ls requirements.txt Pipfile pyproject.toml setup.py 2>/dev/null
   ```

### Check for .NET

1. Look for .NET project files:
   ```bash
   find . -name "*.csproj" -o -name "*.sln" | head -10
   ```

2. Check for .NET version in project files:
   ```bash
   grep -r "TargetFramework" *.csproj 2>/dev/null
   ```

### Check for React

1. Check package.json for React:
   ```bash
   cat package.json | grep -i react
   ```

2. Look for React component files:
   ```bash
   find . -name "*.jsx" -o -name "*.tsx" | head -10
   ```

## Common Integration Patterns

### Why Python Might Be in a .NET + React Project

1. **Data Science/ML**: Python scripts for machine learning models
2. **Build Tools**: Python-based build or deployment scripts
3. **Microservices**: Python microservices running alongside .NET API
4. **Data Processing**: ETL jobs or data transformation scripts
5. **Testing**: Python-based test automation or fixtures
6. **Legacy Code**: Existing Python services being migrated

### Identifying the Integration

Look at the directory structure:
- `scripts/` folder with `.py` files → Build/deployment scripts
- `ml/` or `models/` with Python → Machine learning components
- Separate Python API alongside .NET → Microservices architecture
- `tests/` with Python → Testing automation
- Python files calling .NET or vice versa → Service integration

## Example Project Structures

### .NET API + React (No Python)
```
MyProject/
├── Backend/
│   ├── API.csproj
│   └── Controllers/
├── Frontend/
│   ├── package.json
│   ├── src/
│   └── components/
└── README.md
```

### .NET API + React + Python ML
```
MyProject/
├── Backend/
│   ├── API.csproj
│   └── Controllers/
├── Frontend/
│   ├── package.json
│   └── src/
├── ml-service/
│   ├── requirements.txt
│   ├── model.py
│   └── train.py
└── README.md
```

### .NET API + React + Python Scripts
```
MyProject/
├── Backend/
│   ├── API.csproj
│   └── Controllers/
├── Frontend/
│   ├── package.json
│   └── src/
├── scripts/
│   ├── deploy.py
│   └── data_migration.py
└── README.md
```

## Troubleshooting

### Script Shows No Technologies Found

- Make sure you're running the script in the project root directory
- Check if files are in subdirectories (the script searches recursively)
- Some files might be in `.gitignore` and not present in the clone

### False Positives

- Virtual environment Python files are ignored by the script
- `node_modules` is excluded from scanning
- Hidden `.git` directories are skipped

## Next Steps

After determining your tech stack:

1. **If Python is detected**: 
   - Check `requirements.txt` or similar for dependencies
   - Look at Python files to understand their purpose
   - Check if they're standalone or integrated with .NET

2. **If no Python is detected**:
   - Your .NET + React app runs without Python
   - Python is not required for development or deployment
   - Any Python setup is optional

3. **For mixed stacks**:
   - Document the integration points
   - Ensure all technologies are set up in your development environment
   - Check if Python services need to run alongside your .NET API
