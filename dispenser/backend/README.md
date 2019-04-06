# Dispenser
A simulation of a cash dispenser written for a recruitment process and
later enhanced to serve as a code sample.

## Assumptions

## Usage

## Todo
1. Only a mapping of available notes passed to the dispenser. 
Based on this a single ChainDivisor object created. 
An ordered sequence of notes has to be saved in dispenser as well.
2. ChainDivisor spits out a Request object which can be queried for a note
and returns how many to dispense. Request has to expose method checking 
whether the amount is exhausted. Then something has to supervise the
individual dispensing. Think whether ChainDivisor operates on Request
internally (atm it does). Test it, correcy typing.
3. Make sure internals of no object are compromised. Rethink
where getters and setters are appropriate.
4. Rethink dispenser_types: rename the file, introduce note type,
allow for infinity in number of notes
5. Inspect tests and mocks; do not test internals (e.g. processor)
6. Inspect RegularNoteProcessor's logic
