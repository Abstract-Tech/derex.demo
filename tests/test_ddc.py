# -*- coding: utf-8 -*-
from click.testing import CliRunner


runner = CliRunner()


def test_ensure_plugin_loaded():
    from derex.runner.cli import ddc_ironwood

    result = runner.invoke(ddc_ironwood, ["config"])

    assert "Loading demo" in result.output
    assert "demo_lms" in result.output
