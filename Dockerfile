# Step 1: Python Base Image
FROM python:3.11-slim

# Step 2: System dependencies (ffmpeg aur git)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Step 3: Working directory setup
WORKDIR /app

# Step 4: Requirements install karna
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Baaki code copy karna
COPY . .

# Step 6: Render ke port ka jhanjhat khatam karne ke liye fake server command
# Yeh command ek chota sa web server 8080 par chalayegi AUR saath me aapka bot bhi shuru kar degi
CMD python3 -m http.server 8080 & python3 -m bot

