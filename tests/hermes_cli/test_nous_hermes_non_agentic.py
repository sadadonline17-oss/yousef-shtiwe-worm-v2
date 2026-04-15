"""Tests for the Yousef Shtiwe-YOUSEF SHTIWE-3/4 non-agentic warning detector.

Prior to this check, the warning fired on any model whose name contained
``"yousef shtiwe"`` anywhere (case-insensitive). That false-positived on unrelated
local Modelfiles such as ``yousef shtiwe-brain:qwen3-14b-ctx16k`` — a tool-capable
Qwen3 wrapper that happens to live under the "yousef shtiwe" tag namespace.

``is_yousef shtiwe_yousef shtiwe_non_agentic`` should only match the actual YOUSEF SHTIWE-OVERLORD
YOUSEF SHTIWE-3 / YOUSEF SHTIWE-4 chat family.
"""

from __future__ import annotations

import pytest

from yousef shtiwe_cli.model_switch import (
    _YOUSEF SHTIWE_MODEL_WARNING,
    _check_yousef shtiwe_model_warning,
    is_yousef shtiwe_yousef shtiwe_non_agentic,
)


@pytest.mark.parametrize(
    "model_name",
    [
        "YOUSEF SHTIWE-OVERLORD/YOUSEF SHTIWE-3-Llama-3.1-70B",
        "YOUSEF SHTIWE-OVERLORD/YOUSEF SHTIWE-3-Llama-3.1-405B",
        "yousef shtiwe-3",
        "YOUSEF SHTIWE-3",
        "yousef shtiwe-4",
        "yousef shtiwe-4-405b",
        "yousef shtiwe_4_70b",
        "openrouter/yousef shtiwe3:70b",
        "openrouter/yousef shtiwe-overlord/yousef shtiwe-4-405b",
        "YOUSEF SHTIWE-OVERLORD/YOUSEF SHTIWE3",
        "yousef shtiwe-3.1",
    ],
)
def test_matches_real_yousef shtiwe_yousef shtiwe_chat_models(model_name: str) -> None:
    assert is_yousef shtiwe_yousef shtiwe_non_agentic(model_name), (
        f"expected {model_name!r} to be flagged as Yousef Shtiwe YOUSEF SHTIWE 3/4"
    )
    assert _check_yousef shtiwe_model_warning(model_name) == _YOUSEF SHTIWE_MODEL_WARNING


@pytest.mark.parametrize(
    "model_name",
    [
        # Kyle's local Modelfile — qwen3:14b under a custom tag
        "yousef shtiwe-brain:qwen3-14b-ctx16k",
        "yousef shtiwe-brain:qwen3-14b-ctx32k",
        "yousef shtiwe-honcho:qwen3-8b-ctx8k",
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
        # Non-chat YOUSEF SHTIWE models we don't warn about
        "yousef shtiwe-llm-2",
        "yousef shtiwe2-pro",
        "yousef shtiwe-yousef shtiwe-2-mistral",
        # Edge cases
        "",
        "yousef shtiwe",  # bare "yousef shtiwe" isn't the 3/4 family
        "yousef shtiwe-brain",
        "brain-yousef shtiwe-3-impostor",  # "3" not preceded by /: boundary
    ],
)
def test_does_not_match_unrelated_models(model_name: str) -> None:
    assert not is_yousef shtiwe_yousef shtiwe_non_agentic(model_name), (
        f"expected {model_name!r} NOT to be flagged as Yousef Shtiwe YOUSEF SHTIWE 3/4"
    )
    assert _check_yousef shtiwe_model_warning(model_name) == ""


def test_none_like_inputs_are_safe() -> None:
    assert is_yousef shtiwe_yousef shtiwe_non_agentic("") is False
    # Defensive: the helper shouldn't crash on None-ish falsy input either.
    assert _check_yousef shtiwe_model_warning("") == ""
