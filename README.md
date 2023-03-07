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

[Full results are available in here](https://github.com/knifecake/python-id-benchmarks/blob/main/results.json).

    ----------------- benchmark 'test_generate': 7 tests -----------------
    Name (time in ns)                 Mean                StdDev          
    ----------------------------------------------------------------------
    generate[snowflake]           492.1435 (1.0)         46.7127 (1.0)    
    generate[cyksuid]             695.9376 (1.41)       119.0593 (2.55)   
    generate[python-ulid]       1,719.8319 (3.49)       240.3840 (5.15)   
    generate[uuid4]             1,961.3799 (3.99)       119.5277 (2.56)   
    generate[timeflake]         2,637.3506 (5.36)       451.9482 (9.68)   
    generate[svix]              3,746.8204 (7.61)       685.0287 (14.66)  
    generate[cuid2]           317,832.6200 (645.81)   4,876.3859 (104.39) 
    ----------------------------------------------------------------------

The fastest library was `snowflake-id` closely followed by `cyksuid`. The rest of the libraries were within the same order of magnitude, except for `cuid2` which was around 600 times slower.

    --------------- benchmark 'test_parse': 5 tests ---------------
    Name (time in ns)            Mean              StdDev          
    ---------------------------------------------------------------
    parse[cyksuid]           477.9390 (1.0)       87.9305 (1.0)    
    parse[uuid4]           1,373.0170 (2.87)     257.4402 (2.93)   
    parse[snowflake]       1,542.9839 (3.23)     370.3375 (4.21)   
    parse[timeflake]       3,866.8549 (8.09)     334.3074 (3.80)   
    parse[svix]           23,713.3479 (49.62)    952.0104 (10.83)  
    ---------------------------------------------------------------

For libraries that allowed serializing and parsing primitive representations, results were very similar to generation.

## Reproducing the experiment

Measurements were performed with Python 3.11.2 running on Pop!_OS 22.04 LTS (based in Ubuntu / Debian, Linux kernel v6.0.12). Hardware was an MSI Prestige 14 laptop purchased in September 2020 with an Intel(R) Core(TM) i7-10710U CPU with 16GB of RAM.

To reproduce the results, install Python 3.11.2 and then install all required packages with `pip install -r requirements.txt` (it is recommended to use a [virtual environment](https://github.com/pypa/virtualenv)).

Use GNU `make` to run the benchmark suite with

    make

Alternatively, run `pytest` manually with `pytest bench.py`.

## License

The data and scripts used to perform benchmarks are dedicated to the public domain. Libraries used in this project have their own licenses which are linked to above.