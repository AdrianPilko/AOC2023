#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>



/* 
.....
.S-7.
.|.|.
.L-J.
..... 
*/

std::string filenameStr = "8.txt";

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
   std::ifstream inputFile(filenameStr.c_str()); // Replace "filename.txt" with your file's name
   
   std::string line;
   
   while (bool gotLine = getLineFromFile(inputFile, line))
   {    
     int temp = line.size();
     if (gotLine) numLines++;
     if (gotLine && temp > longest) longest = temp;
   
   }
   inputFile.close();
}

main()
{
  int longestLine;
  int numLines;
  getLongestLine(longestLine, numLines);

  std::vector<std::vector<char>> data(numLines, std::vector<char>(longestLine));

  for (int l = 0; l  < numLines; l++)
  {
    for (int c = 0; c < longestLine; c++)
    {
      data[l][c] = '.';  // prepoulate all with '.', the real data has all different line lengths
    }
  }
  
  std::ifstream inputFile(filenameStr.c_str()); // Replace "filename.txt" with your file's name
  std::string line;
  int rowS = 0;
  int colS = 0;
   
  // populate jumpTable from the rest 
  int lineNum = 0;
  while (getLineFromFile(inputFile, line))
  {
    for (int c = 0; c < longestLine; c++)
    {
      data[lineNum][c] = line[c];  // prepoulate all with '.', the real data has all different line lengths
      if (data[lineNum][c] == 'S')
      {
         rowS = lineNum;
         colS = c;
      }
    }    
    lineNum++;
  }
  std::cout << "found  S at (row, col) = (" << rowS << "," << colS << ")" << std::endl;

  inputFile.close(); // Close the file when done reading
  
  std::system("pause");
  return 0;
}