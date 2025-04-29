import cv2
import os

def process_video(input_path, trails=False, passing_lanes=False, zones=False):
    # Read input video
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(5)

    output_path = os.path.join("outputs/videos", "processed_" + os.path.basename(input_path))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Simple fake overlays
        if trails:
            cv2.putText(frame, 'Trail Overlay', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        if passing_lanes:
            cv2.putText(frame, 'Passing Lanes', (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        if zones:
            cv2.putText(frame, 'Tactical Zones', (50,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        out.write(frame)

    cap.release()
    out.release()
    return output_path
