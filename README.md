# synapse_project

---

### **Building `py-synapse-ai`: A Guided Walkthrough**

We will follow the PyPA tutorial's structure precisely. I will provide the content for each file you need to create.

#### **1. Project Structure Setup**

First, let's confirm the file structure. Based on the tutorial, this is the ideal layout for our project. Let's assume your username is `nuralnexus` for uniqueness.

```
synapse_project/
├── src/
│   └── synapse_ai_nuralnexus/
│       ├── __init__.py
│       └── framework.py
├── tests/
├── LICENSE
├── pyproject.toml
└── README.md
```
*   `synapse_ai_nuralnexus/`: This is our **package directory**. The code that people will import lives here.
*   `framework.py`: This file will contain our `CognitiveNode` and `Graph` classes.
*   `__init__.py`: This empty file tells Python that `synapse_ai_nuralnexus` is a package that can be imported.

#### **2. Creating the Core Package Files**

Now, let's create the configuration and informational files.

##### **`pyproject.toml` (The "Blueprint")**

This is the most important configuration file. It tells tools like `pip` *how* to build your project. We'll use the `hatchling` backend as recommended by the modern PyPA guide, as it's simple and powerful.

**Create `pyproject.toml` with this content:**
```toml
# pyproject.toml

# Defines the build system and its requirements.
# This tells pip it needs 'hatchling' to build the project.
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

# Defines the core metadata for your project.
# This is what will appear on PyPI.
[project]
name = "synapse-ai-nuralnexus" # Unique name for PyPI
version = "0.1.0"
authors = [
  { name="Your Name", email="your.email@example.com" },
]
description = "A Pythonic framework for building and executing Cognitive Graphs with LLMs."
readme = "README.md" # Specifies the README file
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]

# (Optional) You can define project URLs here
[project.urls]
"Homepage" = "https://github.com/your_username/synapse_project"
"Bug Tracker" = "https://github.com/your_username/synapse_project/issues"
```

**Why this works:**

*   `[build-system]` is standard boilerplate. You rarely need to change it.
*   `[project]` contains all the metadata `setup.py` used to hold. It's the modern, cleaner way to define your project. `name`, `version`, and `description` are essential.
*   `readme = "README.md"` tells the build system to use your `README.md` file as the long description on PyPI.

##### **`README.md` (The "Front Page")**

I've already generated a detailed README for you. That one is perfect and follows best practices. It has a clear description, installation instructions, and examples.

##### **`LICENSE` (The "Legal Agreement")**

As the tutorial states, this is crucial. The MIT License is a great choice for open-source projects because it's simple and permissive.

**Create `LICENSE` with this content:**
```
Copyright (c) 2023 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

#### **3. Generating the Distribution Archives**

Now you're ready to build the package.

1.  **Install the build tool:**
    ```bash
    pip install build
    ```
2.  **Run the build command** from your project's root directory (`synapse_project/`):
    ```bash
    python -m build
    ```

This command will read your `pyproject.toml`, use `hatchling` to package your `src/synapse_ai_nuralnexus` directory, and create a `dist/` folder containing two files:
*   `synapse_ai_nuralnexus-0.1.0-py3-none-any.whl` (The "built" distribution, faster to install)
*   `synapse_ai_nuralnexus-0.1.0.tar.gz` (The "source" distribution, more universal)

#### **4. Uploading to PyPI (and TestPyPI)**

This is for sharing your library. The tutorial's instructions are perfect.

1.  **Install Twine:**
    ```bash
    pip install twine
    ```
2.  **Upload to TestPyPI first (highly recommended):**
    ```bash
    twine upload --repository testpypi dist/*
    ```
    You will be prompted for your API token from TestPyPI.

3.  **Upload to the real PyPI (when you're ready):**
    ```bash
    twine upload dist/*
    ```

#### **5. Installing and Testing Your Package**

To test it, you can install it directly from TestPyPI into a new virtual environment:

```bash
pip install --index-url https://test.pypi.org/simple/ synapse-ai-nuralnexus
```

Then, you can run a Python script from anywhere on your computer:
```python
from synapse_ai_nuralnexus.framework import CognitiveNode

# Your code here...
```
Notice how the import path `synapse_ai_nuralnexus.framework` directly matches your folder structure `src/synapse_ai_nuralnexus/framework.py`. This is the direct result of following the modern packaging standards.



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
