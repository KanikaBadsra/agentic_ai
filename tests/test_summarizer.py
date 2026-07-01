import unittest
from unittest.mock import patch

from app.graphs.nodes.summarizer_node import summarizer_node


class SummarizerTests(unittest.TestCase):
    def test_summarizer_returns_fallback_values_when_history_lookup_fails(self):
        with patch(
            "app.graphs.nodes.summarizer_node.get_conversation_history",
            side_effect=RuntimeError("db unavailable"),
        ), patch("app.graphs.nodes.summarizer_node.llm.invoke") as mock_invoke:
            mock_invoke.return_value = type("Response", (), {"content": "fallback answer"})()

            result = summarizer_node(
                {
                    "question": "why europe sales are down",
                    "session_id": "demo",
                    "documents": [],
                }
            )

            self.assertEqual(result["final_answer"], "fallback answer")
            self.assertIsNotNone(result["confidence_score"])
            self.assertIsNotNone(result["risk_level"])
            self.assertIsNotNone(result["requires_human_review"])
            self.assertIsNotNone(result["guardrail_status"])


if __name__ == "__main__":
    unittest.main()
