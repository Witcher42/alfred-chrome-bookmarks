ALFREDWORKFLOW_NAME=chrome-bookmarks.alfredworkflow

default:
	(cd src/; zip -r ../zip/${ALFREDWORKFLOW_NAME} *; )

test:
	(cd src/; python "main.py" -v "chrome" -c "get.bookmarks" -q "search";)

install:
	open zip/${ALFREDWORKFLOW_NAME}
