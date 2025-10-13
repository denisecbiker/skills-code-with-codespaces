#!/usr/bin/env python3
"""
Tech Stack Detection Tool

This script analyzes a repository to detect which technologies are in use.
It checks for Python, .NET, React, and other common technologies.
"""

import os
import json
from pathlib import Path


def check_python_usage(root_dir):
    """Detect if the project uses Python."""
    indicators = {
        'python_files': [],
        'package_files': [],
        'virtual_env': False
    }
    
    for root, dirs, files in os.walk(root_dir):
        # Skip common directories
        if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', '.venv', 'venv']):
            continue
            
        for file in files:
            if file.endswith('.py'):
                indicators['python_files'].append(os.path.join(root, file))
            elif file in ['requirements.txt', 'Pipfile', 'pyproject.toml', 'setup.py', 'poetry.lock']:
                indicators['package_files'].append(os.path.join(root, file))
        
        if 'venv' in dirs or '.venv' in dirs or 'virtualenv' in dirs:
            indicators['virtual_env'] = True
    
    return indicators


def check_dotnet_usage(root_dir):
    """Detect if the project uses .NET."""
    indicators = {
        'project_files': [],
        'solution_files': [],
        'csharp_files': [],
        'version': None
    }
    
    for root, dirs, files in os.walk(root_dir):
        if '.git' in root or 'node_modules' in root:
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.csproj'):
                indicators['project_files'].append(file_path)
                # Try to detect .NET version
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        if 'net6.0' in content or '<TargetFramework>net6.0</TargetFramework>' in content:
                            indicators['version'] = '.NET 6'
                        elif 'net7.0' in content:
                            indicators['version'] = '.NET 7'
                        elif 'net8.0' in content:
                            indicators['version'] = '.NET 8'
                        elif 'netcoreapp' in content:
                            indicators['version'] = '.NET Core'
                except:
                    pass
            elif file.endswith('.sln'):
                indicators['solution_files'].append(file_path)
            elif file.endswith('.cs'):
                indicators['csharp_files'].append(file_path)
    
    return indicators


def check_react_usage(root_dir):
    """Detect if the project uses React."""
    indicators = {
        'package_json': [],
        'react_files': [],
        'is_react': False
    }
    
    for root, dirs, files in os.walk(root_dir):
        if '.git' in root or 'node_modules' in root:
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            if file == 'package.json':
                indicators['package_json'].append(file_path)
                # Check if React is a dependency
                try:
                    with open(file_path, 'r') as f:
                        pkg_data = json.load(f)
                        deps = pkg_data.get('dependencies', {})
                        dev_deps = pkg_data.get('devDependencies', {})
                        if 'react' in deps or 'react' in dev_deps:
                            indicators['is_react'] = True
                except:
                    pass
            elif file.endswith(('.jsx', '.tsx')):
                indicators['react_files'].append(file_path)
    
    return indicators


def detect_integration(python_indicators, dotnet_indicators, react_indicators):
    """Detect if Python is integrated with .NET and React."""
    has_python = bool(python_indicators['python_files'] or python_indicators['package_files'])
    has_dotnet = bool(dotnet_indicators['project_files'] or dotnet_indicators['csharp_files'])
    has_react = bool(react_indicators['is_react'] or react_indicators['react_files'])
    
    integration_type = []
    
    if has_python and has_dotnet:
        integration_type.append("Python-to-.NET integration (possible API calls or microservices)")
    if has_python and has_react:
        integration_type.append("Python-to-React integration (possible backend API)")
    if has_dotnet and has_react:
        integration_type.append(".NET-to-React integration (API with React frontend)")
    if has_python and has_dotnet and has_react:
        integration_type.append("Full-stack with all three technologies")
    
    return integration_type


