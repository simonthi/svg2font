# svg2font
A little repository to batch import svgs and output them as font.

## Requirements

* Fontforge

## Installing

```
make install
```

## Usage

* Put .svg files in the ```svg``` folder.  Naming convention: ```Unicode(dec).svg```i.e. 65.svg for A (Latin Capital Letter A).
* Adjust Template ```blank.sfd```to match Cap height and Descender.
* Move to your directory which should look as follows:
  
  ```
  |-  blank.sfd
  |-  svg
      |- 65.svg
      |- 66.svg
      |- …
   ```
   
   .svg should be named usind their ASCII or Unicode decimal value.
* Run```svg2font```in Terminal
