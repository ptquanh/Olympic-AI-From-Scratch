.PHONY: format

# Format tất cả các file markdown trong dự án
format:
	npx prettier --write "**/*.md"
