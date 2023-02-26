# Benchmarks for ID generation libraries

A computational performance comparison of several Python libraries to generate
unique identifiers.

## Benchmarks

The benchmarks are quite simple and consist of generating IDs using each library's raw interface as much as possible, e.g. the UUID module is benchmarked by measuring the execution time of the `uuid.uuid4` function in the `test_generate` benchmark. These methods generally return a custom ID object for each implementation. Serializing this object into a string or some other primitive data time is not benchmarked for now.

Measurements are taken using [Pytest's benchmark plugin](https://pytest-benchmark.readthedocs.io/en/latest/index.html).

Converting a primary data type representation of an ID into an ID object is also measured for libraries that support it in the `test_parse` benchmark.


## Contenders

- [Python's own UUID module](https://docs.python.org/3/library/uuid.html) to generate v4 UUIDs with `uuid.uuid4()`.
- KSUID implementations:
    - [svix-ksuid](https://pypi.org/project/svix-ksuid/) with the standard second-precision implementation
    - [cyksuid](https://pypi.org/project/cyksuid/)
- [ulid-py](https://pypi.org/project/ulid-py/)
- [timeflake](https://pypi.org/project/timeflake/)
- [snowflake-id](https://pypi.org/project/snowflake-id/)
- [cuid2](https://pypi.org/project/cuid2/)


## Results

    ----------------- benchmark 'test_generate': 7 tests -----------------
    Name (time in ns)                 Mean                StdDev          
    ----------------------------------------------------------------------
    generate[snowflake]           510.3674 (1.0)         34.7764 (1.0)    
    generate[cyksuid]             703.0988 (1.38)       134.8331 (3.88)   
    generate[python-ulid]       1,782.9683 (3.49)       310.6836 (8.93)   
    generate[uuid4]             2,048.1680 (4.01)       148.8192 (4.28)   
    generate[timeflake]         3,011.9192 (5.90)       845.7420 (24.32)  
    generate[svix]              3,846.1195 (7.54)       322.3794 (9.27)   
    generate[cuid2]           320,325.8478 (627.64)   4,523.1247 (130.06) 
    ----------------------------------------------------------------------

The fastest library was `snowflake-id` closely followed by `cyksuid`. The rest of the libraries were within the same order of magnitude, except for `cuid2` which was around 600 times slower.

    ---------------- benchmark 'test_parse': 5 tests ----------------
    Name (time in ns)            Mean                StdDev          
    -----------------------------------------------------------------
    parse[cyksuid]           598.0682 (1.0)        406.8139 (1.03)   
    parse[uuid4]           1,465.1938 (2.45)       461.9078 (1.17)   
    parse[snowflake]       1,579.4932 (2.64)       395.6732 (1.0)    
    parse[timeflake]       4,072.7568 (6.81)       718.6803 (1.82)   
    parse[svix]           23,996.5575 (40.12)    2,584.3945 (6.53)   
    -----------------------------------------------------------------

For libraries that allowed serializing and parsing primitive representations, results were very similar to generation.

## Reproducing the experiment.

Measurements were performed with Python 3.11.2 running on Pop!_OS 22.04 LTS (based in Ubuntu / Debian, Linux kernel v6.0.12). Hardware was an MSI Prestige 14 laptop purchased in September 2020 with an Intel(R) Core(TM) i7-10710U CPU with 16GB of RAM.

To reproduce the results, install Python 3.11.2 and then install all required packages with `pip install -r requirements.txt` (it is recommended to use a [virtual environment](https://github.com/pypa/virtualenv)).

Use GNU `make` to run the benchmark suite with

    make

Alternatively, run `pytest` manually with `pytest bench.py`.