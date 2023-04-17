all: main.cpp
	g++ bucketsort.cpp -o bucketsort -std=c++11 -fopenmp
	touch results.csv
	./schunk.sh
clean:
	rm -f bucketsort
	rm -f results.csv