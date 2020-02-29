#build python package build dependency
operation=$1

function setup() {

  pip install wheel twine matplotlib numpy pandas scikit-learn
}

function install() {
    pip install dist/*.tar.gz
}

function build() {

      #Uploading the created python package for testing
      python setup.py sdist bdist_wheel

}


function release() {
    python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
}

function clean() {
 #delete old packages create
 rm -rf dist/* build/*
 pip  uninstall pyExplore -y
}

if [ "$operation" == "clean" ]
then
  clean
elif [ "$operation" == "build" ]
then
  build
elif [ "$operation" == "setup" ]
then
  setup
elif [ "$operation" == "release" ]
then
  release
elif [ "$operation" == "install" ]
then
  install
else
  clean
  build
  install
fi
