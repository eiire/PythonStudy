Convert 7-digit number mask to regular expression for REGEXP_LIKE
-----------------------------------------------------------------
*\*The input is a csv file with masks listed in the column.*

*\*The output is a text file with regular expressions. (regexps.tst in folder where the script was launched)*

The input is either the absolute path to the file, or the name of the required file in the same folder where the **script was launched**.

Example: ABCCBNC -> (.){3}(\\d)([^\\2])([^\\2\\3])\\4\\3([^\\2\\3\\4])\\4;
1A1111A -> (.){3}[1](\\d)[1][1][1][1]\\2