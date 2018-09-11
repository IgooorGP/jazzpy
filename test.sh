# ---------------------------------
# Main shell file to run tests.
# ---------------------------------

# runs nosetests with watch-dog
exec nosetests --with-watch --with-coverage --cover-package=. --cover-erase