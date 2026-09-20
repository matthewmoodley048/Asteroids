# Asteroids

A simple 2D arcade game where you pilot a spaceship and survive an asteroid storm by shooting.

## Requirements

- [uv](https://docs.astral.sh/uv/) (`brew install uv` on macOS)

uv will download Python 3.13 automatically if you don't have it.

## Setup and Running

```
uv sync
cd src
uv run -m main
```

`uv sync` creates a virtual environment and installs all dependencies (such as pygame).

## Codebase Overview

All code lives in `src/`. To tweak game behavior (player speed, screen width, asteroid size, etc.), edit the constants there.

| File               | Responsibility                                                 |
| ------------------ | -------------------------------------------------------------- |
| `asteroid.py`      | A single asteroid: spawning, destroying, splitting             |
| `asteroidfield.py` | The spawn area for asteroids, plus their shape and size        |
| `circleshape.py`   | Base class used for collision detection (player and asteroids) |
| `main.py`          | Entry point: sets up the window, player, and asteroids         |
| `player.py`        | Player movement, rotation, and shooting input                  |
| `shooting.py`      | Bullet movement and rendering                                  |
