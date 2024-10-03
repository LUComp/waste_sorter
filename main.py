from gui.control_panel import ControlPanel
import cv2
import torch

if __name__ == "__main__":      

      device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

      model_d = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
      model_c = torch.load('checkpoints/trash.pth', map_location=device)
      
      cap = cv2.VideoCapture(0)

      panel = ControlPanel("Waste Sorter")

      panel.video_stream(cap, model_d, model_c)

      panel.mainloop()

      # Release the webcam when the window is closed
      cap.release()
      cv2.destroyAllWindows()


