# Style Presets

## Music Presets
| Preset | Style/Mood | BPM |
|--------|------------|-----|
| `jazz` | Smooth jazz fusion | 95 |
| `blues` | Delta blues | 72 |
| `ethiopian-jazz` | Ethio-jazz fusion | 85 |
| `cinematic` | Epic orchestral | 100 |
| `electronic` | Progressive house | 128 |
| `ambient` | Atmospheric pads | 60 |
| `lofi` | Lo-fi hip-hop | 85 |
| `rnb` | Contemporary R&B | 90 |

## Video Presets
| Preset | Style/Mood | Aspect Ratio |
|--------|------------|--------------|
| `nature` | Wildlife documentary | 16:9 |
| `urban` | Cyberpunk cityscape | 16:9 |
| `space` | Astronaut/sci-fi | 16:9 |
| `abstract` | Liquid metal/geometric | 1:1 |
| `ocean` | Underwater scenes | 16:9 |
| `fantasy` | Dragons/epic fantasy | 16:9 |
| `portrait` | Fashion/beauty | 9:16 |

## Adding a New Preset
To add a new preset, you would:
1. Modify the relevant dictionary in `src/ai_content/presets/music.py` or `src/ai_content/presets/video.py`.
2. Add a new entry with the desired prompt, BPM (for music), or aspect ratio (for video).
3. The CLI will automatically pick up the new preset on the next run.
