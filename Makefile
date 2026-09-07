.PHONY: format

# Format all markdown files in the project
format:
	npx prettier --write "**/*.md"
