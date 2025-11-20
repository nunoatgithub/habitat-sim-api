# habitat-sim-api

This repository contains 3 flavors of the habitat-sim-api:
1. with-all-types - stubs for the public and private parts of the habitat-sim package, generated from the code in the habitat-sim github repo, using
```bash
stubgen --parse-only --include-private -o target src_python/habitat_sim src_python/habitat_sim/**/*.py
```
2. with-public-types - stubs for the public parts of the habitat-sim package, generated using
```bash
stubgen --parse-only -o target src_python/habitat_sim
```

3. with-packages - automated AI extraction of a public api comprised of py files only, with abstract or empty implementations  


_Regarding 1 and 2, for the benefit of IDEs, empty package files (\_\_init\_\_.py) were also added in locations that reflect their position in the original source_

These three flavors were created for versions 0.2.2 and 0.3.3 of habitat-sim.

_What is stubgen_
- _`stubgen` is a tool from the `mypy` project that generates `.pyi` type stub files from Python source code._ 
- _The `--parse-only` flag tells `stubgen` to generate stubs using static parsing only, without importing or executing the code (important for C++/Python bindings or code with heavy dependencies)._
- _The `-o target` option sets the output directory for the generated stubs._
- _The `src_python/habitat_sim` and `src_python/habitat_sim/**/*.py` arguments specify the source directories/files to process._

Requirements
- Python 3.8+
- pip
- build tools (install once in your environment):

```bash
python -m pip install --upgrade build setuptools wheel
```

Build:

```bash
cd /path/to/repo/0.2.2 or cd /path/to/repo/0.3.3
```

then do one of the following depending on the flavor you want to build.  
```bash
./build.sh --with-all-types
./build.sh --with-public-types
./build.sh --with-packages 
```
There are not 6 separate deliverables, but one single distro for 0.2.2 and another for 0.3.3, one decides which flavor it contains by running the proper build script. A pragmatic choice for now.

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

Troubleshooting
- During packaging, setuptools warns if `README.md` or `LICENSE` are missing. Add minimal `README.md` and `LICENSE` files into each version folder if you want to remove those warnings.
- If `python -m build` fails: ensure the build dependencies are installed (see Requirements above).
- If `./build.sh` is not executable: run `chmod +x build.sh` in the version folder.


---

**Annex : Small reminder about how distribution works in python**

This is a short reminder of what you find under each `dist/` and how to use those artifacts.

What you typically find in `dist/`
- Wheel (`.whl`): a built binary (for pure-Python packages this is a zip) that contains package files and metadata. Example: `habitat_sim_api-0.2.2-py3-none-any.whl`.
- Source distribution (`sdist`, `.tar.gz` or `.zip`): the source archive that contains the package sources and metadata. Example: `habitat_sim_api-0.2.2.tar.gz`.
- The temporary `build/` or `bdist.*` directories are intermediate build outputs and are not needed for installation.

Which to use
- Prefer the wheel: it's ready to install and fast (no build step).
- Use the sdist only if a wheel is not available; pip will build from the sdist which can be slower and may require build-time deps.

Install examples (local/offline/private use)
- Install a wheel directly (recommended):

```bash
pip install /full/path/to/<version>/dist/habitat_sim_api-0.2.2-py3-none-any.whl
```

- Install a source archive:

```bash
pip install /full/path/to/<version>/dist/habitat_sim_api-0.2.2.tar.gz
```

- Install from a local directory of artifacts (useful for CI or air-gapped environments):

```bash
pip install --no-index --find-links /full/path/to/<version>/dist 'habitat-sim-api==0.2.2'
```

- Host a simple HTTP index (ephemeral) for a folder of wheels:

```bash
cd /full/path/to/<version>/dist
python -m http.server 8000
# on the client machine
pip install --index-url http://<host>:8000/simple/ --no-deps habitat-sim-api==0.2.2
```

Inspecting artifacts
- List wheel contents:

```bash
unzip -l /path/to/*.whl
```

- Read package metadata (METADATA or PKG-INFO):

```bash
unzip -p /path/to/*.whl '*/METADATA' | sed -n '1,120p'
# or
tar -xOzf /path/to/*.tar.gz PKG-INFO | sed -n '1,120p'
```

Notes about types-only packages
- Ensure `py.typed` is included inside the packaged `habitat_sim` directory so type checkers pick up the `.pyi` stubs (PEP 561).
- The wheel filename `py3-none-any.whl` indicates the wheel is universal across Python 3 interpreters (suitable for 3.8+ as you specified).
