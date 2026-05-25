# Project 1: Deterministic Rule-Based Chatbot

A Python-based logic engine built from scratch to demonstrate explicit control flow, input sanitization, and deterministic AI guardrails. This project satisfies the Phase 1 requirements of the DecodeLabs training program.

## 🚀 Features

- **Continuous Input Loop:** Keeps the session active until an explicit exit command (`exit`, `quit`, `bye`) is received.
- **Data Sanitization & Normalization:** Processes raw user inputs by stripping trailing spaces and converting characters to lowercase to prevent logic bypasses.
- **Strict Intent Matching:** Maps inputs directly to specific predefined technical and everyday responses using precise if-else logic gates.
- **Zero Hallucination Guarantee:** Operates strictly as a "White Box" system, ensuring 100% predictability and auditability from input to output.

## 🧠 Core Architecture & AI Concepts Covered

- **System 1 (Probabilistic Core):** The README and bot behavior document how modern LLMs rely on text prediction and probabilistic generation, which introduces risks like hallucinations.
- **System 2 (Deterministic Layer):** The code serves as a rigid rule-based engine where rules are explicit, unyielding, and completely safe.
- **AI Guardrails:** Demonstrates the logic behind production-grade safety filters (like NVIDIA NeMo Guardrails or Llama Guard) used by enterprises to monitor and block unsafe AI behaviors.
- **IPO Model:** Strictly adheres to the Input (Sanitization), Process (Logic matching), and Output (Response loop) lifecycle.

## 🛠️ File Structure

- `chatbot.py`: The complete, dependency-free Python application codebase.
- `README.md`: System documentation and architectural overview.

## 💻 How to Run

1. Make sure you have Python 3 installed.
2. Run the file using your terminal:
   ```bash
   python chatbot.py
