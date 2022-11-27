#ifndef FULLY_HOMOMORPHIC_ENCRYPTION_TRANSPILER_EXAMPLES_CALCULATOR_H_CUSTOM_
#define FULLY_HOMOMORPHIC_ENCRYPTION_TRANSPILER_EXAMPLES_CALCULATOR_H_CUSTOM_

// Sums and subtracts values
class Calculator {
 public:
  // Applies operand op to x and y. op can be either '-', '+' or '*'. Otherwise,
  // -1 is returned.
  short process(short w, short x, short y, short z);
};

#endif  // FULLY_HOMOMORPHIC_ENCRYPTION_TRANSPILER_EXAMPLES_CALCULATOR_H_CUSTOM_
