import cv2
import os

def process_video_segment(input_path, trails=False, passing_lanes=False, zones=False,
                          segment_mode=False, start_min=0, end_min=None):

    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(3))
    height = int(cap.get(4))
    duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps

    # Segment trimming
    if segment_mode and end_min:
        start_frame = int(start_min * 60 * fps)
        end_frame = int(end_min * 60 * fps)
    else:
        start_frame = 0
        end_frame = int(duration * fps)

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    output_path = os.path.join("outputs/videos", f"processed_segment_{start_min}-{end_min}.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    current_frame = start_frame

    while cap.isOpened() and current_frame < end_frame:
        ret, frame = cap.read()
        if not ret:
            break

        if trails:
            cv2.putText(frame, f"Overlay: Trails", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        if passing_lanes:
            cv2.putText(frame, f"Overlay: Passing Lanes", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        if zones:
            cv2.putText(frame, f"Overlay: Tactical Zones", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        out.write(frame)
        current_frame += 1

    cap.release()
    out.release()
    return output_path

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
