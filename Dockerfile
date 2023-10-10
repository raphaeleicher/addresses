FROM docker.io/library/unit:1.31.0-python3.11 as base
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1


FROM base as builder
WORKDIR /app
RUN pip install poetry==1.6.1 && \
    touch README.md
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache
COPY pyproject.toml poetry.lock ./
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --only main --no-root


FROM base as runtime
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"
WORKDIR /app/code
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
ADD ./django_project/ /app/code/
RUN chown -R unit:unit /app/code && \
    python manage.py collectstatic --clear --noinput
COPY ./unit.json /docker-entrypoint.d/config.json

# port used by the listener in config.json
EXPOSE 8080
