FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsndfile1 \
        ffmpeg \
            espeak-ng \
                && rm -rf /var/lib/apt/lists/*

                # Install TTS
                RUN pip install --no-cache-dir TTS flask flask-cors

                # Copy server files
                COPY server/ /app/server/

                # Expose port
                EXPOSE 5002

                # Set environment variable for port (Railway uses PORT)
                ENV PORT=5002

                # Run the server
                CMD python /app/server/app.py --port $PORT
