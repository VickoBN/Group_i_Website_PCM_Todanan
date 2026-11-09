FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PATH=/app/.venv/bin:$PATH

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY . .
RUN uv sync --frozen --no-dev

RUN SECRET_KEY=hanya-untuk-build DEBUG=False python manage.py collectstatic --noinput

RUN useradd --create-home --uid 1000 appuser && mkdir -p /app/media && chmod +x docker-entrypoint.sh && chown -R appuser:appuser /app
USER appuser

ENV UV_NO_SYNC=1
ENV PORT=8000
EXPOSE 8000

CMD ./docker-entrypoint.sh