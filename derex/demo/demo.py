import logging
import pkg_resources
from typing import List, Dict, Callable

from derex import runner

logger = logging.getLogger(__name__)


class Config(runner.config.BaseConfig):
    def compose_path(self, name: str) -> str:
        return pkg_resources.resource_filename(__name__, f"compose/files/path/{name}")

    def yaml_opts_openedx(self) -> List[str]:
        result = super(Config, self).yaml_opts_openedx()
        result += ["-f", self.compose_path("demo.yml")]
        return result

    @runner.hookimpl
    def settings(self) -> Dict[str, Callable]:
        logger.info("Running in plugin Demo")
        return {"services": self.yaml_opts_services, "openedx": self.yaml_opts_openedx}
