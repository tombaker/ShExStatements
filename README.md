# ShExStatements
ShExStatements allows the users to generate shape expressions from simple CSV statements and files. `shexstatements` can be also be used from the command line.

## Quick start
Clone the **ShExStatements** repository.
```
$ git clone https://github.com/johnsamuelwrites/ShExStatements.git 
```

Go to **ShExStatements** directory.
```
$ cd ShExStatements
```

Install modules required by **ShExStatements** (here: installing into a virtual environment).
```
$ python3 -m venv .venv
$ source ./.venv/bin/activate
$ pip3 install .
```

Run the following command with an example CSV file. The file contains an example description of a language on Wikidata. This file uses comma as a delimiter to separate the values.
```
$ ./shexstatements.sh examples/language.csv
```

CSV file can use delimiters like _;_. Take for example, the following command works with a file using semi-colon as a delimiter.

```
$ ./shexstatements.sh examples/languagedelimsemicolon.csv --delim ";"
```

But sometimes, users may like to specify the header. In that case, they can make use of `-s` or `--skipheader` to tell the generator to skip the header (firsrt line of CSV).

```
$ ./shexstatements.sh --skipheader examples/languageheader.csv 
```

In all the above cases, the shape expression generated by **ShExStatements** will look like
```
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
start = @<language>
<language> {
  wdt:P31 [ wd:Q34770  ] ;# instance of a language
  wdt:P1705 LITERAL ;# native name
  wdt:P17 .+ ;# spoken in country
  wdt:P2989 .+ ;# grammatical cases
  wdt:P282 .+ ;# writing system
  wdt:P1098 .+ ;# speakers
  wdt:P1999 .* ;# UNESCO language status
  wdt:P2341 .+ ;# indigenous to
}
```

Use `-j` or `--shexj` to generate ShEx JSON Syntax (ShExJ) instead of default ShEx Compact syntax (ShExC).

```
$ ./shexstatements.sh --shexj examples/language.csv 
```

The output will be similiar to:

```json
{
  "type": "Schema",
  "start": "language",
  "shapes": [
    {
      "type": "Shape",
      "id": "language",
      "expression": {

      }
    }
  ]
}
```
It's also possible to use application profiles of the following form
```
Entity_name,Property,Property_label,Mand,Repeat,Value,Value_type,Annotation
```
and Shape expressions can be generated using the following form
```
$ ./shexstatements.sh -ap --skipheader examples/languageap.csv 
```


## Objectives
* Easily generate shape expressions (ShEx) from CSV files 
* Simple syntax


## Documentation and examples
A detailed documentation can be found [here](./docs.md). with a number of example CSV files in the [examples](examples/) folder.

## Test cases
All the test cases can be run in  the following manner
```
$ python3 -m tests.tests
```

## Author
* John Samuel

## Acknowledgements
* Wikidata Community

## Archives and Releases
* [Zenodo](https://doi.org/10.5281/zenodo.3723870)
* [Release Notes](RELEASE.md)

## Licence
All code are released under GPLv3+ licence. The associated documentation and other content are released under [CC-BY-SA](http://creativecommons.org/licenses/by-sa/4.0/).
