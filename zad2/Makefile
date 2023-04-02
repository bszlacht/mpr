all:
	g++ main.cpp -o main -std=c++11 -fopenmp
	touch results.csv
	./sc.sh
clean:
	rm -f main
	rm -f sc.sh