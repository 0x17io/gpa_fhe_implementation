# gpa_fhe_implementation
The only way this code will work is if you fully install: https://github.com/google/fully-homomorphic-encryption This does take quite a long time.

When running the docker file, ensure that you initialize your session with the following commands:
intro
apt-get install curl -y && apt-get install emacs -y && curl https://sh.rustup.rs -sSf | sh
source "$HOME/.cargo/env"

Make FHE
bazel run //transpiler/examples/hangman:hangman_client



build:
bazel build -c opt //transpiler/codelab/gpa_demo:gpa_demo.transpiled_files

run:
bazel run -c opt gpa_demo:gpa_cleartext_test

option 2
bazel run gpa_demo:gpa_cleartext_test

run:
bazel run -c opt gpa_demo:gpa_cleartext_test -- 20 30 40 15
