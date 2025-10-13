# Tech Stack Detection - Usage Examples

## Example 1: Current Repository (Python Only)

When you run the detection tool on this repository:

```bash
python detect-tech-stack.py
```

**Output:**
```
============================================================
TECH STACK DETECTION REPORT
============================================================

Analyzing directory: /home/runner/work/skills-code-with-codespaces/skills-code-with-codespaces

🐍 PYTHON DETECTION:
   ✅ Found 2 Python file(s)
   ℹ️  No Python package files found

⚙️  .NET DETECTION:
   ❌ No .NET project files found
   ℹ️  No C# files found

⚛️  REACT DETECTION:
   ❌ React not found in package.json
   ℹ️  No .jsx or .tsx files found

🔗 INTEGRATION ANALYSIS:
   ℹ️  This appears to be a Python-only project

============================================================
SUMMARY:
============================================================
Python:  ✅ YES
.NET:    ❌ NO
React:   ❌ NO

💡 This project uses Python, but doesn't appear to have .NET or React.
============================================================
```

**What this means:** This repository only contains Python code. There is no .NET or React.

---

## Example 2: .NET 6 API with React Frontend (No Python)

For a typical .NET + React project without Python:

**Project Structure:**
```
MyApp/
├── Backend/
│   ├── MyApp.Api.csproj
│   └── Controllers/
│       └── WeatherController.cs
├── Frontend/
│   ├── package.json (with React dependency)
│   └── src/
│       └── App.jsx
└── MyApp.sln
```

**Expected Output:**
```
Python:  ❌ NO
.NET:    ✅ YES
React:   ✅ YES

💡 Your .NET 6 API with React frontend does NOT use Python.
```

---

## Example 3: .NET 6 API with React Frontend + Python ML Service

For a full-stack app with Python integration:

**Project Structure:**
```
MyApp/
├── Backend/
│   ├── MyApp.Api.csproj
│   └── Controllers/
│       └── WeatherController.cs
├── Frontend/
│   ├── package.json (with React dependency)
│   └── src/
│       └── App.jsx
├── ml-service/
│   ├── requirements.txt
│   ├── model.py
│   └── predict.py
└── MyApp.sln
```

**Expected Output:**
```
Python:  ✅ YES
.NET:    ✅ YES
React:   ✅ YES

💡 Your .NET 6 API with React frontend DOES use Python!

🔗 INTEGRATION ANALYSIS:
   ℹ️  Full-stack with all three technologies
```

**What this means:** Your application uses Python (likely for ML/data processing), .NET for the API backend, and React for the frontend.

---

## Example 4: .NET 6 API with React + Python Build Scripts

For a project with Python scripts but not as part of the application:

**Project Structure:**
```
MyApp/
├── Backend/
│   ├── MyApp.Api.csproj
│   └── Controllers/
├── Frontend/
│   ├── package.json (with React dependency)
│   └── src/
├── scripts/
│   ├── deploy.py
│   └── setup.py
└── MyApp.sln
```

**Expected Output:**
```
Python:  ✅ YES
.NET:    ✅ YES
React:   ✅ YES

🐍 PYTHON DETECTION:
   ✅ Found 2 Python file(s)
      - /path/to/scripts/deploy.py
      - /path/to/scripts/setup.py
```

**What this means:** Python is present but only for development/deployment scripts, not as part of the runtime application.

---

## How to Interpret Results

### Question: "Does my .NET 6 API with React frontend use Python?"

**Answer depends on the output:**

1. **Python: ❌ NO** → Your app does NOT use Python. It's pure .NET + React.

2. **Python: ✅ YES** → Your app DOES use Python. Check the detected files to understand how:
   - Files in `ml/`, `models/`, `ai/` → Machine learning components
   - Files in `scripts/`, `tools/` → Build/deployment tools (not runtime)
   - Files in separate service folders → Microservices architecture
   - Files in `api/`, `backend/` → Python backend services

### Common Scenarios

| Python Files Location | Likely Purpose | Part of Runtime? |
|----------------------|----------------|------------------|
| `/ml/` or `/models/` | Machine Learning | ✅ Yes |
| `/scripts/` or `/tools/` | Build/Deploy Scripts | ❌ No |
| `/python-api/` or `/python-service/` | Microservice | ✅ Yes |
| `/tests/` | Test Automation | ❌ No (dev only) |
| `/data/` or `/etl/` | Data Processing | ✅ Maybe |

---

## Quick Check Commands

If you can't run the full script, use these commands:

### Does my project use Python?
```bash
# Look for Python files
find . -name "*.py" -not -path "*/\.*" -not -path "*/node_modules/*" | head -10

# Look for Python package files
ls requirements.txt Pipfile pyproject.toml 2>/dev/null
```

### Does my project use .NET?
```bash
# Look for .NET project files
find . -name "*.csproj" -o -name "*.sln" | head -10

# Check .NET version
grep -r "TargetFramework" *.csproj 2>/dev/null
```

### Does my project use React?
```bash
# Check package.json for React
find . -name "package.json" -exec grep -l "react" {} \;

# Look for React components
find . -name "*.jsx" -o -name "*.tsx" | head -10
```

---

## Need Help?

See [TECH_STACK_DETECTION.md](TECH_STACK_DETECTION.md) for more detailed information about:
- Manual detection methods
- Understanding integration patterns
- Troubleshooting
- Next steps based on your results
