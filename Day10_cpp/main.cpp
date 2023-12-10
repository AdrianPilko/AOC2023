#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>


std::string filenameStr = "8test.txt";
//std::string filenameStr = "8.txt";

/* 
.....
.S-7.
.|.|.
.L-J.
..... 
*/

typedef enum e_directnV {eup = 0,edown, eleft, eright} t_directn; 

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

bool isValidDirection(t_directn di, char theNextSymbol)
{
  bool rv = false;
  switch (theNextSymbol)
  {
    case '|' : if ((di == eup) || (di == edown)) rv = true;     break;
    case '-' : if ((di == eleft) || (di == eright)) rv = true; break;
    case '7' : if ((di == eleft) || (di == edown)) rv = true; break;
    case 'J' : if ((di == eleft) || (di == eup)) rv = true; break;
    case 'F' : if ((di == eright) || (di == edown)) rv = true; break;
    case 'L' : if ((di == eright) || (di == edown)) rv = true; break;
    case 'S' : // should never happen but catch just in case
              std::cout <<"got back to starting position!" << std::endl; rv = false; break;
    default: rv = false;  break;
    break;
  };    
  return rv;
}

main()
{
  std::cout << " entering main " << std::endl;
  
  int longestLine;
  int numLines;
  
  getLongestLine(longestLine, numLines);

  std::cout << " got dimensions rows=" << numLines << " cols=" << longestLine << std::endl;

  std::vector<std::vector<char>> data(numLines, std::vector<char>(longestLine));

  for (int l = 0; l  < numLines; l++)
  {
    for (int c = 0; c < longestLine; c++)
    {
      data[l][c] = '.';  // prepoulate all with '.', the real data has all different line lengths
    }
  }
  
  std::cout << " populated vector " << std::endl;
  
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
  
  // starting at rowS, ColS navigate the vector until can't go any further
  
  // choose a starting direction
  t_directn currentDir;
  t_directn lastDir;
  char nextChar;
  int row = rowS;
  int col = colS;
  
  int nextRow = 0;
  int nextCol = 0;
  
  int triedEveryDirection = 0;
  currentDir = eup;
  lastDir = eleft;
  
  std::cout << " before while loop , currentDir=" << currentDir << ", last=" << lastDir << std::endl;
  
  while (lastDir != currentDir)
  {
    if ((currentDir == eleft) && (col > 0)) 
    { 
      nextChar = data[row][col-1]; 
      nextRow = row; 
      nextCol = col-1; 
      std::cout << " trying left,";
    }  
    if ((currentDir == eright) && (col < longestLine-1))
    { 
      nextChar = data[row][col+1];
      nextRow = row; 
      nextCol = col+1;
      std::cout << " trying right,";
    } 
    if ((currentDir == eup) && (row > 0)) 
    { 
      nextChar = data[row-1][col];
      nextRow = row-1; 
      nextCol = col;
      std::cout << " trying up,";
    }  
    if ((currentDir == edown) && (row < numLines-1)) {
      nextChar = data[row+1][col];
      nextRow = row+1; 
      nextCol = col;    
      std::cout << " trying down,";
    }  
    
    if (isValidDirection(currentDir, nextChar))
    {
      std::cout << "valid from " << row << "," << col << " " ;
      row = nextRow;
      col = nextCol;
      std::cout << "to " << row << "," << col << std::endl;
      triedEveryDirection = 0;
      currentDir = (t_directn)triedEveryDirection;
    }
    else
    {
      std::cout << " not valid from " << row << "," << col << " to " << nextRow << "," << nextCol << std::endl;      
      triedEveryDirection++;
      
      if (triedEveryDirection <= 3)
      {
          currentDir = (t_directn)triedEveryDirection;        
      }
      else
      {
        triedEveryDirection = 0;
        lastDir = currentDir;
        currentDir = (t_directn)triedEveryDirection;
      }
    }
    std::cout << " pause, press return" << std::endl;
    std::system("pause");
  }
  std::cout << " pause, press return" << std::endl;
  std::system("pause");
  return 0;
}