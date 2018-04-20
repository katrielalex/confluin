grammar spequation;
options { language = Python3; }

spec: (functions | equations)+;

// e.g. functions: foo/1, bar/2
functions: 'functions:' WS? function (',' WS? function)* EOL?;
function: name '/' arity;
arity: INTEGER;
name: (UPPER | LOWER)+;

// e.q. equations: a(x) = b
equations: 'equations:' WS? equation (',' WS? equation)* EOL?;
equation: term WS? '=' WS? term;

term: base | application;
base: (UPPER | LOWER)+;
application: base '(' term (',' WS? term)* ')';

EOL: '\n';
WS: [ \t\r]+ -> skip; // skip all whitespace
UPPER: ('A'..'Z');
LOWER: ('a'..'z');
INTEGER: DIGIT+;
DIGIT: '0'..'9';
