# Lab 03

Lab 3 asks us to go over the basics of Python, as well as run some basic example
scripts and install some third party packages.

## Installation

Just about every modern desktop or server Linux installation that I know of
comes with a version of Python pre-installed, which in my case was 3.10.9.

I also installed a program called
[micromamba](https://mamba.readthedocs.io/en/latest/index.html), which is an
alternative to the [miniconda](https://docs.conda.io/en/latest/miniconda.html)
package manager for Python. Micromamba allows me to create sandboxed
environments to install python packages in, as I generally try and avoid
installing python packages globally.

If by some miracle somebody is reading this... **please do not** install
packages from `pip` by doing something like `sudo pip install <package>`. The
issue with installing packages like this is you may cause version conflicts with
your system packages, and it can be incredibly painful to debug and fix. For the
same reason I wouldn't install packages with `pip install --user <package>`
either, as there's still the possibility for version conflicts between packages
themselves!

There's a couple possible solutions to global package installations.

The simplest is the use
[virtual environments](https://docs.python.org/3/tutorial/venv.html), which give
you a copy of the Python interpreter and pip in folder, and allow you to install
packages that can only be accessed by that environment. Virtual environments are
battle tested and have been used for years, and are fairly simple to get setup.

My chosen solution is to use micromamba, a package and environment manager. If
you've got micromamba installed, creating an environment for this lab is as easy
as `micromamba create -f ./env.yaml`, then activate it with
`micromamba activate lab_03`.

A final recommendation would be to use [pipx](https://pypi.org/project/pipx/) if
you are using a program (that gets invoked in the terminal for example) instead
of a library.

## Changes I Made

One thing I noticed is that many of the provided example scripts used older /
arguably outdated features, especially with string formatting. Here's a list of
changes I made to many of the scripts:

- Switching to f-strings

  The motivation for this one is simple, f-strings are easier to read and
  significantly faster in terms of runtime performance compared to the wonky `%`
  operator and `.format()`. You can still use the same floating point formatting
  you know and love as well.

- Adding a Main Function

  Python has no enforced concept of a main function like C / C++ / other
  compiled languages. Despite this, you should still include one, and its
  execution should be gated by the following:

  ```python
  def main():
    pass

  if __name__ == "__main__": 
    main()
  ```

  The if statement ensures that the current file is being invoked directly
  (`python my_file.py`), and only in that circumstance executes the main
  function. When importing files in python, the entire file is executed
  immediately. This includes statements / code that is just hanging around in
  the file!

- Type Hints

  Type hints are a relatively recent feature that can help you give some strong
  typing to your variables similar to how things work in compiled languages.
  There is effectively no runtime costs to using them (the Python interpreter
  ignores them completely), and they are mainly useful within your editor / IDE
  of choice, where you can catch lots of bugs due to mismatched types. Once you
  start working with larger codebases having some amount of static typing is
  essential.

## Other Things I've Done

- Adding a pyproject.toml

  [PEP 621](https://peps.python.org/pep-0621/) introduced the concept of a
  project.toml file, where all of a projects core metadata is stored for
  packaging related tools to consume, as well as other tools to have
  configuration. I've put some basic info in there, as well as configuration for
  [ruff](https://github.com/charliermarsh/ruff), my linter of choice.

- Adding a justfile

  One problem I've had for years was the need of a cross-platform script runner.
  Makefiles aren't really a great choice due to their terrible errors and
  general jank factor. In comes [just](https://github.com/casey/just), which is
  nothing but a command runner. You don't need it at all to run things in this
  repo, but it'll give you an idea of what commands I'm using most often / think
  are important.

## Running the Original Files

I've copied the original files directly from the IOT repo as of 02/13/2023.

```auto
Calendar Date: 2023-02-13
Julian Date: 2459988.5
Modified Julian Date: 59988.0
Date: 2023-02-13
Date: 02-13-23
Day of Week: Monday
Month: February
Year: 2023
26 days after the first day of classes
80 days before the last day of classes
2023-02-13 17:44:46.265485
2023-02-13 17:44:46.265535
2023-02-13 22:44:46.265545
1676328286.2655518
Mon Feb 13 17:44:46 2023
2023-02-13 17:44:46.265616
2023-02-13 22:44:46.265626
Information for New York/USA

Timezone: US/Eastern
Latitude: 40.72; Longitude: -74.00

Dawn:    2023-02-13 06:24:16.679789-05:00
Sunrise: 2023-02-13 06:52:59.652406-05:00
Noon:    2023-02-13 12:10:13-05:00
Sunset:  2023-02-13 17:27:57.563584-05:00
Dusk:    2023-02-13 17:56:41.814544-05:00
2023-02-13 Moon Phase: 20
2023-02-14 Moon Phase: 21
2023-02-15 Moon Phase: 22
2023-02-16 Moon Phase: 23
2023-02-17 Moon Phase: 24
2023-02-18 Moon Phase: 25
2023-02-19 Moon Phase: 27
2023-02-20 Moon Phase: 0
2023-02-21 Moon Phase: 1
2023-02-22 Moon Phase: 2
2023-02-23 Moon Phase: 3
2023-02-24 Moon Phase: 4
2023-02-25 Moon Phase: 5
2023-02-26 Moon Phase: 6
2023-02-27 Moon Phase: 7
2023-02-28 Moon Phase: 8
2023-03-01 Moon Phase: 8
2023-03-02 Moon Phase: 9
2023-03-03 Moon Phase: 10
2023-03-04 Moon Phase: 11
2023-03-05 Moon Phase: 12
2023-03-06 Moon Phase: 13
2023-03-07 Moon Phase: 13
2023-03-08 Moon Phase: 14
2023-03-09 Moon Phase: 15
2023-03-10 Moon Phase: 16
2023-03-11 Moon Phase: 17
2023-03-12 Moon Phase: 18
2023-03-13 Moon Phase: 19
2023-03-14 Moon Phase: 20
Library Parking, Williams Lake, Cariboo Regional District, British Columbia, Canada
(52.130143399999994, -122.14187089155848)
Stevens Institute of Technology, Field House Road, Hoboken, Hudson County, New Jersey, 07030, United States
(40.744809599999996, -74.0252392276461)
sbattery(percent=40.565493364108484, secsleft=17575, power_plugged=False)
Word Count: 1343
Top Ten Words: [('our', 26), ('their', 20), ('has', 20), ('he', 19), ('them', 15), ('these', 13), ('have', 11), ('we', 11), ('us', 11), ('people', 10)]
The number of physical cores =  4
The number of logical CPUs =  8
The utilization per second as a percentage for each CPU
[5.1, 3.1, 1.0, 3.1, 6.0, 7.1, 3.1, 6.3]
[3.0, 7.1, 5.2, 1.0, 6.1, 3.0, 2.0, 7.1]
[0.0, 0.0, 2.9, 4.0, 1.0, 2.0, 0.0, 0.0]
[2.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0]
[0.0, 4.2, 2.1, 5.1, 2.0, 0.0, 0.0, 2.0]
[1.0, 2.1, 5.1, 2.0, 0.0, 0.0, 0.0, 4.0]
[0.0, 2.1, 6.1, 4.0, 3.0, 1.0, 1.0, 3.0]
[0.0, 1.1, 1.0, 1.0, 0.0, 0.0, 1.0, 2.0]
[1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 2.0]
[1.0, 1.1, 1.0, 6.0, 0.0, 1.0, 1.0, 1.0]
Mon Feb 13 17:44:59 2023
Mon Feb 13 17:45:09 2023
```

## Running Modified Files

```auto
Calendar Date: 2023-02-13
Julian Date: 2459988.5
Modified Julian Date: 59988.0
Date: 2023-02-13
Date: 02-13-23
Day of Week: Monday
Month: February
Year: 2023
26 days after the first day of classes
80 days before the last day of classes
2023-02-13 17:43:55.200199
2023-02-13 17:43:55.200248
2023-02-13 22:43:55.200258
1676328235.200265
Mon Feb 13 17:43:55 2023
2023-02-13 17:43:55.200328
2023-02-13 22:43:55.200336
Information for New York/USA

Timezone: US/Eastern
Latitude: 40.72; Longitude: -74.00

Dawn:    2023-02-13 06:24:16.679789-05:00
Sunrise: 2023-02-13 06:52:59.652406-05:00
Noon:    2023-02-13 12:10:13-05:00
Sunset:  2023-02-13 17:27:57.563584-05:00
Dusk:    2023-02-13 17:56:41.814544-05:00
2023-02-13 Moon Phase: 20
2023-02-14 Moon Phase: 21
2023-02-15 Moon Phase: 22
2023-02-16 Moon Phase: 23
2023-02-17 Moon Phase: 24
2023-02-18 Moon Phase: 25
2023-02-19 Moon Phase: 27
2023-02-20 Moon Phase: 0
2023-02-21 Moon Phase: 1
2023-02-22 Moon Phase: 2
2023-02-23 Moon Phase: 3
2023-02-24 Moon Phase: 4
2023-02-25 Moon Phase: 5
2023-02-26 Moon Phase: 6
2023-02-27 Moon Phase: 7
2023-02-28 Moon Phase: 8
2023-03-01 Moon Phase: 8
2023-03-02 Moon Phase: 9
2023-03-03 Moon Phase: 10
2023-03-04 Moon Phase: 11
2023-03-05 Moon Phase: 12
2023-03-06 Moon Phase: 13
2023-03-07 Moon Phase: 13
2023-03-08 Moon Phase: 14
2023-03-09 Moon Phase: 15
2023-03-10 Moon Phase: 16
2023-03-11 Moon Phase: 17
2023-03-12 Moon Phase: 18
2023-03-13 Moon Phase: 19
2023-03-14 Moon Phase: 20
Library Parking, Williams Lake, Cariboo Regional District, British Columbia, Canada
(52.130143399999994, -122.14187089155848)
Stevens Institute of Technology, Field House Road, Hoboken, Hudson County, New Jersey, 07030, United States
(40.744809599999996, -74.0252392276461)
sbattery(percent=40.75783804577804, secsleft=16659, power_plugged=False)
Word Count: 1343
Top Ten Words: [('our', 26), ('their', 20), ('has', 20), ('he', 19), ('them', 15), ('these', 13), ('have', 11), ('we', 11), ('us', 11), ('people', 10)]
The number of physical cores = 4
The number of logical CPUs = 8
The utilization per second as a percentage for each CPU
[3.9, 4.0, 3.9, 1.0, 3.0, 1.0, 5.1, 7.5]
[6.9, 3.9, 6.8, 0.0, 3.0, 4.0, 6.0, 4.0]
[6.9, 9.9, 10.9, 11.7, 10.7, 5.2, 7.0, 5.9]
[4.9, 1.0, 2.0, 6.7, 4.0, 4.9, 0.0, 3.0]
[4.0, 3.0, 2.9, 11.7, 1.0, 2.0, 0.0, 1.0]
[3.9, 3.0, 4.0, 7.6, 1.0, 4.0, 3.1, 1.0]
[2.0, 1.0, 8.0, 5.0, 2.0, 5.9, 5.1, 4.9]
[4.0, 3.0, 9.8, 9.0, 2.0, 6.9, 5.9, 7.9]
[2.9, 1.0, 7.8, 2.0, 0.0, 1.0, 2.0, 13.2]
[0.0, 3.0, 4.0, 5.8, 3.0, 0.0, 0.0, 11.3]
Mon Feb 13 17:44:08 2023
Mon Feb 13 17:44:18 2023
Mon Feb 13 17:44:28 2023
Mon Feb 13 17:44:38 2023
```
