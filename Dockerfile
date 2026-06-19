FROM python:3.12-slim

WORKDIR /app

# uv 바이너리 복사 (공식 권장 방식)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# 의존성 파일 먼저 복사 (레이어 캐시 활용)
COPY pyproject.toml uv.lock README.md ./
COPY src/ ./src/

# 패키지 설치
RUN uv pip install --system -e .

EXPOSE 8000

# SSE transport로 HTTP 서버 실행 (PlayMCP in KC 등록용)
CMD ["python", "-c", \
     "from playmcp_server.server import mcp; mcp.run(transport='sse', host='0.0.0.0', port=8000)"]
