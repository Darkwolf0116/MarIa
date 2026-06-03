.PHONY: run ruleta install add lock clean

run:
	uv run python -m streamlit run app.py

ruleta:
	uv run python -m streamlit run ruleta.py

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
