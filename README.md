

---

# Synapse 🧠

**A Pythonic framework for building and executing Cognitive Graphs with Large Language Models (LLMs).**

[![PyPI version](https://badge.fury.io/py/py-synapse-ai.svg)](https://badge.fury.io/py/py-synapse-ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Synapse allows you to move beyond simple, one-shot prompts and build complex, stateful, and reliable AI workflows. Instead of writing linear scripts, you define a "chain of thought" as a graph of interconnected **Cognitive Nodes**, where each node represents a specific, focused task for an LLM.

This approach makes your AI logic modular, easy to debug, and incredibly powerful.

---

## ✨ Key Features

*   **Cognitive Graphs:** Model complex reasoning tasks as a graph of dependent nodes, just like a human chain of thought.
*   **Pythonic by Design:** Built to feel natural for Python developers. No weird syntax, just classes and functions.
*   **Automatic Dependency Resolution:** Synapse automatically determines the correct order of execution. Just run your final node, and the entire graph resolves itself.
*   **Built-in Validation:** Attach Python functions as validators to each node to ensure the LLM's output is reliable and structured correctly.
*   **Modular and Reusable:** Each `CognitiveNode` is a self-contained component that can be saved, shared, and reused across different graphs.
*   **Persona Control:** Assign a specific persona or role to the LLM for each individual step in your workflow, ensuring contextually appropriate responses.

---

## 🚀 Quick Start

### 1. Installation

Install Synapse using `pip`:

```bash
pip install py-synapse-ai
```
*(Note: This is a placeholder name for PyPI. You would use the name you chose in `setup.py`)*

### 2. Basic Usage: Building a Simple Graph

Let's build a simple AI workflow that takes a topic, generates three creative ideas about it, and then picks the best one.

```python
# main.py
from synapse.framework import CognitiveNode, Graph

# --- Define the nodes in our graph ---

# Node 1: Generates creative ideas
idea_generator = CognitiveNode(
    persona="You are a world-class brainstorming assistant, known for wild and creative ideas.",
    instruction="Generate three distinct and innovative startup ideas based on the topic: '{{topic}}'."
)

# Node 2: Evaluates the ideas and picks the best one
idea_evaluator = CognitiveNode(
    persona="You are a pragmatic venture capitalist who looks for feasibility and market potential.",
    instruction="From the following list of ideas, pick the single most promising one and explain your choice in one sentence. Ideas:\n{{ideas_list}}"
)

# --- Connect the graph ---

# First, we need to set the initial input for our graph.
# We do this by "pre-executing" a simple node with our topic.
topic_input = CognitiveNode(instruction="urban farming").execute()

# Connect the topic_input to the idea_generator
idea_generator.connect(topic=topic_input)

# Connect the output of the idea_generator to the idea_evaluator
idea_evaluator.connect(ideas_list=idea_generator)

# --- Define the graph and run it! ---

# The final node in our graph is the evaluator.
creative_process_graph = Graph(final_node=idea_evaluator)

# Execute the entire workflow
best_idea = creative_process_graph.run()

print("--- The Best Idea ---")
print(best_idea)
```

---

## Core Concepts

### `CognitiveNode`
The `CognitiveNode` is the heart of Synapse. It's a Python object that encapsulates a single AI task.

-   **`instruction`**: A string template for the prompt. It can contain placeholders like `{{input_name}}` that will be filled by connected nodes.
-   **`persona`**: A string defining the role the LLM should adopt for this specific task.
-   **`validators`**: A list of Python functions that check the LLM's output. If a validator returns `False`, an exception is raised.
-   **`.connect(**kwargs)`**: A method to wire the inputs of this node to the outputs of other nodes.
-   **`.execute()`**: A method that runs the node's task. This is usually handled automatically by the graph.

### `Graph`
The `Graph` object is a simple executor. You initialize it with the final node of your workflow. When you call `.run()`, it triggers a recursive execution process that starts from the final node and works its way backward through all the dependencies.

---

## 🔧 Advanced Example: JSON Output with Validation

Synapse excels at creating reliable, structured data. Here’s how you can enforce a JSON output.

```python
import json
from synapse.framework import CognitiveNode, Graph

# A simple validator function
def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False

# The raw text we want to analyze
customer_feedback = "The new interface is sleek and much faster, but I can't find the export button anywhere!"

# The node that performs the analysis and formats the output
json_analyzer = CognitiveNode(
    persona="You are a data extraction bot that only speaks in JSON.",
    instruction="""
    Analyze the following customer feedback and return a JSON object with 'sentiment' and 'key_frustration'.
    Feedback: '{{feedback_text}}'
    """,
    validators=[is_valid_json] # Attach our validator!
)

# Connect the inputs
feedback_input = CognitiveNode(instruction=customer_feedback).execute()
json_analyzer.connect(feedback_text=feedback_input)

# Build and run the graph
analysis_graph = Graph(final_node=json_analyzer)
json_output = analysis_graph.run()

# Now you have a guaranteed valid JSON string
parsed_data = json.loads(json_output)
print(json.dumps(parsed_data, indent=2))
```

---

## 🤝 Contributing

This is an open-source project, and contributions are welcome! Please check the `CONTRIBUTING.md` file for guidelines on how to submit issues, feature requests, and pull requests.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
