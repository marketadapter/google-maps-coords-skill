---
name: google-maps-coords
description: 구글 지도 URL에서 위도(lat)·경도(lng)를 추출한다. 단축 URL·iframe 임베드·일반 장소 URL 모두 처리.
allowed-tools: Bash
---

# google-maps-coords

구글 지도 공유 URL에서 위도(lat)와 경도(lng)를 추출한다.

## 실행 방법

사용자가 구글 지도 URL을 제공하면 이 SKILL.md와 같은 디렉토리에 있는 extract.py를 실행한다.

**Claude Code** (`~/.claude/skills/google-maps-coords/`에 설치된 경우):

```bash
python3 ~/.claude/skills/google-maps-coords/extract.py "<URL>"
```

**Codex** (`~/.agents/skills/google-maps-coords/`에 설치된 경우):

```bash
python3 ~/.agents/skills/google-maps-coords/extract.py "<URL>"
```

URL이 여러 개면 각각 실행한다.

## 결과 출력 형식

```
위도 (lat): 37.123456
경도 (lng): 127.123456
```

## 지원 URL 형식

| 형식 | 예시 |
|---|---|
| 단축 URL | `https://maps.app.goo.gl/XXXXX` |
| 장소 URL | `https://www.google.com/maps/place/.../@lat,lng,zoom/` |
| 검색 URL | `https://www.google.com/maps?q=lat,lng` |
| iframe 임베드 URL | `https://www.google.com/maps/embed?pb=...!2d<lng>!3d<lat>...` |
| data= URL | `https://www.google.com/maps/place/NAME/data=...!3d<lat>!4d<lng>...` |

단축 URL은 HTTP 리다이렉트를 따라가며, 나머지는 네트워크 요청 없이 로컬 파싱한다.
