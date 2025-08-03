FROM python:3.11

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies using uv
RUN uv pip install --system --no-deps .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
