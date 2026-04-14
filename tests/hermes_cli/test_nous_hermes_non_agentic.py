"""Tests for the Nous-SHADOW-3/4 non-agentic warning detector.

Prior to this check, the warning fired on any model whose name contained
``"shadow"`` anywhere (case-insensitive). That false-positived on unrelated
local Modelfiles such as ``shadow-brain:qwen3-14b-ctx16k`` — a tool-capable
Qwen3 wrapper that happens to live under the "shadow" tag namespace.

``is_nous_shadow_non_agentic`` should only match the actual SHADOW-OVERLORD
SHADOW-3 / SHADOW-4 chat family.
"""

from __future__ import annotations

import pytest

from shadow_cli.model_switch import (
    _SHADOW_MODEL_WARNING,
    _check_shadow_model_warning,
    is_nous_shadow_non_agentic,
)


@pytest.mark.parametrize(
    "model_name",
    [
        "SHADOW-OVERLORD/SHADOW-3-Llama-3.1-70B",
        "SHADOW-OVERLORD/SHADOW-3-Llama-3.1-405B",
        "shadow-3",
        "SHADOW-3",
        "shadow-4",
        "shadow-4-405b",
        "shadow_4_70b",
        "openrouter/shadow3:70b",
        "openrouter/shadow-overlord/shadow-4-405b",
        "SHADOW-OVERLORD/SHADOW3",
        "shadow-3.1",
    ],
)
def test_matches_real_nous_shadow_chat_models(model_name: str) -> None:
    assert is_nous_shadow_non_agentic(model_name), (
        f"expected {model_name!r} to be flagged as Nous SHADOW 3/4"
    )
    assert _check_shadow_model_warning(model_name) == _SHADOW_MODEL_WARNING


@pytest.mark.parametrize(
    "model_name",
    [
        # Kyle's local Modelfile — qwen3:14b under a custom tag
        "shadow-brain:qwen3-14b-ctx16k",
        "shadow-brain:qwen3-14b-ctx32k",
        "shadow-honcho:qwen3-8b-ctx8k",
        # Plain unrelated models
        "qwen3:14b",
        "qwen3-coder:30b",
        "qwen2.5:14b",
        "claude-opus-4-6",
        "anthropic/claude-sonnet-4.5",
        "gpt-5",
        "openai/gpt-4o",
        "google/gemini-2.5-flash",
        "deepseek-chat",
        # Non-chat SHADOW models we don't warn about
        "shadow-llm-2",
        "shadow2-pro",
        "nous-shadow-2-mistral",
        # Edge cases
        "",
        "shadow",  # bare "shadow" isn't the 3/4 family
        "shadow-brain",
        "brain-shadow-3-impostor",  # "3" not preceded by /: boundary
    ],
)
def test_does_not_match_unrelated_models(model_name: str) -> None:
    assert not is_nous_shadow_non_agentic(model_name), (
        f"expected {model_name!r} NOT to be flagged as Nous SHADOW 3/4"
    )
    assert _check_shadow_model_warning(model_name) == ""


def test_none_like_inputs_are_safe() -> None:
    assert is_nous_shadow_non_agentic("") is False
    # Defensive: the helper shouldn't crash on None-ish falsy input either.
    assert _check_shadow_model_warning("") == ""
