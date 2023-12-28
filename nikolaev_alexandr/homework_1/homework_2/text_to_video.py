import torch
import streamlit as st
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
import cv2
import base64

# Streamlit app
def main():
    st.title("Оживление текста.")

    # User input
    prompt = st.text_input("Введите текст, чтобы нейросеть сгенерировала короткое видео на его основе.")

    if st.button("Получить ответ") and prompt:

        # Создание DiffusionPipeline
        pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        pipe.enable_model_cpu_offload()

        # Запрос для создания видео
        answer_frames = pipe(prompt, num_inference_steps=25).frames

        # Определение параметров видео
        height, width, _ = answer_frames[0].shape
        fps = 8  # Например, можно использовать 30 кадров в секунду

        # Создание объекта VideoWriter с кодеком H264
        fourcc = cv2.VideoWriter_fourcc(*'H264')
        video_path = 'output_video.mp4'
        video_writer = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

        # Запись кадров в видеофайл
        for frame in answer_frames:
            video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))  # OpenCV требует BGR формат

        # Закрытие объекта VideoWriter
        video_writer.release()

        # Display the answer
        if video_path:
            st.subheader("Результат:")
            st.video(video_path)

            # Button to download the video
            with open(video_path, "rb") as video_file:
                video_bytes = video_file.read()
            st.download_button(
                label="Скачать видео",
                data=video_bytes,
                file_name="output_video.mp4",
                mime="video/mp4"
            )

if __name__ == "__main__":
    main()