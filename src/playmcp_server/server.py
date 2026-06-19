"""FastMCP 서버 인스턴스와 진입점.

stdio transport 에서는 stdout(print) 을 절대 사용하지 않는다.
모든 로그는 sys.stderr 로 보낸다 (logging.basicConfig(stream=sys.stderr)).
"""

import logging
import sys

from mcp.server.fastmcp import FastMCP

from playmcp_server.config import load_config
from playmcp_server.tools import register_tools

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

logger = logging.getLogger("playmcp_server")

# FastMCP 인스턴스. 이름은 PACKAGE_NAME 과 맞춘다.
mcp = FastMCP("playmcp-server")

# 설정 로딩 (.env 없으면 통과)
config = load_config()

# tools/ 아래 도구들을 등록한다.
register_tools(mcp)


def main() -> None:
    """콘솔 스크립트 진입점. stdio transport 로 서버를 실행한다."""
    logger.info("starting playmcp-server (stdio transport)")
    mcp.run()


if __name__ == "__main__":
    main()
