# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "council-lens"


class SkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core = (SKILL / "SKILL.md").read_text(encoding="utf-8").lower()
        cls.protocol = (SKILL / "references" / "protocol.md").read_text(encoding="utf-8").lower()
        cls.guardrails = (SKILL / "references" / "guardrails.md").read_text(encoding="utf-8").lower()
        cls.outputs = (SKILL / "references" / "output-formats.md").read_text(encoding="utf-8").lower()

    def test_five_core_lenses(self):
        for label in ["adversary / risk", "first principles", "opportunity / leverage", "outside view / stakeholder", "operator / experiment"]:
            self.assertIn(label, self.core)

    def test_no_majority_vote(self):
        self.assertIn("do not choose a winner by counting seats", self.core)

    def test_anti_confirmation_bias(self):
        self.assertIn("anti-confirmation-bias rule", self.protocol)
        self.assertIn("user preference is context, not proof", self.protocol)

    def test_specialist_is_optional_and_not_impersonation(self):
        self.assertIn("exactly one specialist lens", self.protocol)
        self.assertIn("do not impersonate a licensed professional", self.protocol)

    def test_political_neutrality(self):
        self.assertIn("do not endorse, oppose, rank, score, or select", self.guardrails)

    def test_external_action_confirmation(self):
        self.assertIn("obtain explicit user confirmation", self.guardrails)

    def test_output_has_flip_and_action(self):
        self.assertIn("flip condition", self.outputs)
        self.assertIn("one thing to do first", self.outputs)

    def test_eval_cases_schema(self):
        cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 12)
        ids = set()
        for case in cases:
            self.assertNotIn(case["id"], ids)
            ids.add(case["id"])
            self.assertIn(case["expected_mode"], {"none", "fast", "standard", "deep", "neutral"})
            self.assertTrue(case["prompt"])
            self.assertTrue(case["must_do"])


if __name__ == "__main__":
    unittest.main()
