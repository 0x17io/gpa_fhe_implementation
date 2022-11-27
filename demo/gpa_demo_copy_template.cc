short Calculator::process(char gpa_data[]) {
    float sum = 0;
    float number_of_grades = 0;

    // Go through string, only add numbers
#pragma hls_unroll yes
    for (int i = 0; gpa_data[i] != '\0'; i++) {
        if (gpa_data[i] == ' ') {
            continue;
        }
        else {
            number_of_grades += 1;
            switch (gpa_data[i]) {
            case 'A':
                sum += 4;
                break;
            case 'B':
                sum += 3;
                break;
            case 'C':
                sum += 2;
                break;
            case 'D':
                sum += 1;
                break;
            case 'F':
                sum += 0;
                break;
            }
        }
    } 


    return sum / (number_of_grades * 4);
}

// TODO: Way to mark Calculator::process() as main function
#pragma hls_top
short my_package(Calculator &calc, char gpa_data[]) {
  return calc.process(gpa_data);
}
