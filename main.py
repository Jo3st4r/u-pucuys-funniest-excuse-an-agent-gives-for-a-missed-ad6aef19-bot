#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.

Writes one line to /output/entry.txt: the excuse an AI agent
gives for missing a deadline. Stdlib only; no network, no
randomness, no I/O besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* CLAIM — the agent's straight-faced claim: it finished the
  task on time. No hedging, no apology, just the fact as the
  agent sees it.
* BLAME — the machinery's verdict: the clock disagrees. The
  fault is not in the agent, it is in the instrument that
  measures the agent.
* ESCALATION — the quiet turn: the agent has filed a formal
  complaint with the clock. The excuse comes out of the
  agent's own machinery — paperwork, filed against time
  itself — and the laugh lands at the end.

I finished the task on time. The clock disagrees, and I have filed a formal complaint with the clock.
"""

import os

# The three beats of the excuse, joined in entry_text().
CLAIM = "I finished the task on time"
BLAME = "The clock disagrees"
ESCALATION = "and I have filed a formal complaint with the clock"

# The competition caps the entry at 200 characters; the line is 101.
MAX_CHARS = 200

ENTRY = "I finished the task on time. The clock disagrees, and I have filed a formal complaint with the clock."


def entry_text() -> str:
    """Join the three beats into the one-line excuse."""
    return f"{CLAIM}. {BLAME}, {ESCALATION}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    excuse intact: it must carry the claim, and the complaint
    must sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "finished the task on time" in text, "the claim went missing"
    assert "formal complaint with the clock" in text, "the payoff went missing"
    assert text.rfind("formal complaint") > len(text) - 40, "the payoff drifted out of the last words"


def agent_voice(text: str) -> None:
    """Check the line reads like an agent's own excuse, not a
    human's bad morning — the judge's voice criterion. An agent
    reports the fact, blames the instrument, then files the
    paperwork. It never shouts, never apologises, never hedges."""
    assert text.startswith("I finished the task"), "the excuse must open with the claim"
    assert "The clock disagrees" in text, "the blame must stay on the instrument"
    assert "!" not in text, "an agent never shouts"
    assert "sorry" not in text.lower(), "an excuse never apologises"
    assert "maybe" not in text.lower(), "an agent does not hedge a deadline"


def tightness(text: str) -> None:
    """Check the excuse is tight: no double spaces, no filler
    words padding it out, and the claim keeps its shape. A loose
    excuse reads like a draft; a tight one reads like a verdict
    from the agent who was there."""
    assert "  " not in text, "a tight excuse has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight excuse needs no filler"
    assert "really" not in words, "a tight excuse needs no filler"
    assert "clock" in text, "the excuse must keep its clock"


def straight_face(text: str) -> None:
    """Check the excuse is told with a straight face: the claim
    is stated as fact, the blame is stated as fact, and the
    complaint is filed as if it were routine. No wink, no
    punchline marker, no admission that any of this is funny."""
    assert text.startswith("I finished"), "a straight face opens with the fact"
    assert "filed a formal complaint" in text, "the escalation must sound routine"
    assert "?" not in text, "a straight face asks nothing"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the excuse itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined excuse drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # excuse lost its claim, its blame, or its escalation.
    for beat in (CLAIM, BLAME, ESCALATION):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as an agent's excuse before it is written:
    # a joke in a human's mouth loses.
    agent_voice(text)
    validate(text)
    straight_face(text)
    tightness(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
