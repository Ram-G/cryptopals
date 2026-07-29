#include "util.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int run_and_verify(solve_function solve, const char *expected) {
    char *actual;
    int result;

    if (expected == NULL) {
        fputs("error: set EXPECTED before verifying the solution\n", stderr);
        return 1;
    }
    if (solve == NULL) {
        fputs("error: solution function is not set\n", stderr);
        return 1;
    }

    actual = solve();
    if (actual == NULL) {
        fputs("error: solution returned no answer\n", stderr);
        return 1;
    }
    if (strcmp(actual, expected) != 0) {
        fprintf(stderr, "error: expected '%s', got '%s'\n", expected, actual);
        result = 1;
    } else {
        puts(actual);
        puts("✅ verified");
        result = 0;
    }

    free(actual);
    return result;
}
