#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>


//std::string filenameStr = "in.txt";
std::string filenameStr = "intest.txt";

/* 
   .|...\....
   |.-.\.....
   .....|-...
   ........|.
   ..........
   .........\
   ..../.\\..
   .-.-/..|..
   .|....-|.\
   ..//.|....
 */

typedef enum e_directnV {eup = 0,edown, eleft, eright, eupAndDownSplit, eLeftAndRightSplit, enotValid} t_directn; 

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
        case eupAndDownSplit:
            os << "up and down split";
            break;
        case eLeftAndRightSplit:
            os << "left and right split";
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
    bool rv = true;
#if 0
    bool rv = false;
    switch (theNextSymbol)
    {
        case '|' : if ((di == eup) || (di == edown)) rv = true;     break;
        case '-' : if ((di == eleft) || (di == eright)) rv = true; break;
        case '/' : if ((di == eleft) || (di == edown)) rv = true; break;
                       // to display a "\" you have to "escape" it with double slash
        case '\\' : if ((di == eleft) || (di == eup)) rv = true; break;
        case '.' : if ((di == eright) || (di == edown)) rv = true; break;
        default: rv = false;  break;
                 break;
    };
#endif    
    return rv;
}

t_directn theNextValidDirection(t_directn currentDir, char theNextSymbol)
{
    t_directn rv;

    switch (theNextSymbol)
    {
        case '|' :  // beam splitter vertical type
            if (currentDir == edown) 
            {
                rv = edown;   
            }	
            else if (currentDir == eup)
            {
                rv = eup;
            }
            else if (currentDir == eleft)
            {
                rv = eupAndDownSplit;
            }
            else if (currentDir == eright)
            {
                rv = eupAndDownSplit;
            }
            std::cout << "beam splitter vert" << std::endl;
            break;
        case '-' :  // beam splitter horizontal type 
            if (currentDir == edown) 
            {
                rv = eLeftAndRightSplit;   
            }	
            else if (currentDir == eup)
            {
                rv = eLeftAndRightSplit;
            }
            else if (currentDir == eleft)
            {
                rv = eleft;
            }
            else if (currentDir == eright)
            {
                rv = eright;
            }
            std::cout << "beam splitter horiz" << std::endl;
            break;
        case '/' :  // mirror type 1
            if (currentDir == eup) rv = eright;     
            else if (currentDir == edown) rv = eleft;     
            else if (currentDir == eleft) rv = eup;     
            else if (currentDir == eright) rv = edown;   
            else rv = enotValid;  
            break;
            // to display a "\" you have to "escape" it with double slash                
        case '\\' :  // mirror type 2
            if (currentDir == eup) rv = eleft;     
            else if (currentDir == edown) rv = eright;     
            else if (currentDir == eleft) rv = eup;     
            else if (currentDir == eright) rv = edown;   
            else rv = enotValid;  
            break;

        case '.' :   // rule requires we continue in same direction                
            rv = currentDir;     
            break;
        default: rv = enotValid;  break;
                 break;
    };    
    return rv;
}


int main()
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

    std::cout << "vector pre-populated to handle unequal line lengths" << std::endl;

    std::ifstream inputFile(filenameStr.c_str()); // Replace "filename.txt" with your file's name
    std::string line;
    int rowS = 0;   /// top left is the start point
    int colS = 0;

    // populate jumpTable from the rest 
    int lineNum = 0;
    while (getLineFromFile(inputFile, line))
    {
        for (int c = 0; c < longestLine; c++)
        {
            data[lineNum][c] = line[c];  // prepoulate all with '.', the real data has all different line lengths 
        }    
        lineNum++;
    }
    std::cout << "found  S at (row, col) = (" << rowS << "," << colS << ")" << std::endl;

    inputFile.close(); // Close the file when done reading

    // starting at rowS, ColS navigate the vector until can't go any further

    // choose a starting direction
    t_directn currentDir = eright;  
    int row = rowS;
    int col = colS;
    int hops = 0; 
    int result = 0;

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
                case eupAndDownSplit: std::cout << "SPLIT up and down" << std::endl;  break;
                case eLeftAndRightSplit: std::cout << "SPLIT left and right" << std::endl; break;
            };
            std::cout << " WAS valid, currentDir=" << currentDir <<", row=" << row << " col=" << col << std::endl;  
            hops++;
            if (col < 0 || col >= longestLine || row < 0 || row >= numLines)
            {
                std::cout << "hit edge HALT!" << std::endl;
                currentDir = enotValid;
                result = (float) hops / 2.0;
            }
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
    //  std::system("pause");
    return 0;
}
