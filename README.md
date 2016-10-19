# beancount-type-stubs

To test out:

```
pip install mypy-lang
# The stubs must be in a directory named `stubs`
git clone https://github.com/yegle/beancount-type-stubs stubs
export MYPYPATH=$PWD/stubs
cd beancount/src/python
mypy -p beancount
```

NOTE: `unittest.pyi` is based on
https://github.com/python/typeshed/blob/master/stdlib/3/unittest.pyi but
added `mock = ... # type: Any` in the end, to workaround
https://github.com/python/typeshed/issues/372
