#include "calculator.h"

short Calculator::process(short w, short x, short y, short z) {
  return (short) ((w + x + y + z)/4);
}

// TODO: Way to mark Calculator::process() as main function
#pragma hls_top
short my_package(Calculator &calc, short w, short x, short y, short z) {
  return calc.process(w, x, y, z);
}
