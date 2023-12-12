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

typedef enum e_directnV {eup = 0,edown, eleft, eright, enotValid} t_directn; 

// Overload the << operator for Direction enum
std::ostream& operator<<(std::ostream& os, const e_directnV& dir) {
    switch (dir) {
        case eup:
            os << "up";
            break;
        case edown:
            os << "down";
            break;
        case eleft:
            os << "left";
            break;
        case eright:
            os << "right";
            break;
        case enotValid:
        default:
            os << "Invalid direction";
            break;
    }
    return os;
}

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
    case 'L' : if ((di == eright) || (di == eup)) rv = true; break;
    case 'S' : // should never happen but catch just in case
              std::cout <<"got back to starting position!" << std::endl; rv = false; break;
    default: rv = false;  break;
    break;
  };    
  return rv;
}

t_directn theNextValidDirection(t_directn currentDir, char theNextSymbol)
{
  t_directn rv;
  
  switch (theNextSymbol)
  {
    case '|' : 
                if (currentDir == edown) rv = edown;     
                else rv = eup;     
                break;
    case '-' : 
                if (currentDir == eleft) rv = eleft;     
                else rv = eright;     
                break;
    case '7' : 
                if (currentDir == eup) rv = eleft;     
                else  rv = edown;     
                break;
    case 'J' : 
                if (currentDir == eright) rv = eup;     
                else  rv = eleft;     
                break;
    case 'F' : 
                if (currentDir == eup) rv = eright;     
                else rv = edown;     
                break;
    case 'L' : 
                if (currentDir == edown) rv = eright;     
                else rv = eup;     
                break;
    case 'S' : // should never happen but catch just in case
              std::cout <<"got back to starting position!" << std::endl; rv = enotValid; break;
    default: rv = enotValid;  break;
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
  int row = rowS;
  int col = colS;
  int hops = 0; 
  int result = 0;
  
  std::cout << " BEFORE START currentDir=" << currentDir << ", row=" << row << " col=" << col << std::endl;
  
  // work out what the first valid direction is form S
  bool validDir = false; 

  if (isValidDirection(eup, data[row-1][col]))
  {
     currentDir = eup;
     row = row-1; 
  }
  else if (isValidDirection(edown, data[row+1][col]))
  {
     currentDir = edown;
     row = row+1; 
  }
  else if (isValidDirection(eleft, data[row][col-1]))
  {
     currentDir = eleft;
     col = col-1;      
  }  
  else if (isValidDirection(eright, data[rowS][colS+1]))
  {
     currentDir = eright;
     col = col+1;      
  }
  std::cout << " currentDir=" << currentDir << ", row=" << row << " col=" << col << std::endl;  

  while (enotValid != currentDir)
  {
    currentDir = theNextValidDirection(currentDir, data[row][col]);
    
    if (isValidDirection(currentDir, data[row][col]))
    {
       switch (currentDir)
       {
         case eup : row = row - 1; break;
         case edown : row = row + 1; break;
         case eleft : col = col - 1; break;
         case eright : col = col + 1; break;
       };
       std::cout << " WAS valid, currentDir=" << currentDir <<", row=" << row << " col=" << col << std::endl;  
       hops++;
    }
    else
    {
      std::cout << " not valid, currentDir=" << currentDir <<", row=" << row << " col=" << col << std::endl;  
      currentDir = enotValid;
      result = (float) hops / 2.0;
    }  
  }
  std::cout << "hops = " << hops << " result = " << result+1 << std::endl;
  std::cout << " pause, press return" << std::endl;
  std::system("pause");
  return 0;
}