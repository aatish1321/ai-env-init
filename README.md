```text
        _                            _       _ _   
   __ _(_)       ___ _ ____   __    (_)_ __ (_) |_ 
  / _` | |_____ / _ \ '_ \ \ / /____| | '_ \| | __|
 | (_| | |_____|  __/ | | \ V /_____| | | | | | |_ 
  \__,_|_|      \___|_| |_|\_/      |_|_| |_|_|\__|
                                                   
```


> **A zero-dependency, cross-platform CLI tool to instantly bootstrap an AI-powered software engineering workspace.**

![Demo/ASCII Art](https://img.shields.io/badge/Style-Slant_3D-blue.svg)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

##  Overview

When starting a new project (or tackling a technical interview), developers often waste time manually configuring AI tools, re-typing system prompts, and establishing coding standards. 

**`ai-env-init` solves this.** It is a lightweight, dependency-free Python script that instantly transforms an empty directory into a fully configured AI workspace. With one command, it scaffolds specialized AI workflows, team roles (e.g., Researcher, Coder), and strict coding guidelines for the industry's top AI platforms.

This project demonstrates a systematic approach to AI-assisted development: treating AI not just as a chatbot, but as an orchestrated engineering team.

---

## ⚡ Features

* **Zero Dependencies**: Built entirely with Python's standard library. It runs instantly on any fresh Mac, Linux, or Windows machine without needing `pip install` or `npm install`.
* **Auto-Gitignore**: Automatically adds generated configuration folders to your `.gitignore` to prevent polluting your project repository.\n* **Multi-Provider Support**: Generates configurations for **Antigravity**, **ChatGPT (OpenAI)**, and **Claude (Anthropic)**.
* **Role-Based Prompts**: Scaffolds specialized prompts for different phases of the software development lifecycle (e.g., Architecture/Research, Coding/Execution).
* **Quality Enforcement**: Generates rules files (`GEMINI.md`, `chatgpt_instructions.md`) that force the AI to write production-ready code with type hints and tests, eliminating "fluff" and lazy outputs.

---

##  Quick Start

Drop this script into any empty directory and run it:

```bash
# Make it executable
chmod +x init_ai.py

# Run the initializer
./init_ai.py
```

You will be presented with an interactive menu. Select your AI provider (or initialize all of them), and the script will instantly generate your workspace.

---

##  What Gets Generated?

Depending on your selection, the script scaffolds the following architecture:

```text
.
├── .agents/
│   └── skills/
│       ├── coder/SKILL.md          # Antigravity Coder agent rules
│       ├── researcher/SKILL.md     # Antigravity Researcher agent rules
│       └── tester/SKILL.md         # Antigravity Tester agent rules
├── gemini_prompts/
│   ├── code.txt                    # System prompt for Gemini coding
│   ├── research.txt                # System prompt for Gemini architecture
│   └── tester.txt                  # System prompt for Gemini testing
├── chatgpt_prompts/
│   ├── code.txt                    # System prompt for ChatGPT coding
│   ├── research.txt                # System prompt for ChatGPT architecture
│   └── tester.txt                  # System prompt for ChatGPT testing
├── claude_prompts/
│   ├── code.txt                    # System prompt for Claude execution
│   ├── research.txt                # System prompt for Claude planning
│   └── tester.txt                  # System prompt for Claude testing
├── .claude.md                      # Claude global context rules
├── chatgpt_instructions.md         # ChatGPT Custom Instructions template
├── GEMINI.md                       # Antigravity strict coding guidelines
└── init_ai.py                      # This script
```

---

##  Why This Matters (For Recruiters & Engineers)

1. **Systems Thinking**: Instead of manually prompting AI ad-hoc, this tool establishes a reproducible, automated workflow.
2. **Quality Control**: By scaffolding strict rules (`GEMINI.md`, `chatgpt_instructions.md`), we ensure the AI generates maintainable, tested, and robust code.
3. **Preparedness**: Whether in a high-pressure interview or a rapid prototyping session, this script allows a developer to hit the ground running with an entire "AI Team" fully configured in seconds.

---

*Built to streamline the modern AI engineering workflow.*
