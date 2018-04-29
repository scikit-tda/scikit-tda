# make gh-pages in repo base directory to automatically build and deploy documents to github

gh-pages:
	# first, update all the projects
	echo "Update all submodules"
	cd libraries/kepler-mapper; git pull origin master
	cd libraries/persim; git pull origin master
	cd libraries/ripser; git pull origin master
	cd libraries/umap; git pull origin master
	git add libraries
	git commit -m "update submodules"; git push origin master

	echo "Make gh-pages"

	echo "get up-to-date source from submodules"
	git submodule update --recursive

	#rm libraries/kepler-mapper/index.html
	cd docs; make html

	echo "Go to gh-pages"
	git checkout gh-pages

	echo "Remove old dirs"
	rm -rf _sources _static _modules libraries

	echo "Move new html"
	mv -fv docs/_build/html/* .

	echo "Remove built docs"
	rm -rf docs

	echo "Add to git"
	git add -A

	echo "commit and deploy"
	git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout master
