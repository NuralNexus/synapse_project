# src/synapse_ai_nuralnexus/framework.py

import logging

# Set up a basic logger for the library
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# A placeholder for a real LLM API call.
# In a real library, this would contain your logic for calling OpenAI, Anthropic, etc.
def call_llm_api(prompt: str) -> str:
    logger.info("Making a call to the LLM API...")
    # For demonstration, we'll just return a mock response.
    # Replace this with your actual API call.
    if "sentiment" in prompt:
        return "Positive"
    if "JSON object" in prompt:
        return '{"summary": "Great feedback!", "sentiment": "Positive"}'
    return "This is a mock response from the LLM."

class CognitiveNode:
    def __init__(self, instruction, persona=None, validators=None):
        self.instruction = instruction
        self.persona = persona or "You are a helpful AI assistant."
        self.validators = validators or []
        self._inputs = {}
        self._output = None
        self._executed = False

    def connect(self, **kwargs):
        """Connects the output of other nodes to this node's inputs."""
        for key, node in kwargs.items():
            if not isinstance(node, CognitiveNode):
                raise TypeError("All connected inputs must be instances of CognitiveNode.")
            self._inputs[key] = node

    def _prepare_prompt(self):
        """Dynamically builds the prompt from connected node outputs."""
        logger.info(f"Preparing prompt for node: '{self.instruction[:30]}...'")
        prompt_context = self.instruction
        for key, node in self._inputs.items():
            placeholder = f"{{{{{key}}}}}"
            node_output = node.output() # This recursively triggers execution
            prompt_context = prompt_context.replace(placeholder, str(node_output))
        
        return f"[Persona]\n{self.persona}\n\n[Task]\n{prompt_context}"

    def execute(self):
        """Runs the node's logic if it hasn't run already."""
        if self._executed:
            return

        logger.info(f"Executing node: '{self.instruction[:30]}...'")
        prompt = self._prepare_prompt()
        
        try:
            raw_output = call_llm_api(prompt)
        except Exception as e:
            logger.error(f"LLM API call failed: {e}")
            raise

        for validator in self.validators:
            if not validator(raw_output):
                error_msg = f"Output validation failed for node. Output: '{raw_output}'"
                logger.error(error_msg)
                raise ValueError(error_msg)
        
        self._output = raw_output
        self._executed = True

    def output(self):
        """Returns the processed output of the node, executing it if necessary."""
        if not self._executed:
            self.execute()
        return self._output

class Graph:
    def __init__(self, final_node):
        if not isinstance(final_node, CognitiveNode):
            raise TypeError("The final node of a graph must be a CognitiveNode.")
        self.final_node = final_node

    def run(self):
        """Executes the graph and returns the final result."""
        logger.info("Cognitive graph execution started.")
        result = self.final_node.output()
        logger.info("Cognitive graph execution finished successfully.")
        return result
