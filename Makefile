.DEFAULT_GOAL := all

CC ?= cc
C_STANDARD_FLAGS := -std=c17 -Wall -Wextra -Wpedantic -g
C_SOURCES := $(wildcard solutions/c/set*/ch*.c)
C_BINARIES := $(patsubst solutions/c/%.c,.build/c/%,$(C_SOURCES))

.PHONY: all c

all: c

c: $(C_BINARIES)

.build/c/%: solutions/c/%.c solutions/c/util.c solutions/c/util.h Makefile
	@mkdir -p "$(@D)"
	$(CC) $(CPPFLAGS) $(C_STANDARD_FLAGS) $(CFLAGS) "$<" \
		solutions/c/util.c $(LDFLAGS) $(LDLIBS) -o "$@"
