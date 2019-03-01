if [[ "$DISTRIB" == "conda" ]]; then

  # To run conda python use the following parameters
  #  DISTRUB="conda"
  #  TRAVIS_OS_NAME=["linux", "osx"]
  #  PYTHON_VERSION=["3.4", "3.5", "3.6", "3.7"]

  # Deactivate the travis-provided virtual environment and setup a
  # conda-based environment instead
  deactivate

  # Use the miniconda installer for faster download / install of conda itself
  pushd .
  cd
  mkdir -p download
  cd download
  echo "Cached in $HOME/download :"
  ls -l
 
  if [ "$TRAVIS_OS_NAME" = linux ]; then
      sudo apt-get update
      MINICONDAVERSION="Linux"
  else
      MINICONDAVERSION="MacOSX"
  fi

  echo "Set miniconda version $MINICONDAVERSION"

  echo "Get the miniconda for python 3"
  if [[ ! -f miniconda.sh ]]; then
      wget https://repo.continuum.io/miniconda/Miniconda3-latest-$MINICONDAVERSION-x86_64.sh -O miniconda.sh 
  fi

  MINICONDA_PATH=$HOME/miniconda
  chmod +x miniconda.sh && ./miniconda.sh -b -p $MINICONDA_PATH
  export PATH=$MINICONDA_PATH/bin:$PATH

  cd $TRAVIS_BUILD_DIR

  # Configure the conda environment and put it in the path using the provided versions
  conda create -n testenv --yes python=$PYTHON_VERSION numpy scipy pip cython pytest pytest-cov

  source activate testenv

  python --version
  python -c "import numpy; print('numpy %s' % numpy.__version__)"
  python -c "import scipy; print('scipy %s' % scipy.__version__)"
  python setup.py install



else
  pip3 install Cython
  pip3 install .
  pip3 install pytest-cov
fi