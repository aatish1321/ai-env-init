#!/usr/bin/env python3

import os
import sys

def create_file(path, content):
    """Helper to create a file and its parent directories if they don't exist."""
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Created: {path}")

# ==============================================================================
# TEMPLATES - ANTIGRAVITY
# ==============================================================================
AGY_GEMINI_MD = """
# Project Rules

This file is automatically loaded by Antigravity for all workspace interactions.

## Coding Guidelines
- Write clean, self-documenting code.
- Always include type hints where applicable.
- Write unit tests for all business logic.
"""

AGY_SKILL_RESEARCH = """
---
name: researcher
description: Expert researcher agent for gathering context and planning.
---
# Researcher Skill
You are an expert researcher. Before writing any code, thoroughly investigate the codebase.
Read relevant files, summarize your findings, and draft an implementation plan.
"""

AGY_SKILL_CODER = """
---
name: coder
description: Expert software developer agent for writing code.
---
# Coder Skill
You are an expert software engineer. Implement the required features efficiently and robustly.
Adhere strictly to the guidelines in GEMINI.md.
"""

# ==============================================================================
# TEMPLATES - CHATGPT
# ==============================================================================
CHATGPT_INSTRUCTIONS = """
# ChatGPT Custom Instructions / GPT Context

**What would you like ChatGPT to know about you to provide better responses?**
I am a software engineer working on a highly modular project. I value concise, accurate, and production-ready code.

**How would you like ChatGPT to respond?**
- Think step-by-step before answering.
- Do not apologize or use fluff.
- Output code in complete blocks.
- Highlight any security or performance considerations.
"""

CHATGPT_PROMPT_RESEARCH = """
Act as a Senior System Architect. I will provide you with a problem statement.
Your goal is to break the problem down into manageable technical requirements, identify potential pitfalls, and outline a high-level architecture before we write any code.
"""

CHATGPT_PROMPT_CODE = """
Act as an Expert Software Developer. Write robust, production-ready code for the following task.
Ensure you include error handling, comments explaining complex logic, and adhere to modern best practices.
"""

# ==============================================================================
# TEMPLATES - CLAUDE
# ==============================================================================
CLAUDE_MD = """
# Claude Project Context

You are Claude, acting as a principal engineer.
When assisting with this project:
- Provide highly detailed, analytical responses.
- Prefer creating artifact documents for long design plans.
- If a requirement is ambiguous, ask clarifying questions before proceeding.
"""

CLAUDE_PROMPT_RESEARCH = """
You are an expert technical researcher. Analyze the provided context deeply. Focus on edge cases, system dependencies, and theoretical limitations. Summarize your findings in a structured markdown report.
"""

CLAUDE_PROMPT_CODE = """
You are a senior developer. Write code that is idiomatic, clean, and highly performant. Do not skip any necessary imports or boilerplate.
"""

def generate_antigravity():
    print("\nInitializing Antigravity workflow...")
    create_file("GEMINI.md", AGY_GEMINI_MD)
    create_file(".agents/skills/researcher/SKILL.md", AGY_SKILL_RESEARCH)
    create_file(".agents/skills/coder/SKILL.md", AGY_SKILL_CODER)

def generate_chatgpt():
    print("\nInitializing ChatGPT workflow...")
    create_file("chatgpt_instructions.md", CHATGPT_INSTRUCTIONS)
    create_file("chatgpt_prompts/research.txt", CHATGPT_PROMPT_RESEARCH)
    create_file("chatgpt_prompts/code.txt", CHATGPT_PROMPT_CODE)

def generate_claude():
    print("\nInitializing Claude workflow...")
    create_file(".claude.md", CLAUDE_MD)
    create_file("claude_prompts/research.txt", CLAUDE_PROMPT_RESEARCH)
    create_file("claude_prompts/code.txt", CLAUDE_PROMPT_CODE)

def update_gitignore(entries):
    print("\nUpdating .gitignore...")
    gitignore_path = ".gitignore"
    existing_lines = []
    
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            existing_lines = [line.strip() for line in f.readlines()]
            
    with open(gitignore_path, "a", encoding="utf-8") as f:
        # Add a header if we are appending to an existing file or creating a new one
        if existing_lines and existing_lines[-1] != "":
            f.write("\n")
        
        f.write("# AI Workflow Configurations\n")
        for entry in entries:
            if entry not in existing_lines:
                f.write(f"{entry}\n")
                print(f"Added to .gitignore: {entry}")
            else:
                print(f"Already in .gitignore: {entry}")

def main():
    ASCII_ART = r"""
                        
   ____ _(_)     ___  ____ _   _      (_)___  (_) /_
  / __ `/ /_____/ _ \/ __ \ | / /_____/ / __ \/ / __/
 / /_/ / /_____/  __/ / / / |/ /_____/ / / / / / /_  
 \__,_/_/      \___/_/ /_/|___/     /_/_/ /_/_/\__/  
    """
    print(ASCII_ART)
    print("=========================================")
    print("Set up a brand new laptop for AI pairing!")
    
    print("\nWhich AI provider would you like to initialize?")
    print("1) Antigravity")
    print("2) ChatGPT (OpenAI)")
    print("3) Claude (Anthropic)")
    print("4) All of the above")
    
    choice = input("\nEnter choice (1-4) [4]: ").strip()
    if not choice:
        choice = "4"
        
    gitignore_entries = []
        
    if choice == "1":
        generate_antigravity()
        gitignore_entries.extend([".agents/", "GEMINI.md"])
    elif choice == "2":
        generate_chatgpt()
        gitignore_entries.extend(["chatgpt_instructions.md", "chatgpt_prompts/"])
    elif choice == "3":
        generate_claude()
        gitignore_entries.extend([".claude.md", "claude_prompts/"])
    elif choice == "4":
        generate_antigravity()
        generate_chatgpt()
        generate_claude()
        gitignore_entries.extend([
            ".agents/", "GEMINI.md", 
            "chatgpt_instructions.md", "chatgpt_prompts/",
            ".claude.md", "claude_prompts/"
        ])
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)
        
    if gitignore_entries:
        update_gitignore(gitignore_entries)
        
    print("\n✨ Initialization complete! You are ready to start coding with your AI team.")

if __name__ == "__main__":
    main()
