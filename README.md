# About
Uses face recognition technology for authorization following the "multiple persons rules" wherebe a fixed number of identified must be confirmed to authorize access to an asset class.

# Dependencies
- [face-recognition 1.3.0](https://pypi.org/project/face-recognition/) (Python Library)
- [dlib](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf) is a state-of-the-art face recognition built with deep learning. The model has an accuracy of 99.38% on the Labeled Faces in the Wild benchmark.
- [Flask v2.1](https://flask.palletsprojects.com/en/2.1.x/) is a micro web framework written in Python.

# Setup
## Install `cmake`
Note: `apt` is a package manager for Ubuntu linux. Use the appropriate method to install `cmake` in your operating system.
```
sudo apt install cmake
```

## Install `dlib`
You will need Python's package manager for this next step. Make sure `python3-pip` is installed on your computer.
```
pip install dlib
```

## Install `face-recognition`
```
pip install face-recognition
```

## Install `flask`
```
pip install flask
```

# Deploy
```
flask run
```
