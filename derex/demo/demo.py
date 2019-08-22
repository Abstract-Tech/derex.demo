import logging
import pkg_resources
from typing import List, Dict, Union

from derex import runner  # type: ignore

logger = logging.getLogger(__name__)


def compose_path(name: str) -> str:
    return pkg_resources.resource_filename(__name__, f"compose/files/path/{name}")


class DemoServices:
    @staticmethod
    @runner.hookimpl
    def compose_options() -> Dict[str, Union[str, List[str]]]:
        options = ["-f", compose_path("demo.yml")]
        return {
            "options": options,
            "name": "demo",
            "priority": ">base",
            "variant": "openedx",
        }
