Make sure to build docker as described in here: https://github.com/google/fully-homomorphic-encryption
Run the below commands to get started within the docker container:

apt-get install curl -y && apt-get install emacs -y && curl https://sh.rustup.rs -sSf | sh
source "$HOME/.cargo/env"

bazel run //transpiler/examples/hangman:hangman_client
calculate((short) atoi(argv[1]), (short) atoi(argv[2]), (short) atoi(argv[3]), (short) atoi(argv[4])); 


build:
bazel build -c opt //transpiler/codelab/gpa_demo:gpa_demo.transpiled_files

run:
bazel run -c opt gpa_demo:gpa_cleartext_test

option 2
bazel run gpa_demo:gpa_cleartext_test

run:
bazel run -c opt gpa_demo:gpa_cleartext_test -- 20 30 40 15
