# selenium-baseline

Loosely based on the Screenplay pattern - tests decoupled -> tasks (interactions) decoupled -> pages decoupled. Includes logging and screenshots on failure.

### Usage

Docker will need to be running.

```sh
make build   		# Build the dev container with pytest, selenium, chromium etc
make shell   		# Open a shell in the container
pytest tests/ -v -s # Run the tests, -s shows live task logs
```

Or run commands directly:

```sh
docker compose run --rm dev python -m pytest tests/ -v -s   # -s shows live task logs
```

#### What's inside

- Python 3.13 on Debian Bookworm
- uv for package management
- Selenium, pytest, and Chromium pre-installed

#### ToDo

- [ ] Parallel tests
- [ ] Jenkins pipeline