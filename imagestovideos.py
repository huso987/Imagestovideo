import cv2
import os

def resimden_video(image_folder, video_adi, hiz):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()  #dosyalari siralama

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = frame.shape

    video = cv2.VideoWriter(video_adi, cv2.VideoWriter_fourcc(*'mp4v'), hiz, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
    image_folder = "/home/huseyin/Pictures/eski"  # Fotograf klasoru
    video_adi = "output_video.mp4"  # video dosya adi
    hiz = 30  # Video hizi

    resimden_video(image_folder, video_adi, hiz)
