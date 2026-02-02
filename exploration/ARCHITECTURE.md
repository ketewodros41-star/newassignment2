# Codebase Architecture

## Main Modules in `src/ai_content/`
- `core/`: Defines the foundational protocols (`MusicProvider`, `VideoProvider`), registries, and result objects.
- `config/`: Manages configuration using Pydantic, handling environment variables and settings.
- `providers/`: Contains specific implementations for different AI services (Google, AIMLAPI).
- `presets/`: Stores pre-configured style dictionaries for music and video generation.
- `pipelines/`: Orchestrates multi-step workflows (e.g., source selection -> generation -> post-processing).
- `cli/`: Implements the Typer-based command-line interface.

## Provider Organization
Providers are organized by service name (e.g., `google`, `aimlapi`) within the `providers/` directory. Each service directory contains modules for specific capabilities (e.g., `lyria.py`, `veo.py`). They register themselves with the `ProviderRegistry` using decorators like `@ProviderRegistry.register_music`.

## Purpose of `pipelines/`
The `pipelines/` directory is intended for complex, multi-step orchestration. While the basic CLI commands use providers directly, the pipeline layer allows for chaining operations, such as fetching metadata from Archive.org, generating music and video in parallel, and merging them with FFmpeg.
