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

    ------------------ benchmark 'test_generate': 7 tests -----------------
    Name (time in ns)                 Mean                 StdDev          
    -----------------------------------------------------------------------
    generate[snowflake]           636.7661 (1.0)         779.1200 (1.0)    
    generate[cyksuid]             791.9977 (1.24)      2,900.1399 (3.72)   
    generate[python-ulid]       1,960.5808 (3.08)      2,636.9567 (3.38)   
    generate[uuid4]             2,320.8571 (3.64)      3,943.6629 (5.06)   
    generate[timeflake]         3,531.1497 (5.55)      6,503.3901 (8.35)   
    generate[svix]              4,447.4623 (6.98)      6,877.8612 (8.83)   
    generate[cuid2]           355,568.9206 (558.40)   95,253.4169 (122.26) 
    -----------------------------------------------------------------------

The fastest library was `snowflake-id` closely followed by `cyksuid`. The rest of the libraries were within the same order of magnitude, except for `cuid2` which was around 600 times slower.

    ---------------- benchmark 'test_parse': 5 tests -----------------
    Name (time in ns)            Mean                 StdDev          
    ------------------------------------------------------------------
    parse[cyksuid]           543.3401 (1.0)       2,270.7900 (1.0)    
    parse[uuid4]           1,600.9003 (2.95)      4,166.5666 (1.83)   
    parse[snowflake]       1,901.3237 (3.50)      3,671.0701 (1.62)   
    parse[timeflake]       4,377.6101 (8.06)      3,299.7071 (1.45)   
    parse[svix]           27,368.5353 (50.37)    16,984.4702 (7.48)   
    ------------------------------------------------------------------

For libraries that allowed serializing and parsing primitive representations, results were very similar to generation.

## Reproducing the experiment

Measurements were performed with Python 3.11.2 running on Pop!_OS 22.04 LTS (based in Ubuntu / Debian, Linux kernel v6.0.12). Hardware was an MSI Prestige 14 laptop purchased in September 2020 with an Intel(R) Core(TM) i7-10710U CPU with 16GB of RAM.

To reproduce the results, install Python 3.11.2 and then install all required packages with `pip install -r requirements.txt` (it is recommended to use a [virtual environment](https://github.com/pypa/virtualenv)).

Use GNU `make` to run the benchmark suite with

    make

Alternatively, run `pytest` manually with `pytest bench.py`.

## License

The data and scripts used to perform benchmarks are dedicated to the public domain. Libraries used in this project have their own licenses which are linked to above.