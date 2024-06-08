
## Переменные окружения

```dotenv
YOUTUBE_VIDEO="https://www.youtube.com/watch?v=NdSqAAT28v0" // ссылка на видео
EVERY_VIDEO_FRAME="3" // будет браться каждый 3 кадр
VIDEO_PATH="video" // путь видео в проекте
VIDEO_NAME="dance.mp4" //название видеофайла 
IMAGES_PATH="images" // путь к изображениям
```

## Шаги запуска

1. Необходимо выполнить youtube-downloader. Он скачает видео в папке с Youtube
2. Необходимо выполнить video-to-images. Он создаст датасет из картинок
3. Необходимо выполнить autoencoder-v2. Он обучит autoencoder
4. Необходимо выполнить rnn. Он обучит rnn и запишет видео
