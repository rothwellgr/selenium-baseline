.PHONY: build shell clean

build:
	docker compose build

shell:
	docker compose run --rm dev

clean:
	docker compose down --rmi all -v 2>/dev/null || true
