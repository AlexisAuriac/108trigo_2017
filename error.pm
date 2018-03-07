#!/bin/perl

use strict;
use warnings;

sub help {
    print << 'END_HELP';
USAGE
    ./108trigo fun a0 a1 a2....
DESCRIPTION
    fun    function to be applied, among at least "EXP", "COS", "SIN", "COSH" and "SINH"
    ai     coeficients of the matrix
END_HELP
}

sub error {
    if (scalar @ARGV == 1 && $ARGV[0] eq "-h") {
	help();
	exit 0;
    }
    return (84);
}

1;
