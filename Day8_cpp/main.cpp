#include <iostream>
#include <string>
#include <fstream>
#include <map>

// get it working without reading form file first
/* char * testData = "LLR\n" \
                  "AAA = (BBB, BBB)\n"\
                  "BBB = (AAA, ZZZ)\n"\
                  "ZZZ = (ZZZ, ZZZ)\0" */



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

typedef struct  s_LRJumpTableEntry
{
  std::array<std::string, 2> LRJumpCode;
  
} t_LRJumpTableEntry;
 std::map<std::string, t_LRJumpTableEntry> jumpTable; 
main()
{
  std::string filename = "8.txt";
  std::ifstream inputFile(filename.c_str()); // Replace "filename.txt" with your file's name
  std::string line;
  std::string LRCodes;
  std::map<std::string, t_LRJumpTableEntry> jumpTable; 
  
  //populate LRCodes from first line
  getLineFromFile(inputFile, LRCodes);
  // next line is always blank
  getLineFromFile(inputFile, line);
   
  // populate jumpTable from the rest 
  while (getLineFromFile(inputFile, line))
  {
    // chop up the code line into the key then the LR bit
    std::string key = line.substr (0,3);     // is always 3 long in the data I've seen!       
    std::size_t pos = line.find("(") + 1;      
    std::string Lbit = line.substr (pos,3);     // is always 3 long in the data I've seen!
    pos = line.find(",") + 2;
    std::string Rbit = line.substr (pos,3);     // is always 3 long in the data I've seen!   
//    std::cout << Lbit << ' ' << Rbit << std::endl;
    
    
    // now add to the map
    t_LRJumpTableEntry tempJumpEntry = {Lbit, Rbit};
    std::pair<std::string, t_LRJumpTableEntry> tempMapEntry = make_pair(key, tempJumpEntry);
    jumpTable.insert(tempMapEntry);
    
  }
  
  std::cout << jumpTable["AAA"].LRJumpCode[0] << " " << jumpTable["AAA"].LRJumpCode[1]  << std::endl;
  std::cout << jumpTable["BBB"].LRJumpCode[0] << " " << jumpTable["BBB"].LRJumpCode[1] << std::endl;
  std::cout << jumpTable["ZZZ"].LRJumpCode[0] << " " << jumpTable["ZZZ"].LRJumpCode[1] << std::endl;
  
  bool foundZZZ = false;
  std::string jumpCodeStr = "AAA";
  t_LRJumpTableEntry currentJumpEntry = jumpTable[jumpCodeStr];
  int numberOfJumps = 0;
  int indexToLR = 0;
  char LRCommand = '*'; //set to invalid normal value to check logic ok
  while (foundZZZ == false)
  {
    if (jumpCodeStr == "ZZZ") foundZZZ = true;
    
    LRCommand = LRCodes[indexToLR];
    if (LRCommand == 'L')
    {
      jumpCodeStr = currentJumpEntry.LRJumpCode[0];
    }
    else
    {
      jumpCodeStr = currentJumpEntry.LRJumpCode
      [1];
    }
    currentJumpEntry = jumpTable[jumpCodeStr];
      
    numberOfJumps++; 
    indexToLR++;
    if (indexToLR >= LRCodes.size()) indexToLR = 0;   // cycle LR codes
  }
  std::cout << "numberOfJumps=" << --numberOfJumps << std::endl;

  inputFile.close(); // Close the file when done reading
}