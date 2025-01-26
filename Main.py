
import os
import cv2
import numpy as np
import pyttsx3
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_chart_animation(output_path):
    """
    Generates a simple animated chart using OpenCV and saves it as a video.
    """
    # Generate mock data
    years = np.arange(2000, 2021)
    gdp = np.cumsum(np.random.uniform(-1, 5, size=len(years))) + 50

    # Video settings
    fps = 2
    height, width = 720, 1280
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    animation_path = os.path.join(output_path, "chart_animation.mp4")
    out = cv2.VideoWriter(animation_path, fourcc, fps, (width, height))

    # Generate frames
    for frame in range(1, len(years) + 1):
        # Create a plot
        fig, ax = plt.subplots(figsize=(16, 9))
        ax.plot(years[:frame], gdp[:frame], color="blue", lw=2)
        ax.set_xlim(years[0], years[-1])
        ax.set_ylim(min(gdp) - 5, max(gdp) + 5)
        ax.set_xlabel("Year")
        ax.set_ylabel("GDP (in billions)")
        ax.set_title("Ethiopian Economic Trends")
        plt.tight_layout()

        # Convert the plot to an image
        fig.canvas.draw()
        img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        plt.close(fig)

        # Resize and write to video
        img = cv2.resize(img, (width, height))
        out.write(img)

    out.release()
    return animation_path

def create_title_screen(title, description, output_path):
    """
    Creates a title screen video using OpenCV.
    """
    duration = 5
    fps = 24
    height, width = 720, 1280
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    title_path = os.path.join(output_path, "title_screen.mp4")
    out = cv2.VideoWriter(title_path, fourcc, fps, (width, height))

    font = cv2.FONT_HERSHEY_SIMPLEX
    for _ in range(duration * fps):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        cv2.putText(frame, title, (50, 200), font, 2, (255, 255, 255), 3, cv2.LINE_AA)
        cv2.putText(frame, description, (50, 400), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        out.write(frame)

    out.release()
    return title_path

def create_voiceover(text, output_path):
    """
    Generates a voiceover audio file using pyttsx3.
    """
    voiceover_path = os.path.join(output_path, "voiceover.mp3")

    engine.save_to_file(text, voiceover_path)
    engine.runAndWait()
    return voiceover_path

def combine_video(title_path, animation_path, voiceover_path, output_path):
    """
    Combines the title screen, animation, and voiceover into a final video using OpenCV.
    """
    cap1 = cv2.VideoCapture(title_path)
    cap2 = cv2.VideoCapture(animation_path)

    # Get video properties
    fps = int(cap1.get(cv2.CAP_PROP_FPS))
    width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    final_video_path = os.path.join(output_path, "final_video.mp4")
    out = cv2.VideoWriter(final_video_path, fourcc, fps, (width, height))

    # Write title video
    while cap1.isOpened():
        ret, frame = cap1.read()
        if not ret:
            break
        out.write(frame)

    cap1.release()

    # Write animation video
    while cap2.isOpened():
        ret, frame = cap2.read()
        if not ret:
            break
        out.write(frame)

    cap2.release()
    out.release()

    # Add audio using ffmpeg
    os.system(f"ffmpeg -i {final_video_path} -i {voiceover_path} -c:v copy -c:a aac -strict experimental {final_video_path}")
    return final_video_path

def main():
    # Get user input
    title = input("Enter the title of the video: ")
    description = input("Enter a short description of the video: ")

    # Create output directory
    output_path = "output"
    os.makedirs(output_path, exist_ok=True)

    # Step 1: Create title screen
    title_path = create_title_screen(title, description, output_path)

    # Step 2: Generate chart animation
    animation_path = generate_chart_animation(output_path)

    # Step 3: Create voiceover
    voiceover_text = f"Welcome to this video about {title}. {description}."
    voiceover_path = create_voiceover(voiceover_text, output_path)

    # Step 4: Combine everything
    final_video_path = combine_video(title_path, animation_path, voiceover_path, output_path)

    print(f"Video created successfully! Check the output at: {final_video_path}")

if __name__ == "__main__":
    main()
