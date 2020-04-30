import io
import pytest
from md_toc import toc


@pytest.fixture
def sample():
    talk = """
# Introduction
---
# Topic

## Subtopic
---
# Summary
"""
    return io.StringIO(talk)


def test_first(sample):
    assert toc(sample) == """# TOC
* [Introduction](#1)
* [Topic](#2)
  + [Subtopic](#2)
* [Summary](#3)
"""
