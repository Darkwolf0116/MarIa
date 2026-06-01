.PHONY: run install add lock clean

run:
	uv run python -m streamlit run app.py

install:
	uv sync

add:
	uv add $(pkg)

lock:
	uv lock

clean:
	rm -rf __pycache__/
	rm -rf .venv/
	rm -f uv.lock
