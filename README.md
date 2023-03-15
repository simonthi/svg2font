# svg2font
A little repository to batch import svgs and output them as font.

## Requirements

* Fontforge

## Installing

```
make install
```

## Usage

* Put .svg files in the ```svg``` folder.  Naming convention: ```Unicod(dec).svg```i.e. 65.svg for A (Latin Capital Letter A).
* Adjust Template ```blank.sfd```to match Cap height and Descender.
* Run ```svg2font```in Terminal
