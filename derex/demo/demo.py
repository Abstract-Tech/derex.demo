import logging
import pkg_resources
from typing import List, Dict, Callable

from derex import runner  # type: ignore

logger = logging.getLogger(__name__)


def compose_path(name: str) -> str:
    return pkg_resources.resource_filename(__name__, f"compose/files/path/{name}")


class Config:
    def yaml_opts_openedx(self) -> List[str]:
        return ["-f", compose_path("demo.yml")]

    @runner.hookimpl
    def settings(self) -> Dict[str, Callable]:
        logger.info("Running in plugin Demo")
        return {"openedx": self.yaml_opts_openedx}
