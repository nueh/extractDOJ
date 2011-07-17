This is a python script to extract plain text from a [Day One][1] journal. I use Day One both on my iPhone and my MacBook, and I think it's a great program to write down your daily thoughts and ideas. But I couldn't stand the fact, that everything was kept in an opaque bundle.


[1]:	http://www.dayoneapp.com/
[2]:	http://en.wikipedia.org/wiki/Property_list


Usage
-----
	$ ./extractDOJ.py -h
	usage: extractDOJ [-h] [-d DATE_FORMAT] [-c] [-r]
	              /Path/to/Journal.dayone [outfile]

	Extracts plain text fromy our Day One journal (http://dayoneapp.com/).

	positional arguments:
	  /Path/to/Journal.dayone
	                        Your journal file (bundle, actually)
	  outfile               save output to file OUTFILE

	optional arguments:
	  -h, --help            show this help message and exit
	  -d DATE_FORMAT        format of date (google 'strftime python')
	  -c, --csv             output CSV (tab separated values)
	  -r                    reversed order
	

Examples
--------
	./extractDOJ.py /Path/to/Journal.dayone Journal.txt
Extracts entries as plain text into file Journal.txt

	./extractDOJ.py -c /Path/to/Journal.dayone Journal.txt
Extracts entries as tab separated values into file Journal.txt. Useful to import your diary into an Excel file.