def main():
    """Main function to detect tech stack."""
    root_dir = os.getcwd()
    
    print("=" * 60)
    print("TECH STACK DETECTION REPORT")
    print("=" * 60)
    print(f"\nAnalyzing directory: {root_dir}\n")
    
    # Check for Python
    python_indicators = check_python_usage(root_dir)
    print("🐍 PYTHON DETECTION:")
    if python_indicators['python_files']:
        print(f"   ✅ Found {len(python_indicators['python_files'])} Python file(s)")
        for f in python_indicators['python_files'][:5]:
            print(f"      - {f}")
        if len(python_indicators['python_files']) > 5:
            print(f"      ... and {len(python_indicators['python_files']) - 5} more")
    else:
        print("   ❌ No Python files found")
    
    if python_indicators['package_files']:
        print(f"   ✅ Found Python package file(s):")
        for f in python_indicators['package_files']:
            print(f"      - {os.path.basename(f)}")
    else:
        print("   ℹ️  No Python package files found")
    
    # Check for .NET
    dotnet_indicators = check_dotnet_usage(root_dir)
    print("\n⚙️  .NET DETECTION:")
    if dotnet_indicators['project_files']:
        print(f"   ✅ Found {len(dotnet_indicators['project_files'])} .NET project file(s)")
        if dotnet_indicators['version']:
            print(f"   ✅ Version: {dotnet_indicators['version']}")
        for f in dotnet_indicators['project_files'][:3]:
            print(f"      - {f}")
    else:
        print("   ❌ No .NET project files found")
    
    if dotnet_indicators['csharp_files']:
        print(f"   ✅ Found {len(dotnet_indicators['csharp_files'])} C# file(s)")
    else:
        print("   ℹ️  No C# files found")
    
    # Check for React
    react_indicators = check_react_usage(root_dir)
    print("\n⚛️  REACT DETECTION:")
    if react_indicators['is_react']:
        print("   ✅ React is listed as a dependency in package.json")
    else:
        print("   ❌ React not found in package.json")
    
    if react_indicators['react_files']:
        print(f"   ✅ Found {len(react_indicators['react_files'])} React component file(s)")
        for f in react_indicators['react_files'][:3]:
            print(f"      - {f}")
    else:
        print("   ℹ️  No .jsx or .tsx files found")
    
    # Integration detection
    print("\n🔗 INTEGRATION ANALYSIS:")
    integrations = detect_integration(python_indicators, dotnet_indicators, react_indicators)
    if integrations:
        for integration in integrations:
            print(f"   ℹ️  {integration}")
    else:
        has_python = bool(python_indicators['python_files'])
        has_dotnet = bool(dotnet_indicators['project_files'])
        has_react = bool(react_indicators['is_react'])
        
        if has_python and not has_dotnet and not has_react:
            print("   ℹ️  This appears to be a Python-only project")
        elif has_dotnet and not has_python and not has_react:
            print("   ℹ️  This appears to be a .NET-only project")
        elif has_react and not has_python and not has_dotnet:
            print("   ℹ️  This appears to be a React-only project")
        else:
            print("   ℹ️  No clear technology stack detected")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("=" * 60)
    has_python = bool(python_indicators['python_files'] or python_indicators['package_files'])
    has_dotnet = bool(dotnet_indicators['project_files'] or dotnet_indicators['csharp_files'])
    has_react = bool(react_indicators['is_react'] or react_indicators['react_files'])
    
    print(f"Python:  {'✅ YES' if has_python else '❌ NO'}")
    print(f".NET:    {'✅ YES' if has_dotnet else '❌ NO'}")
    print(f"React:   {'✅ YES' if has_react else '❌ NO'}")
    
    if has_python and has_dotnet and has_react:
        print("\n💡 Your .NET 6 API with React frontend DOES use Python!")
    elif has_dotnet and has_react and not has_python:
        print("\n💡 Your .NET 6 API with React frontend does NOT use Python.")
    elif has_python:
        print("\n💡 This project uses Python, but doesn't appear to have .NET or React.")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
