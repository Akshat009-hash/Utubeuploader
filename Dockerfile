# Step 1: Base image select karein (Python 3.11 kyunki Pyrogram ispe stable chalta hai)
FROM python:3.11-slim

# Step 2: System dependencies install karein (agar bot mein media, ffmpeg ya git chahiye toh)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Step 3: Working directory set karein
WORKDIR /app

# Step 4: Requirements file copy aur install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Baaki saara bot ka code copy karein
COPY . .

# Step 6: Render ke 'Port Not Detected' error ko bypass karne ke liye dummy port expose karein
ENV PORT=8080
EXPOSE 8080

# Step 7: Bot ko chalane ki command
CMD ["python3", "-m", "bot"]

