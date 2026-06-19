<!-- mcp-name: io.github.PlayMCP-SDC/playmcp-server -->

# playmcp-server

PlayMCP MCP 서버 (설명을 채워주세요)

> ⚠️ 이 프로젝트는 **placeholder 값**으로 생성된 골격입니다.
> 조직명/패키지명/모듈명/설명이 확정되면 `./scripts/rename.sh` 로 한 번에 변경하세요.
> 자세한 건 아래 [이름 변경](#이름-변경-placeholder--실제-값) 참고.

## 설치 / 개발 방법

### 실행 (배포 후, 최종 사용자)

```bash
uvx playmcp-server
```

### 로컬 개발

```bash
# 가상환경 + 의존성 설치
uv venv
source .venv/bin/activate
uv sync

# MCP Inspector 로 도구 테스트
uv run mcp dev src/playmcp_server/server.py

# 린트 / 테스트
uv run ruff check .
uv run pytest
```

## 프로젝트 구조

```
playmcp-server/
├── src/playmcp_server/
│   ├── server.py        # FastMCP 인스턴스 + main() 진입점
│   ├── config.py        # 환경변수/설정 로딩
│   ├── tools/           # 도구 모듈 (register_tools 로 등록)
│   ├── resources/       # 리소스 자리
│   └── prompts/         # 프롬프트 자리
├── tests/               # in-memory transport pytest
├── docs/                # 설계 문서
├── scripts/rename.sh    # placeholder 일괄 변경 스크립트
├── pyproject.toml       # 빌드/의존성 (hatchling)
├── server.json          # MCP 레지스트리 메타데이터
└── .github/             # CI/CD, CODEOWNERS, PR 템플릿
```

## 네이밍 규칙

| 용도 | 형식 | 값 |
| --- | --- | --- |
| PyPI / 명령어 | 소문자-하이픈 | `playmcp-server` |
| Python 패키지 | 소문자_밑줄 | `playmcp_server` |
| 레지스트리 네임스페이스 | `io.github.<ORG>/<PKG>` | `io.github.PlayMCP-SDC/playmcp-server` |

> 위 표의 `<!-- mcp-name: ... -->` 주석은 `server.json` 의 `name` 과 **정확히 일치**해야
> 레지스트리 소유권 검증을 통과합니다.

## 이름 변경 (placeholder → 실제 값)

조직명·패키지명·모듈명·설명이 확정되면:

```bash
./scripts/rename.sh <new-org> <new-package-name> <new_module_name> "<한 줄 설명>"
# 예) ./scripts/rename.sh PlayMCP-SDC weather-mcp weather_mcp "날씨 정보 MCP 서버"
```

스크립트가 모든 파일의 문자열을 치환하고 `src/<module_name>/` 폴더명까지 바꿉니다.

## 기여 방법

[CONTRIBUTING.md](CONTRIBUTING.md) 를 참고하세요.
