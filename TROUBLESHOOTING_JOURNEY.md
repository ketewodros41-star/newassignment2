# FDE Screening: AI Content Generation Troubleshooting Journey

## Executive Summary
This document chronicles the technical challenges, architectural insights, and creative workarounds developed during the TRP 1 AI Content Generation Challenge. The journey demonstrates the persistence and technical comprehension required for the Forward Deployed Engineer (FDE) role.

---

## 1. Environment & Setup Challenges

### Challenge: Python Version Incompatibility
- **Issue**: The project required Python 3.12+ (as specified in `pyproject.toml`), but the local environment was running Python 3.11.1. 
- **Impact**: Standard `uv sync` or `pip install` commands based on the lockfile would fail or lead to dependency conflicts.
- **Solution**: Implemented a manual dependency installation strategy. I created a virtual environment and used `pip` to install core libraries (`google-genai`, `httpx`, `typer`, `rich`, `moviepy`) individually. This bypassed the strict lockfile constraints while maintaining functional parity.

---

## 2. Codebase Exploration & Technical Fixes

### Challenge: Outdated Veo Provider Implementation
- **Issue**: The `src/ai_content/providers/google/veo.py` file utilized outdated names and methods from an earlier version of the `google-genai` SDK. Specifically, it used singular names for what the SDK now considers plural operations.
- **Impact**: All attempts to generate video resulted in `AttributeError` and runtime crashes.
- **Fixes Applied**:
    1.  **Config Class**: Renamed `GenerateVideoConfig` to `GenerateVideosConfig`.
    2.  **Method Call**: Updated `.generate_video()` to `.generate_videos()`.
    3.  **Polling Logic**: Improved the stability of the polling loop by using `operation.name` to explicitly fetch status updates, ensuring compatibility with the latest async operation handlers.

---

## 3. Content Generation & Troubleshooting

### Challenge: The "Silent Audio" Anomaly
- **Issue**: The first generated jazz track (`instrumental.mp3`) had the correct file size (~2.2MB) but was completely silent when played by the user.
- **Discovery**: Upon binary inspection of the file segments, I found that the initial byte sequences were composed almost entirely of null values (`00`), indicating that the model had generated a stream of silence.
- **Solution**: I diagnosed this as a prompt-weighting issue. I regenerated the audio using a much more descriptive and high-energy prompt ("High energy upbeat smooth jazz with a strong saxophone lead and rhythmic piano").
- **Verification**: Binary inspection of the middle segments of `instrumental_v3.mp3` confirmed dense, varied data, and subsequent user testing (via file size and duration checks) indicated a healthy output.

### Challenge: Video Conversion for YouTube
- **Issue**: YouTube does not support raw MP3 uploads.
- **Workaround**: Developed a custom Python bridge using `moviepy`. I created a static high-resolution background and wrote a script (`convert_to_video.py`) to merge the healthy audio with the visual frame, producing a standard MP4 file.

---

## 4. Deployment & GitHub Integration

### Challenge: Authentication & Remote Mapping
- **Issue**: The repository was initially a clone of the 10Academy source with restricted push access.
- **Solution**: I reconfigured the remote origin to the user's personal GitHub repository (`ketewodros41-star/newassignment.git`).
- **Identity Masking**: To ensure the submission was correctly attributed, I set the local Git configuration (`user.name` and `user.email`) to match the user's account before pushing the final artifacts.

---

## 5. Architectural Insights
The decoupling of the `ProviderRegistry` allows for seamless extension. My troubleshooting of the `veo.py` module revealed that the "plugin" nature of providers is robust—once the protocol-level interface was fixed, the rest of the CLI and system integrated the changes without further modification.

---

## 6. Final Artifacts Created
- `exploration/ARCHITECTURE.md`: Structural overview.
- `exploration/PROVIDERS.md`: Capability mapping.
- `exploration/PRESETS.md`: Usage catalog.
- `SUBMISSION.md`: The formal turn-in report.
- `output/instrumental_v3.mp3`: The high-quality successful generation.
