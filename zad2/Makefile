all: main.cpp
	g++ main.cpp -o main -std=c++11 -fopenmp
	touch results.csv
	./schunk.sh
clean:
	rm -f main
	rm -f results.csv