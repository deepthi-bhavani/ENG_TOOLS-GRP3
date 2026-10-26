## TestPyPI Package

Package URL: https://test.pypi.org/project/epita-deepthi-dataanalytics/

### Installation and Usage

The package can be tested from a fresh environment using:

```powershell
uv run --no-project --with epita-deepthi-dataanalytics --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ epita-deepthi-cli
```

### Wheel vs. Source Distribution

A wheel (`.whl`) is a pre-built distribution, so installation is generally faster and does not require building the package from source. A source distribution (`.tar.gz`) contains the source files and build configuration, allowing the package to be built during installation. Both distributions are useful, but wheels are usually more convenient for users.
