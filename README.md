Python scripts to convert BLF (CanAnalyzer trace) files to log or csv.

Prerequisites:

    - can
    
    - csv #if converting to csv
    
Usage

* To convert to candump file run as follows,
  
    `python3 blftoCandump.py input_file_name` 
    
    * Here enter input file name only. don't include file extension (.blf)
    * This will output to input_file_name_candump.log file
    
* To convert to csv file run as follows, 

    `python3 blftoCsv.py input_file_name `
    
    * Here enter input file name only. don't include file extension (.blf)
    * This will output to  input_file_name_csvdump.csv file
