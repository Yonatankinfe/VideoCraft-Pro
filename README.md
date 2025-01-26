# VideoCraft-Pro
🎥📈 Automated video presentation generator with dynamic charts, voiceovers, and title screens - perfect for data storytelling!

---

## Description  
An end-to-end Python pipeline for creating professional video presentations complete with animated visualizations and synthetic voiceovers. Combines data visualization, text-to-speech, and video editing capabilities.

```python
# Key Features
- Custom title screen generation
- Animated matplotlib chart sequences
- pyttsx3 text-to-speech integration
- OpenCV video composition
- FFmpeg audio/video mixing
- User-friendly CLI interface
```
---

## README.md

# 📂 VideoCraft-Pro

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-opencv%20|%20matplotlib%20|%20pyttsx3-orange)

Automated video production system for data-driven presentations.

## 🚀 Overview
Creates polished videos in 4 stages:
1. **Title Screen** - Customizable intro frame
2. **Chart Animation** - Data visualization timeline
3. **Voiceover** - AI-generated narration
4. **Video Composition** - Combines elements with audio sync

## 🛠️ Installation
```bash
git clone https://github.com/Yonatankinfe/VideoCraft-Pro.git
cd VideoCraft-Pro
pip install -r requirements.txt
sudo apt-get install ffmpeg  # Required for audio mixing
```

## 📋 Requirements File
```text
opencv-python==4.9.0.80
matplotlib==3.8.2
pyttsx3==2.71
numpy==1.26.3
```

## 🖥️ Usage
```bash
python video_pipeline.py
```
Interactive prompt will request:
```python
Title: "Ethiopian Economic Trends"          # Max 50 characters
Description: "2000-2020 GDP Growth Analysis" # Short summary
```

## 📊 Output Structure
```
/output
  ├── title_screen.mp4       # Intro animation
  ├── chart_animation.mp4    # Data visualization
  ├── voiceover.mp3          # Generated narration
  └── final_video.mp4        # Complete presentation
```

## ⚙️ Technical Components

### Chart Animation Engine
```python
# Customizable parameters
years = np.arange(2000, 2021)              # X-axis range
gdp = np.cumsum(np.random.uniform(-1, 5))  # Mock data generator
fps = 2                                    # Animation speed
```

### Voiceover System
```python
engine = pyttsx3.init()
# Adjust voice properties
engine.setProperty('rate', 150)    # Speech speed (words/minute)
engine.setProperty('volume', 0.9)  # Output volume
```

### Video Composition
- Title screen duration: 5 seconds
- 720p resolution (1280x720)
- MP4 format with AAC audio

## 💡 Customization Guide

### Modify Chart Style
```python
ax.plot(years[:frame], gdp[:frame], color="green", ls="--")  # Change color/linestyle
ax.grid(True)  # Add gridlines
```

### Add Custom Data
Replace mock data generation with:
```python
import pandas as pd
real_data = pd.read_csv("your_data.csv")
years = real_data['year'].values
gdp = real_data['gdp'].values
```

### Enhance Title Screen
```python
# Add additional text elements
cv2.putText(frame, "Created by Your Name", (50, 600), font, 0.8, (255,255,255), 2)
```

## ⚠️ Important Notes
1. Requires ffmpeg for audio/video mixing
2. First run may take 2-3 minutes (voice engine initialization)
3. Video resolution fixed at 720p (change width/height in code)
4. Ensure console has write permissions for output directory

## 🌟 Future Roadmap
- [ ] Add multiple chart types (bar, pie, scatter)
- [ ] Implement background music support
- [ ] Create GUI interface
- [ ] Add subtitle generation

## 🤝 Contributing
1. Install dev requirements:
```bash
pip install pytest moviepy
```
2. Run tests:
```bash
python -m pytest test_video_pipeline.py
```
3. Submit PR with descriptive commit messages

## 📜 License
MIT License - see [LICENSE](LICENSE) for details
```
