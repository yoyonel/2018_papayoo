RM = rm -rf

all: docker-build

wheel:
	@echo "Building python project..."
	@python setup.py bdist_wheel

re: fclean all

pytest:
	pytest ${PYTEST_OPTIONS}

default: docker
