# tests/test_framework.py

import unittest
from unittest.mock import patch
from synapse_ai_nuralnexus.framework import CognitiveNode, Graph

class TestCognitiveGraph(unittest.TestCase):

    def test_node_creation(self):
        """Tests that a CognitiveNode can be created successfully."""
        node = CognitiveNode("Test instruction")
        self.assertEqual(node.instruction, "Test instruction")
        self.assertIsNotNone(node.persona)

    def test_graph_execution_flow(self):
        """Tests that nodes connect and execute in the correct order."""
        
        # We use 'patch' to "mock" the LLM API call.
        # This makes our test fast and free, as it doesn't actually call an LLM.
        with patch('synapse_ai_nuralnexus.framework.call_llm_api') as mock_llm_call:
            # We define what the mock API should return for each prompt it receives.
            mock_llm_call.side_effect = [
                "Fact 1: The sky is blue.", # Response for the first node
                "Positive",                  # Response for the second node
            ]

            # Define the graph
            node1 = CognitiveNode("Extract facts about {{topic}}.")
            node2 = CognitiveNode("Determine sentiment from these facts: {{facts}}")
            
            topic_input = CognitiveNode("the sky")._output = "the sky" # Manually set output for input
            
            node1.connect(topic=topic_input)
            node2.connect(facts=node1)
            
            graph = Graph(final_node=node2)
            result = graph.run()

            # Assert that the final result is what we expect
            self.assertEqual(result, "Positive")
            # Assert that the LLM was called twice
            self.assertEqual(mock_llm_call.call_count, 2)

if __name__ == '__main__':
    unittest.main()
