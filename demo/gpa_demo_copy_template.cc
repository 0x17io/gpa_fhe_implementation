short Calculator::process(short x, short y, char op) {
  if (op == '+') {
    return x + y;
  } else if (op == '-') {
    return x - y;
  } else if (op == '*') {
    return x * y;
  } else {
    return -1;
  }
}

// TODO: Way to mark Calculator::process() as main function
#pragma hls_top
short my_package(Calculator &calc, short x, short y, char op) {
  return calc.process(x, y, op);
}
