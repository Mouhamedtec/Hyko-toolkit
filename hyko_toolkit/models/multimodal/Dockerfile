FROM hykoai/toolkit-base:latest

RUN --mount=type=cache,target=/root/.cache/pip pip install transformers[torch]
RUN --mount=type=cache,target=/root/.cache/pip pip install accelerate
RUN --mount=type=cache,target=/root/.cache/pip pip install sentencepiece

COPY . .

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "3000", "main:func"]
