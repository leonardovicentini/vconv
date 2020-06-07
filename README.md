# vconv

---

Program to convert mkv videos to mp4.

### Requirements

python3, ffmpeg

## Usage

The program has the following parameters:

parameter | meaning
--- | ---
--help | Returns the help message
--version | Returns the version of the program
--verbose | Verbose output with information about the ongoing conversion
--quiet | It doesn't return any output on the terminal
--FILE file | Specifies the path of the mkv file to be converted
--Dir DIR | Specifies the path of a folder containing the mkv files
--out | Specifies a subfolder of the indicated path where the converted files will be placed
--test | If present, set the conversion for the first 30 seconds of video only

For more information, type:

    $ vconv -h

## Changelog

**2020-06-07 02_02**

- Bug fixed: The program crashed if file had '.' in the name

**2020-04-11 02_01**

- Added: --quiet, --verbose and --test Flags.
- Bug fixed: The program crashed if the file existed
  already in the destination folder

**2020-04-11 01_01**

- First version

## Author

Leonardo Vicentini