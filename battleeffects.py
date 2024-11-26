from PIL import Image
import os
class BattleEffects:
    def __init__(self, gif_location) -> None:
        self.gif_location = gif_location

    # convert gif file to multiple images/frames
    def animation_frames(self):
        self.frames = []
        gif = Image.open(self.gif_location)
        self.frames_number = gif.n_frames
        self.size = gif.size
        for frame in range(self.frames_number):
            gif.seek(frame)
            frame_image = gif.copy()
            frame_path = (f"./bin/{self.name}frame_{frame}.png")
            frame_image.save(frame_path)
            self.frames.append(frame_path)
        return self.frames
    
    def clear_residue(self):
        for frames in self.frames:
            os.remove(frames)
