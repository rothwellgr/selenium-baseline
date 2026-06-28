FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    unzip \
    git \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

ENV UV_PROJECT_ENVIRONMENT=/usr/local \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY pyproject.toml requirements.txt .

RUN if [ -s requirements.txt ]; then \
        uv add -r requirements.txt && uv sync --no-cache; \
    else \
        uv sync --no-cache; \
    fi

CMD ["bash"]
