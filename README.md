# habitat-sim-api

This repository contains two static type-stub packages that represent exclusively the **public** api of habitat-sim:
- `0.2.2/` — habitat-sim-api version 0.2.2
- `0.3.3/` — habitat-sim-api version 0.3.3

Each version folder is a self-contained, static package (committed `pyproject.toml`, `setup.cfg`, `MANIFEST.in`, `habitat_sim/*.pyi`, `py.typed`, and `_version.py`).

Requirements
- Python 3.8+
- pip
- build tools (install once in your environment):

```bash
python -m pip install --upgrade build setuptools wheel
```

Build
- Build version 0.2.2:

```bash
cd /path/to/repo/0.2.2
./build.sh
# or explicitly: bash build.sh
```

- Build version 0.3.3:

```bash
cd /path/to/repo/0.3.3
./build.sh
```

Artifacts
- Built artifacts are placed in each version folder's `dist/` directory:
  - Wheel: `habitat_sim_api-<version>-py3-none-any.whl`
  - Sdist: `habitat_sim_api-<version>.tar.gz`
- Package name (as published/installed) is `habitat-sim-api`.

Install the built package into another project/environment
- Install the wheel directly:

```bash
pip install /full/path/to/0.2.2/dist/habitat_sim_api-0.2.2-py3-none-any.whl
```

- Or install the sdist:

```bash
pip install /full/path/to/0.2.2/dist/habitat_sim_api-0.2.2.tar.gz
```

- Install from a local dist directory (useful in CI):

```bash
pip install --no-index --find-links /full/path/to/0.2.2/dist habitat-sim-api
```

How these stubs were generated

The type stubs in this repository were generated from the source code of the `habitat-sim` project (https://github.com/nunoatgithub/habitat-sim), specifically from versions 0.2.2 and 0.3.3. The following command was used to generate the stubs for each version:

```bash
stubgen --parse-only -o target src_python/habitat_sim
```

- `stubgen` is a tool from the `mypy` project that generates `.pyi` type stub files from Python source code.
- The `--parse-only` flag tells `stubgen` to generate stubs using static parsing only, without importing or executing the code (important for C++/Python bindings or code with heavy dependencies).
- The `-o target` option sets the output directory for the generated stubs.
- The `src_python/habitat_sim` specify the source directories/files to process.

This command was run separately for each code version (0.2.2 and 0.3.3) of the `habitat-sim` repository. The resulting `.pyi` files were then organized and committed into the corresponding versioned folders in this repository (`0.2.2/` and `0.3.3/`).

Caveats — these are type stubs
- The package contains `.pyi` type stubs and a `py.typed` marker only. These provide static type information for tools like mypy, pyright, and editor completions.
- The stubs do not include runtime implementations. If you try to `import habitat_sim` at runtime and the real `habitat-sim` implementation is not installed, the import may fail.
- If you want this package to be importable at runtime even without the real implementation, add a minimal `habitat_sim/__init__.py` shim (committed) with the behavior you prefer.

Troubleshooting
- During packaging, setuptools warns if `README.md` or `LICENSE` are missing. Add minimal `README.md` and `LICENSE` files into each version folder if you want to remove those warnings.
- If `python -m build` fails: ensure the build dependencies are installed (see Requirements above).
- If `./build.sh` is not executable: run `chmod +x build.sh` in the version folder.

Simple quick-commands summary

```bash
# install build deps (once)
python -m pip install --upgrade build setuptools wheel

# build both versions
bash 0.2.2/build.sh
bash 0.3.3/build.sh

# install a built wheel into an environment
pip install 0.2.2/dist/habitat_sim_api-0.2.2-py3-none-any.whl
```

