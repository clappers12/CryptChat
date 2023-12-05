import cv2
import threading

class VideoHandler:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # 0 is typically the default webcam
        self.is_capturing = False

    def start_capturing(self):
        """Starts video capturing in a separate thread."""
        if not self.is_capturing:
            self.is_capturing = True
            threading.Thread(target=self._capture_loop, daemon=True).start()

    def _capture_loop(self):
        """The loop that captures video frames and displays them."""
        while self.is_capturing:
            ret, frame = self.cap.read()
            if ret:
                cv2.imshow('Video', frame)

                # Break the loop when 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        self.cap.release()
        cv2.destroyAllWindows()

    def stop_capturing(self):
        """Stops the video capturing."""
        self.is_capturing = False

# Example usage
if __name__ == "__main__":
    video_handler = VideoHandler()
    try:
        video_handler.start_capturing()
        input("Capturing video. Press Enter to stop.\n")
    finally:
        video_handler.stop_capturing()
