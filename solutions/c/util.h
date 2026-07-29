#ifndef CRYPTOPALS_C_UTIL_H
#define CRYPTOPALS_C_UTIL_H

#include <stddef.h>

/* The caller owns and frees each non-null answer returned by solve. */
typedef char *(*solve_function)(void);

int run_and_verify(solve_function solve, const char *expected);

#endif
