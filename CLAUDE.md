# CLAUDE.md

이 저장소에서 작업하는 Claude / 기여자를 위한 요약.

## 스택

- Python 3.10+, 패키지/실행 관리는 **uv** (pip/poetry 아님)
- MCP SDK: `mcp[cli]>=1.27,<2` (FastMCP 포함)
- 빌드 백엔드: hatchling
- 린트/포맷: ruff · 테스트: pytest (in-memory transport)
- 배포: git 소스 → PyPI 패키지 → MCP 레지스트리엔 `server.json` 메타데이터만 등록
  (registryType: pypi, runtimeHint: uvx)

## 코드 규칙

1. **stdio transport 에서 stdout(print) 금지.** 로그는 `sys.stderr` / `logging` 으로만.
2. 모든 도구(tool)는 **타입 힌트 + docstring** 작성 (스키마 자동 생성).
3. 도구는 `src/playmcp_server/tools/` 아래 모듈로 분리하고, `tools/__init__.py` 의
   `register_tools` 에서 등록한다. 새 카테고리(resources/prompts)도 같은 패턴.
4. 비밀키/토큰은 `.env` 로만 관리. `.env` 커밋 금지(`.gitignore` 포함), `.env.example` 만 커밋.

## 배포 체크리스트

- [ ] 버전 올릴 때 **`pyproject.toml` 의 `version` 과 `server.json` 의 `version` 을 동시에 수정**
      (두 값은 항상 일치해야 한다). `src/playmcp_server/__init__.py` 의 `__version__` 도 맞춘다.
- [ ] `uv run ruff check .` 통과
- [ ] `uv run pytest` 통과
- [ ] 태그 `v<version>` push → CI(`publish.yml`)가 PyPI Trusted Publishing 으로 업로드
- [ ] (조직 레포로 옮긴 뒤) `mcp-publisher` 로 레지스트리에 `server.json` 등록

## placeholder 주의

현재 조직/패키지/모듈/설명은 임시값이다. 확정 시 `./scripts/rename.sh` 로 일괄 변경한다.
