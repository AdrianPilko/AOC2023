#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>


//std::string filenameStr = "14test.txt";
std::string filenameStr = "14.txt";


typedef std::vector<char> t_vectorLine;
typedef std::vector<t_vectorLine> t_inputData;

bool getLineFromFile(std::ifstream & fileStream, std::string &retLine ) 
{ 
	if (fileStream.is_open()) 
	{
		if (std::getline(fileStream, retLine)) 
		{
			//std::cout << "got line " << retLine << std::endl;
			return true;
		}     
	}
	else 
	{
		std::cerr << "Unable to open file" << std::endl;      
	}
	return false;
}

// use this to size the 2dimension array
// slight bit inefficient reading file twice, but the real data has all different line lengths!
void getLongestLine(int & longest, int & numLines)
{
	longest = 0;
	std::ifstream inputFile(filenameStr.c_str()); // Replace "filename.txt" with your file's name

	std::string line;

	bool gotLine = getLineFromFile(inputFile, line);


	while (gotLine)
	{    
		int temp = line.size();
		if (gotLine) 
		{  
			numLines++;
			///std::cout << "found " << numLines << " so far" << std::endl;
		}   
		if (gotLine && temp > longest) 
		{
			longest = temp;
			//std::cout << "found longest so far line=" <<longest << std::endl;
		}

		gotLine = getLineFromFile(inputFile, line);
	}
	inputFile.close();
}

void printMatrix(t_inputData & dataPtr)
{
	int rows, cols;
	rows = dataPtr.size();
	cols = dataPtr[0].size();
	std::cout << "rows=" << rows << " cols=" << cols << std::endl;
	std::cout << "      "; 
	for (int i = 0; (i < 10); i++)
	{
		std::cout << i;
	}
	for (int i = 10; (i < cols); i++)
	{
		std::cout << i/10;
	}
	std::cout << std::endl;
	for (int i = 0; i < cols; i++)
	{
		if (i > 9) std::cout << i%10;
	}

	for (int r = 0; r < rows; r++)
	{
		std::cout << "row " << r << " ";
		for (int c = 0; c < cols; c++)
		{
			std::cout << dataPtr[r][c];
		}
		std::cout << std::endl;
	}
}



int main()
{
	std::cout << " entering main " << std::endl;

	t_inputData inputData; 

	std::ifstream inputFile(filenameStr.c_str()); // Replace "filename.txt" with your file's name

	// populate jumpTable from the rest 
	int lineNum = 0;
	std::string line;

	while (getLineFromFile(inputFile, line))
	{
		t_vectorLine lineData;

		for (int c = 0; c < line.size(); c++)
		{
			lineData.push_back(line[c]);  
		}
		inputData.push_back(lineData);
		lineNum++;
	}

	inputFile.close(); // Close the file when done reading

	printMatrix(inputData);

	int total = 0;
	int rows, cols;
	rows = inputData.size();
	cols = inputData[0].size();
	// now just bubble the O to top stopping if # is at row -1
	for (int c = 0; c < cols;c++)
	{
		std::vector<char> sortedCol;
		int countO = 0;
		int countDot = 0;

		for (int r = 0; r < rows; r++)
		{
			// this:
			// "0.000..#...0...##.00..#"
			// becomes:
			// "OOOO...#O......##OO...#"
			if (inputData[r][c] == 'O')
			{
				countO++;
			}
			else if (inputData[r][c] == '.')
			{
				countDot++;
			}
			if (inputData[r][c] == '#')
			{
				for (int i = 0; i < countO; i++)
				{
					sortedCol.push_back('O');
				}

				for (int i = 0; i < countDot; i++)
				{
					sortedCol.push_back('.');
				}
				sortedCol.push_back('#');
				countDot = 0;
				countO = 0;
			}
		}
		for (int i = 0; i < countO; i++)
		{
			sortedCol.push_back('O');
		}

		for (int i = 0; i < countDot; i++)
		{
			sortedCol.push_back('.');
		}

		std::cout << "col " << c << " ";
		for (int i = 0; i < sortedCol.size(); i++)
		{
			std::cout << sortedCol[i];
		}
		std::cout << std::endl;

		for (int i = 0; i < sortedCol.size(); i++)
		{
		    if (sortedCol[i] == 'O')
		    {
			   total += sortedCol.size() - i ;
		    }     
		}

	}
	std::cout << "total = " << total << std::endl;
	return 0;
}
