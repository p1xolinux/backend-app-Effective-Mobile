FROM python:3.11-alpine

WORKDIR /app

COPY app.py .

# не root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]